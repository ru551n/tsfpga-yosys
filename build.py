import sys

from common import (
    HDL_MODULES_MODULES_PATH,
    HDL_MODULES_PATH,
    MODULES_PATH,
    TSFPGA_PATH,
    REPO_ROOT
)

sys.path.insert(0, str(TSFPGA_PATH))
sys.path.insert(0, str(HDL_MODULES_PATH))

from tsfpga.examples.build_fpga_utils import arguments, setup_and_run
from tsfpga.build_project_list import BuildProjectList
from tsfpga.module import get_modules


def main() -> None:
    
    modules = get_modules(MODULES_PATH)
    
    args = arguments(REPO_ROOT / "tmp")
    
    projects = BuildProjectList(modules, args.project_filters, include_netlist_not_top_builds=True)
    
    setup_and_run(modules, projects, args, collect_artifacts_function=None)

if __name__ == "__main__":
    main()