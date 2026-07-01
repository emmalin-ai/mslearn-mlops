from pathlib import Path


def test_model_requirements_match_conda_environment():
    repo_root = Path(__file__).resolve().parents[1]
    conda_text = (repo_root / "model" / "conda.yaml").read_text(encoding="utf-8")
    requirements_text = (repo_root / "model" / "requirements.txt").read_text(encoding="utf-8")

    expected_dependencies = [
        "mlflow==3.10.0",
        "cloudpickle==2.2.0",
        "psutil==5.9.4",
        "scikit-learn==1.1.1",
    ]

    for dependency in expected_dependencies:
        assert dependency in conda_text
        assert dependency in requirements_text
