# Third party libraries
from tsfpga.examples.example_env import get_hdl_modules
from tsfpga.module import BaseModule

from tsfpga.vivado.project import VivadoNetlistProject
from tsfpga.yosys.project import YosysNetlistBuild


class Module(BaseModule):
    def get_build_projects(self):
        projects = []

        projects.append(
            YosysNetlistBuild(
                name="test_module",
                modules=[self],
                top="vhdl_top_with_mixed",
                synth_command="synth"
            )
        )

        return projects
