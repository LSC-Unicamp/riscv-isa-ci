import os
import sys
import argparse
from core.config_manager import open_config_file
from core.repository_manager import (
    check_and_clone_repositories,
    BASE_PROCESSORS_DIR,
)
from core.test_cores import build_and_check_cores
from litex.build.generic_toolchain import GenericToolchain
from litex_patch import _build

parser = argparse.ArgumentParser(
    prog="RISC-V ISA CI", description="CI/CD for RISC-V cores", epilog=""
)
parser.add_argument("-u", "--update", action="store_true", default=False, help="")
parser.add_argument("-b", "--build", action="store_true", default=False, help="")
parser.add_argument("-l", "--load", action="store_true", default=False, help="")
parser.add_argument("-f", "--flash", action="store_true", default=False, help="")
parser.add_argument("-t", "--teste", action="store_true", default=False, help="")
args = parser.parse_args()


def main() -> None:
    data: dict[str, any] = open_config_file()
    check_and_clone_repositories(data)

    build_and_check_cores(data, board="ecp5_45f")


# 111100
# 110
# 1000010
if __name__ == "__main__":
    if not os.path.exists(BASE_PROCESSORS_DIR):
        os.mkdir(BASE_PROCESSORS_DIR)

    GenericToolchain.build = _build

    main()
