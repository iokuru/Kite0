use kiteo_engine::analyze;
use serde::Deserialize;
use std::fs;
use std::path::Path;

#[derive(Debug, Deserialize)]
#[allow(dead_code)]
struct BenchmarkCase {
    id: String,
    name: String,
    language: String,
    code: String,
    expected_tc: String,
    expected_sc: String,
    expected_algorithms: Vec<String>,
}

#[test]
fn test_corpus_regression_gate_152_cases() {
    let manifest_path = "benchmark/corpus/snippets.json";
    let content = match fs::read_to_string(Path::new(manifest_path)) {
        Ok(c) => c,
        Err(_) => fs::read_to_string(Path::new("../../benchmark/corpus/snippets.json"))
            .or_else(|_| fs::read_to_string(Path::new("../benchmark/corpus/snippets.json")))
            .expect("Failed to locate benchmark/corpus/snippets.json"),
    };

    let cases: Vec<BenchmarkCase> =
        serde_json::from_str(&content).expect("Failed to deserialize benchmark cases JSON");

    assert_eq!(
        cases.len(),
        152,
        "Canonical dev corpus must contain exactly 152 cases"
    );

    let mut regressions = Vec::new();

    for case in &cases {
        let output = analyze(&case.code, &case.language);

        let tc_match = output.tc == case.expected_tc;
        let sc_match = output.sc == case.expected_sc;

        let mut expected_algos = case.expected_algorithms.clone();
        expected_algos.sort();
        let mut actual_algos = output.algorithms.clone();
        actual_algos.sort();
        let algo_match = actual_algos == expected_algos;

        if !tc_match || !sc_match || !algo_match {
            regressions.push(format!(
                "Case '{}' regressed:\n  TC: expected '{}', got '{}'\n  SC: expected '{}', got '{}'\n  Algos: expected {:?}, got {:?}",
                case.id, case.expected_tc, output.tc, case.expected_sc, output.sc, expected_algos, actual_algos
            ));
        }
    }

    if !regressions.is_empty() {
        panic!(
            "CORPUS REGRESSION GATE FAILED: {}/152 cases regressed!\n\n{}",
            regressions.len(),
            regressions.join("\n\n")
        );
    }
}
