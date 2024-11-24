# Third party libraries
from tsfpga.module import BaseModule

from tsfpga.yosys.project import YosysNetlistBuild


class Module(BaseModule):
    def get_build_projects(self):
        projects = []

        projects.append(
            YosysNetlistBuild(
                name="test_module",
                top_module=self,
                modules=[],
                top="vhdl_top_with_mixed",
                synth_command="synth",
            )
        )

        return projects
