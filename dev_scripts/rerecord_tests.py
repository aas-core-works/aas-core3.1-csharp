"""Run all tests and re-record the golden data."""

import argparse
import os
import pathlib
import shutil
import subprocess
import sys


def main() -> int:
    """Execute the main routine."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.parse_args()

    repo_root = pathlib.Path(os.path.realpath(__file__)).parent.parent

    for path in (repo_root / "test_data").iterdir():
        if path.is_dir() and path.name not in ["Json", "Xml"]:
            print(f"Deleting {path} ...")
            shutil.rmtree(path)

    env = os.environ.copy()
    env["AAS_CORE_AAS3_1_TESTS_RECORD_MODE"] = "1"
    env["AAS_CORE_AAS3_1_TESTS_TEST_DATA_DIR"] = str(repo_root / "test_data")

    print("Running and re-recording all tests...")
    subprocess.check_call(
        ["dotnet", "test"],
        cwd=repo_root / "src",
        env=env,
    )
    print("Re-recorded.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
