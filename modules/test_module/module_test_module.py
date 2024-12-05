# Third party libraries
from tsfpga.module import BaseModule

from tsfpga.yosys.project import YosysNetlistBuild


class Module(BaseModule):
    def get_build_projects(self):
        projects = []

        for num_bits in [10, 20, 30]:
            projects.append(
                YosysNetlistBuild(
                    name=f"test_module_{num_bits}",
                    top_module=self,
                    modules=[],
                    generics=dict(NUM_BITS=num_bits),
                    top="vhdl_top_with_mixed",
                    synth_command="synth_xilinx",
                )
            )

        return projects
