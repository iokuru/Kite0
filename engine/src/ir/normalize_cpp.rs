use super::arena::{BlockId, ExprId, StmtId};
use super::ast::*;
use crate::parser::AstNode;

pub struct CppNormalizer<'a> {
    source: &'a [u8],
    module: IrModule,
    in_solution_class: bool,
    current_access_public: bool,
}

impl<'a> CppNormalizer<'a> {
    pub fn new(source: &'a str) -> Self {
        Self {
            source: source.as_bytes(),
            module: IrModule::new(),
            in_solution_class: false,
            current_access_public: false,
        }
    }

    pub fn normalize(mut self, root: &'a AstNode) -> IrModule {
        self.visit_node(root);
        self.module
    }

    fn text(&self, node: &AstNode) -> String {
        node.text(self.source).to_string()
    }

    fn visit_node(&mut self, node: &'a AstNode) {
        match node.kind() {
            "function_definition" => {
                self.visit_function(node);
            }
            "class_specifier" | "struct_specifier" => {
                let name = node
                    .child_by_field_name("name")
                    .map(|n| self.text(n))
                    .unwrap_or_default();
                let is_sol = name == "Solution";
                if is_sol {
                    self.module.has_solution_class = true;
                }
                let prev_sol = self.in_solution_class;
                let prev_access = self.current_access_public;
                self.in_solution_class = is_sol;
                self.current_access_public = node.kind() == "struct_specifier";

                if let Some(body) = node.child_by_field_name("body") {
                    for child in &body.children {
                        if child.kind() == "access_specifier" {
                            let txt = self.text(child);
                            if txt.contains("public") {
                                self.current_access_public = true;
                            } else if txt.contains("private") || txt.contains("protected") {
                                self.current_access_public = false;
                            }
                        } else {
                            self.visit_node(child);
                        }
                    }
                } else {
                    for child in &node.children {
                        self.visit_node(child);
                    }
                }

                self.in_solution_class = prev_sol;
                self.current_access_public = prev_access;
            }
            "translation_unit" => {
                for child in &node.children {
                    self.visit_node(child);
                }
            }
            _ => {
                for child in &node.children {
                    self.visit_node(child);
                }
            }
        }
    }

    fn visit_function(&mut self, node: &'a AstNode) {
        let decl_node = node.child_by_field_name("declarator");
        let raw_name = decl_node
            .map(|d| self.text(d))
            .unwrap_or_else(|| "anon".to_string());
        let name = raw_name
            .split('(')
            .next()
            .unwrap_or("anon")
            .trim()
            .to_string();

        let mut params = Vec::new();
        if let Some(d) = decl_node {
            self.extract_cpp_params(d, &mut params);
        }

        let body_node = node.child_by_field_name("body");
        let body_block = if let Some(body) = body_node {
            self.lower_block(body)
        } else {
            self.module.alloc_block(IrBlock::default())
        };

        self.module.functions.push(IrFunction {
            name,
            is_public: if self.in_solution_class {
                self.current_access_public
            } else {
                true
            },
            is_in_solution_class: self.in_solution_class,
            params,
            body: body_block,
        });
    }

    fn extract_cpp_params(&self, node: &'a AstNode, params: &mut Vec<IrParam>) {
        if node.kind() == "parameter_list" {
            for child in &node.children {
                if child.kind() == "parameter_declaration" {
                    let type_name = child
                        .child_by_field_name("type")
                        .map(|t| self.text(t))
                        .unwrap_or_default();
                    let raw_pname = child
                        .child_by_field_name("declarator")
                        .map(|d| self.text(d))
                        .unwrap_or_default();
                    let pname = raw_pname
                        .trim_start_matches('&')
                        .trim_start_matches('*')
                        .trim()
                        .to_string();
                    params.push(IrParam {
                        name: pname,
                        type_name,
                    });
                }
            }
        } else {
            for child in &node.children {
                self.extract_cpp_params(child, params);
            }
        }
    }

    pub fn lower_block(&mut self, node: &'a AstNode) -> BlockId {
        let mut stmts = Vec::new();
        for child in &node.children {
            if child.kind() == "{" || child.kind() == "}" || child.kind() == ";" {
                continue;
            }
            if let Some(stmt_id) = self.lower_statement(child) {
                stmts.push(stmt_id);
            }
        }
        self.module.alloc_block(IrBlock { stmts })
    }

    pub fn lower_statement(&mut self, node: &'a AstNode) -> Option<StmtId> {
        match node.kind() {
            "compound_statement" => {
                let block_id = self.lower_block(node);
                let dummy_expr = self.module.alloc_expr(IrExpr::LiteralInt(0));
                let dummy_stmt = self.module.alloc_stmt(IrStmt::Expr(dummy_expr));
                if let Some(b) = self.module.blocks.get(block_id.0) {
                    if let Some(first) = b.stmts.first() {
                        return Some(*first);
                    }
                }
                Some(dummy_stmt)
            }
            "expression_statement" => {
                for child in &node.children {
                    if child.kind() != ";" {
                        return self.lower_statement(child);
                    }
                }
                None
            }
            "for_statement" => {
                let init = node
                    .child_by_field_name("initializer")
                    .and_then(|n| self.lower_statement(n));
                let cond = node
                    .child_by_field_name("condition")
                    .map(|n| self.lower_expr(n));
                let step = node
                    .child_by_field_name("update")
                    .and_then(|n| self.lower_statement(n));
                let body_node = node.child_by_field_name("body");
                let body = if let Some(b) = body_node {
                    if b.kind() == "compound_statement" {
                        self.lower_block(b)
                    } else if let Some(stmt) = self.lower_statement(b) {
                        self.module.alloc_block(IrBlock { stmts: vec![stmt] })
                    } else {
                        self.module.alloc_block(IrBlock::default())
                    }
                } else {
                    self.module.alloc_block(IrBlock::default())
                };

                let stmt = IrStmt::For {
                    init,
                    cond,
                    step,
                    body,
                };
                Some(self.module.alloc_stmt(stmt))
            }
            "for_range_loop" => {
                let body_node = node.child_by_field_name("body");
                let body = if let Some(b) = body_node {
                    if b.kind() == "compound_statement" {
                        self.lower_block(b)
                    } else if let Some(stmt) = self.lower_statement(b) {
                        self.module.alloc_block(IrBlock { stmts: vec![stmt] })
                    } else {
                        self.module.alloc_block(IrBlock::default())
                    }
                } else {
                    self.module.alloc_block(IrBlock::default())
                };

                let iter_var = self.module.alloc_expr(IrExpr::Var("__iter".to_string()));
                let bound_expr = if let Some(right_node) = node.child_by_field_name("right") {
                    self.lower_expr(right_node)
                } else {
                    self.module.alloc_expr(IrExpr::Var("n".to_string()))
                };
                let cond_expr = self.module.alloc_expr(IrExpr::Binary(
                    BinaryOp::Lt,
                    iter_var,
                    bound_expr,
                ));

                let zero = self.module.alloc_expr(IrExpr::LiteralInt(0));
                let init_stmt = self.module.alloc_stmt(IrStmt::Assign("__iter".to_string(), zero));

                let one = self.module.alloc_expr(IrExpr::LiteralInt(1));
                let next_iter = self.module.alloc_expr(IrExpr::Binary(BinaryOp::Add, iter_var, one));
                let step_stmt = self.module.alloc_stmt(IrStmt::Assign("__iter".to_string(), next_iter));

                let stmt = IrStmt::For {
                    init: Some(init_stmt),
                    cond: Some(cond_expr),
                    step: Some(step_stmt),
                    body,
                };
                Some(self.module.alloc_stmt(stmt))
            }
            "while_statement" => {
                let cond = node
                    .child_by_field_name("condition")
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralBool(true)));
                let body_node = node.child_by_field_name("body");
                let body = if let Some(b) = body_node {
                    if b.kind() == "compound_statement" {
                        self.lower_block(b)
                    } else if let Some(stmt) = self.lower_statement(b) {
                        self.module.alloc_block(IrBlock { stmts: vec![stmt] })
                    } else {
                        self.module.alloc_block(IrBlock::default())
                    }
                } else {
                    self.module.alloc_block(IrBlock::default())
                };

                Some(self.module.alloc_stmt(IrStmt::While { cond, body }))
            }
            "do_statement" => {
                let cond = node
                    .child_by_field_name("condition")
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralBool(true)));
                let body_node = node.child_by_field_name("body");
                let body = if let Some(b) = body_node {
                    if b.kind() == "compound_statement" {
                        self.lower_block(b)
                    } else if let Some(stmt) = self.lower_statement(b) {
                        self.module.alloc_block(IrBlock { stmts: vec![stmt] })
                    } else {
                        self.module.alloc_block(IrBlock::default())
                    }
                } else {
                    self.module.alloc_block(IrBlock::default())
                };

                Some(self.module.alloc_stmt(IrStmt::While { cond, body }))
            }
            "comma_expression" => {
                for child in &node.children {
                    if child.kind() != "," && child.kind() != ";" {
                        if let Some(stmt) = self.lower_statement(child) {
                            return Some(stmt);
                        }
                    }
                }
                None
            }
            "if_statement" => {
                let cond = node
                    .child_by_field_name("condition")
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralBool(true)));

                let cons_node = node.child_by_field_name("consequence");
                let then_block = if let Some(c) = cons_node {
                    if c.kind() == "compound_statement" {
                        self.lower_block(c)
                    } else if let Some(stmt) = self.lower_statement(c) {
                        self.module.alloc_block(IrBlock { stmts: vec![stmt] })
                    } else {
                        self.module.alloc_block(IrBlock::default())
                    }
                } else {
                    self.module.alloc_block(IrBlock::default())
                };

                let else_block = node.child_by_field_name("alternative").map(|alt| {
                    if alt.kind() == "compound_statement" {
                        self.lower_block(alt)
                    } else if let Some(stmt) = self.lower_statement(alt) {
                        self.module.alloc_block(IrBlock { stmts: vec![stmt] })
                    } else {
                        self.module.alloc_block(IrBlock::default())
                    }
                });

                Some(self.module.alloc_stmt(IrStmt::If {
                    cond,
                    then_block,
                    else_block,
                }))
            }
            "return_statement" => {
                let mut ret_expr = None;
                for child in &node.children {
                    if child.kind() != "return" && child.kind() != ";" {
                        ret_expr = Some(self.lower_expr(child));
                        break;
                    }
                }
                Some(self.module.alloc_stmt(IrStmt::Return(ret_expr)))
            }
            "break_statement" => Some(self.module.alloc_stmt(IrStmt::Break)),
            "continue_statement" => Some(self.module.alloc_stmt(IrStmt::Continue)),
            "declaration" => {
                let type_node = node.child_by_field_name("type");
                let type_text = type_node.map(|t| self.text(t)).unwrap_or_default();
                let is_container = is_cpp_container(&type_text);

                for child in &node.children {
                    if child.kind() == "init_declarator" {
                        let decl_node = child.child_by_field_name("declarator");
                        let is_array_decl = decl_node
                            .map(|d| d.kind() == "array_declarator")
                            .unwrap_or(false);

                        if is_array_decl {
                            let ad = decl_node.unwrap();
                            let var_name = ad
                                .child_by_field_name("declarator")
                                .map(|d| self.text(d))
                                .unwrap_or_else(|| "var".to_string());
                            let size_node = ad.child_by_field_name("size").or_else(|| {
                                ad.children.iter().find(|c| {
                                    c.kind() != "["
                                        && c.kind() != "]"
                                        && c.field_name.as_deref() != Some("declarator")
                                })
                            });
                            let size_expr = size_node.map(|s| self.lower_expr(s));
                            let alloc = IrAlloc {
                                var: var_name,
                                type_name: format!("{type_text}[]"),
                                size: size_expr,
                            };
                            self.module.allocations.push(alloc.clone());
                            return Some(self.module.alloc_stmt(IrStmt::Alloc(alloc)));
                        }

                        let var_name = decl_node
                            .map(|d| self.text(d))
                            .unwrap_or_else(|| "var".to_string());
                        let value_node = child.child_by_field_name("value");

                        if let Some(v) = value_node {
                            if v.kind() == "argument_list" {
                                let first_arg = v.children.iter().find(|c| {
                                    c.kind() != "(" && c.kind() != ")" && c.kind() != ","
                                });
                                let size_expr = first_arg.map(|a| self.lower_expr(a));
                                let alloc = IrAlloc {
                                    var: var_name,
                                    type_name: type_text.clone(),
                                    size: size_expr,
                                };
                                self.module.allocations.push(alloc.clone());
                                return Some(self.module.alloc_stmt(IrStmt::Alloc(alloc)));
                            }
                        }

                        if is_container {
                            let alloc = IrAlloc {
                                var: var_name,
                                type_name: type_text.clone(),
                                size: None,
                            };
                            self.module.allocations.push(alloc.clone());
                            return Some(self.module.alloc_stmt(IrStmt::Alloc(alloc)));
                        }

                        let val_expr = if let Some(v) = value_node {
                            self.lower_expr(v)
                        } else {
                            self.module.alloc_expr(IrExpr::LiteralInt(0))
                        };
                        return Some(self.module.alloc_stmt(IrStmt::Assign(var_name, val_expr)));
                    } else if child.kind() == "array_declarator" {
                        let var_name = child
                            .child_by_field_name("declarator")
                            .map(|d| self.text(d))
                            .unwrap_or_else(|| "var".to_string());
                        let size_node = child.child_by_field_name("size").or_else(|| {
                            child.children.iter().find(|c| {
                                c.kind() != "["
                                    && c.kind() != "]"
                                    && c.field_name.as_deref() != Some("declarator")
                            })
                        });
                        let size_expr = size_node.map(|s| self.lower_expr(s));
                        let alloc = IrAlloc {
                            var: var_name,
                            type_name: format!("{type_text}[]"),
                            size: size_expr,
                        };
                        self.module.allocations.push(alloc.clone());
                        return Some(self.module.alloc_stmt(IrStmt::Alloc(alloc)));
                    } else if child.kind() == "function_declarator" && is_container {
                        let var_name = child
                            .child_by_field_name("declarator")
                            .map(|d| self.text(d))
                            .unwrap_or_else(|| "var".to_string());
                        let param_list = child.child_by_field_name("parameters");
                        let size_expr = if let Some(pl) = param_list {
                            let param = pl
                                .children
                                .iter()
                                .find(|c| c.kind() == "parameter_declaration");
                            if let Some(p) = param {
                                let p_text = self.text(p).trim().to_string();
                                Some(self.module.alloc_expr(IrExpr::Var(p_text)))
                            } else {
                                None
                            }
                        } else {
                            None
                        };
                        let alloc = IrAlloc {
                            var: var_name,
                            type_name: type_text.clone(),
                            size: size_expr,
                        };
                        self.module.allocations.push(alloc.clone());
                        return Some(self.module.alloc_stmt(IrStmt::Alloc(alloc)));
                    } else if child.kind() == "identifier" && is_container {
                        let var_name = self.text(child);
                        let alloc = IrAlloc {
                            var: var_name,
                            type_name: type_text.clone(),
                            size: None,
                        };
                        self.module.allocations.push(alloc.clone());
                        return Some(self.module.alloc_stmt(IrStmt::Alloc(alloc)));
                    }
                }
                None
            }
            "assignment_expression" => {
                let left = node
                    .child_by_field_name("left")
                    .map(|n| self.text(n))
                    .unwrap_or_else(|| "var".to_string());
                let right_node = node.child_by_field_name("right");
                let op = node
                    .child_by_field_name("operator")
                    .map(|n| self.text(n))
                    .unwrap_or_else(|| "=".to_string());
                let right = if let Some(r) = right_node {
                    let r_expr = self.lower_expr(r);
                    match op.as_str() {
                        "+=" => {
                            let l_expr = self.module.alloc_expr(IrExpr::Var(left.clone()));
                            self.module
                                .alloc_expr(IrExpr::Binary(BinaryOp::Add, l_expr, r_expr))
                        }
                        "-=" => {
                            let l_expr = self.module.alloc_expr(IrExpr::Var(left.clone()));
                            self.module
                                .alloc_expr(IrExpr::Binary(BinaryOp::Sub, l_expr, r_expr))
                        }
                        "*=" => {
                            let l_expr = self.module.alloc_expr(IrExpr::Var(left.clone()));
                            self.module
                                .alloc_expr(IrExpr::Binary(BinaryOp::Mul, l_expr, r_expr))
                        }
                        "/=" => {
                            let l_expr = self.module.alloc_expr(IrExpr::Var(left.clone()));
                            self.module
                                .alloc_expr(IrExpr::Binary(BinaryOp::Div, l_expr, r_expr))
                        }
                        ">>=" => {
                            let l_expr = self.module.alloc_expr(IrExpr::Var(left.clone()));
                            self.module
                                .alloc_expr(IrExpr::Binary(BinaryOp::Shr, l_expr, r_expr))
                        }
                        "<<=" => {
                            let l_expr = self.module.alloc_expr(IrExpr::Var(left.clone()));
                            self.module
                                .alloc_expr(IrExpr::Binary(BinaryOp::Shl, l_expr, r_expr))
                        }
                        _ => r_expr,
                    }
                } else {
                    self.module.alloc_expr(IrExpr::LiteralInt(0))
                };
                Some(self.module.alloc_stmt(IrStmt::Assign(left, right)))
            }
            "update_expression" => {
                let var_name = node
                    .child_by_field_name("argument")
                    .map(|n| self.text(n))
                    .unwrap_or_else(|| "var".to_string());
                let op = node
                    .child_by_field_name("operator")
                    .map(|n| self.text(n))
                    .unwrap_or_else(|| "++".to_string());
                let one = self.module.alloc_expr(IrExpr::LiteralInt(1));
                let var_expr = self.module.alloc_expr(IrExpr::Var(var_name.clone()));
                let b_op = if op == "++" {
                    BinaryOp::Add
                } else {
                    BinaryOp::Sub
                };
                let new_expr = self.module.alloc_expr(IrExpr::Binary(b_op, var_expr, one));
                Some(self.module.alloc_stmt(IrStmt::Assign(var_name, new_expr)))
            }
            _ => {
                let expr = self.lower_expr(node);
                Some(self.module.alloc_stmt(IrStmt::Expr(expr)))
            }
        }
    }

    pub fn lower_expr(&mut self, node: &'a AstNode) -> ExprId {
        match node.kind() {
            "number_literal" => {
                let val = self.text(node).parse::<i64>().unwrap_or(0);
                self.module.alloc_expr(IrExpr::LiteralInt(val))
            }
            "true" => self.module.alloc_expr(IrExpr::LiteralBool(true)),
            "false" => self.module.alloc_expr(IrExpr::LiteralBool(false)),
            "identifier" => {
                let name = self.text(node);
                self.module.alloc_expr(IrExpr::Var(name))
            }
            "binary_expression" => {
                let left_node = node.child_by_field_name("left");
                let right_node = node.child_by_field_name("right");
                let op_str = node
                    .child_by_field_name("operator")
                    .map(|n| self.text(n))
                    .unwrap_or_else(|| "+".to_string());

                let left = left_node
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralInt(0)));
                let right = right_node
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralInt(0)));

                let op = match op_str.as_str() {
                    "+" => BinaryOp::Add,
                    "-" => BinaryOp::Sub,
                    "*" => BinaryOp::Mul,
                    "/" => BinaryOp::Div,
                    "%" => BinaryOp::Mod,
                    "&" => BinaryOp::BitAnd,
                    "|" => BinaryOp::BitOr,
                    "^" => BinaryOp::BitXor,
                    "<<" => BinaryOp::Shl,
                    ">>" => BinaryOp::Shr,
                    "==" => BinaryOp::Eq,
                    "!=" => BinaryOp::Ne,
                    "<" => BinaryOp::Lt,
                    "<=" => BinaryOp::Le,
                    ">" => BinaryOp::Gt,
                    ">=" => BinaryOp::Ge,
                    "&&" => BinaryOp::And,
                    "||" => BinaryOp::Or,
                    _ => BinaryOp::Add,
                };

                self.module.alloc_expr(IrExpr::Binary(op, left, right))
            }
            "call_expression" => {
                let fn_name = node
                    .child_by_field_name("function")
                    .map(|n| self.text(n))
                    .unwrap_or_else(|| "call".to_string());
                let args_node = node.child_by_field_name("arguments");
                let mut args = Vec::new();
                if let Some(args_list) = args_node {
                    for child in &args_list.children {
                        if child.kind() != "(" && child.kind() != ")" && child.kind() != "," {
                            args.push(self.lower_expr(child));
                        }
                    }
                }
                self.module.alloc_expr(IrExpr::Call(fn_name, args))
            }
            "subscript_expression" => {
                let base = node
                    .child_by_field_name("argument")
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralInt(0)));
                let index = node
                    .child_by_field_name("index")
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralInt(0)));
                self.module.alloc_expr(IrExpr::Index(base, index))
            }
            "field_expression" => {
                let argument = node
                    .child_by_field_name("argument")
                    .map(|n| self.lower_expr(n))
                    .unwrap_or_else(|| self.module.alloc_expr(IrExpr::LiteralInt(0)));
                let field = node
                    .child_by_field_name("field")
                    .map(|n| self.text(n))
                    .unwrap_or_default();
                self.module
                    .alloc_expr(IrExpr::MemberAccess(argument, field))
            }
            "cast_expression" => {
                if let Some(val) = node.child_by_field_name("value") {
                    self.lower_expr(val)
                } else {
                    let text = self.text(node);
                    self.module.alloc_expr(IrExpr::Var(text))
                }
            }
            "condition_clause" | "parenthesized_expression" => {
                for child in &node.children {
                    if child.kind() != "(" && child.kind() != ")" {
                        return self.lower_expr(child);
                    }
                }
                let text = self.text(node);
                self.module.alloc_expr(IrExpr::Var(text))
            }
            _ => {
                let text = self.text(node);
                self.module.alloc_expr(IrExpr::Var(text))
            }
        }
    }
}

fn is_cpp_container(t: &str) -> bool {
    let t = t.trim();
    t.starts_with("vector")
        || t.starts_with("unordered_map")
        || t.starts_with("unordered_set")
        || t.starts_with("map")
        || t.starts_with("set")
        || t.starts_with("queue")
        || t.starts_with("deque")
        || t.starts_with("stack")
        || t.starts_with("priority_queue")
        || t.starts_with("list")
}
