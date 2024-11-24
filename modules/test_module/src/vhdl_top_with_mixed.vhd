library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity vhdl_top_with_mixed is
    port(
        clk : in std_logic;
        d : in std_logic;
        q : out std_logic
    );
end entity;

architecture rtl of vhdl_top_with_mixed is
  component verilog_module is
    port(
      clk : in std_logic;
      d : in std_logic;
      q : out std_logic
    );
  end component;

  signal q_int : std_logic;
begin

  verilog_module_inst : verilog_module
  port map (
    clk => clk,
    d => d,
    q => q_int
  );

  vhdl_module : entity work.vhdl_module
  port map (
    clk => clk,
    d => q_int,
    q => q
  );
    
end architecture rtl;