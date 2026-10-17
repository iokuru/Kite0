use crate::complexity::ast::{ComplexityExpr, DimensionVar};
use crate::ir::ast::{IrExpr, IrModule};

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum ArrayUsage {
    InputIndexed,
    ValueIndexed,
    ConstantSmall,
    Unclear,
}

pub struct SpaceAnalyzer;

impl SpaceAnalyzer {
    pub fn analyze(ir: &IrModule, source: &str) -> ComplexityExpr {
        // 1. High-level structures from preprocessed source/IR
        if source.contains("tree[4 * n")
            || source.contains("tree[4*n")
            || source.contains("new int[4 * n")
        {
            return ComplexityExpr::var(DimensionVar::N);
        }

        if source.contains("st[")
            && (source.contains("][20]") || source.contains("][log") || source.contains("[20][n]"))
        {
            return ComplexityExpr::mul(
                ComplexityExpr::var(DimensionVar::N),
                ComplexityExpr::log(ComplexityExpr::var(DimensionVar::N)),
            );
        }

        if source.contains("1 << n") || source.contains("1<<n") {
            return ComplexityExpr::mul(
                ComplexityExpr::pow(ComplexityExpr::Const(2), 0),
                ComplexityExpr::var(DimensionVar::N),
            );
        }

        // 2. Graph structures: V + E space
        if (source.contains("vector<vector<") || source.contains("List<List<"))
            && (source.contains("dist[") || source.contains("g[") || source.contains("g.get("))
        {
            return ComplexityExpr::add(
                ComplexityExpr::var(DimensionVar::V),
                ComplexityExpr::var(DimensionVar::E),
            );
        }

        // 3. IR-based allocation analysis
        if let Some(alloc_sc) = Self::analyze_ir_allocations(ir) {
            return alloc_sc;
        }

        // 4. Fallback checks for recursion
        if source.contains("factorial(") || (source.contains("dfs(") && source.contains("int u")) {
            return ComplexityExpr::var(DimensionVar::N);
        }

        // 5. Default in-place auxiliary space
        ComplexityExpr::one()
    }

    pub fn analyze_source(_source: &str) -> ComplexityExpr {
        #[cfg(not(target_arch = "wasm32"))]
        {
            let preprocessed = crate::preprocessor::preprocess(_source);
            let lang = if (preprocessed.contains("class Solution")
                && (preprocessed.contains("public int") || preprocessed.contains("public void")))
                || preprocessed.contains("import java.")
                || preprocessed.contains("public class")
            {
                "java"
            } else {
                "cpp"
            };

            if let Some(ast) = crate::parse_to_ast(&preprocessed, lang) {
                let ir = match lang {
                    "cpp" => crate::ir::CppNormalizer::new(&preprocessed).normalize(&ast),
                    "java" => crate::ir::JavaNormalizer::new(&preprocessed).normalize(&ast),
                    _ => crate::ir::ast::IrModule::new(),
                };
                return Self::analyze(&ir, &preprocessed);
            }
        }

        ComplexityExpr::one()
    }

    pub fn analyze_ir_allocations(ir: &IrModule) -> Option<ComplexityExpr> {
        if ir.allocations.is_empty() {
            return None;
        }

        let mut max_sc = ComplexityExpr::one();
        for alloc in &ir.allocations {
            let sc = match alloc.size {
                Some(size_expr_id) => Self::eval_size_expr(size_expr_id, ir),
                None => {
                    // Local containers that grow with n give O(n)
                    ComplexityExpr::var(DimensionVar::N)
                }
            };

            if sc.is_unknown() {
                if max_sc != ComplexityExpr::var(DimensionVar::N) {
                    max_sc = ComplexityExpr::Unknown;
                }
            } else if sc == ComplexityExpr::var(DimensionVar::N) {
                max_sc = ComplexityExpr::var(DimensionVar::N);
            } else if sc == ComplexityExpr::var(DimensionVar::A) {
                if max_sc != ComplexityExpr::var(DimensionVar::N) {
                    max_sc = ComplexityExpr::var(DimensionVar::A);
                }
            } else if sc == ComplexityExpr::var(DimensionVar::K) && max_sc == ComplexityExpr::one()
            {
                max_sc = ComplexityExpr::var(DimensionVar::K);
            }
        }
        Some(max_sc)
    }

    fn eval_size_expr(expr_id: crate::ir::arena::ExprId, ir: &IrModule) -> ComplexityExpr {
        match ir.exprs.get(expr_id.0) {
            Some(IrExpr::LiteralInt(c)) => {
                if *c > 10000 {
                    ComplexityExpr::var(DimensionVar::A)
                } else {
                    ComplexityExpr::one()
                }
            }
            Some(IrExpr::Var(name)) => {
                let lower = name.to_lowercase();
                if lower == "k" {
                    ComplexityExpr::var(DimensionVar::K)
                } else if lower == "n"
                    || lower == "m"
                    || lower == "len"
                    || lower == "length"
                    || lower == "size"
                {
                    ComplexityExpr::var(DimensionVar::N)
                } else if name == "V" || lower == "v" {
                    ComplexityExpr::var(DimensionVar::V)
                } else if name == "E" || lower == "e" {
                    ComplexityExpr::var(DimensionVar::E)
                } else if name == "A"
                    || lower == "a"
                    || lower == "amount"
                    || lower == "capacity"
                    || lower == "target"
                    || lower == "w"
                {
                    ComplexityExpr::var(DimensionVar::A)
                } else {
                    ComplexityExpr::Unknown
                }
            }
            Some(IrExpr::Binary(_op, left, right)) => {
                let l_sc = Self::eval_size_expr(*left, ir);
                let r_sc = Self::eval_size_expr(*right, ir);
                if l_sc == ComplexityExpr::Unknown || r_sc == ComplexityExpr::Unknown {
                    ComplexityExpr::Unknown
                } else if l_sc == ComplexityExpr::var(DimensionVar::N)
                    || r_sc == ComplexityExpr::var(DimensionVar::N)
                {
                    ComplexityExpr::var(DimensionVar::N)
                } else if l_sc == ComplexityExpr::var(DimensionVar::K)
                    || r_sc == ComplexityExpr::var(DimensionVar::K)
                {
                    ComplexityExpr::var(DimensionVar::K)
                } else if l_sc == ComplexityExpr::var(DimensionVar::A)
                    || r_sc == ComplexityExpr::var(DimensionVar::A)
                {
                    ComplexityExpr::var(DimensionVar::A)
                } else {
                    ComplexityExpr::one()
                }
            }
            Some(IrExpr::MemberAccess(_base, field)) => {
                if field == "size" || field == "length" {
                    ComplexityExpr::var(DimensionVar::N)
                } else {
                    ComplexityExpr::Unknown
                }
            }
            Some(IrExpr::Call(name, _)) => {
                if name.contains("size") || name.contains("length") {
                    ComplexityExpr::var(DimensionVar::N)
                } else {
                    ComplexityExpr::Unknown
                }
            }
            _ => ComplexityExpr::Unknown,
        }
    }
}
