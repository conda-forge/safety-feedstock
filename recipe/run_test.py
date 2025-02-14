import sys
from subprocess import call
import shutil

FAIL_UNDER = "51"
COV = ["coverage"]
RUN = ["run", "--source=safety", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    "validate_with_basic_policy_file",
    "debug_flag",
    "generate_pass",
]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    shutil.rmtree("tests/alerts")
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
