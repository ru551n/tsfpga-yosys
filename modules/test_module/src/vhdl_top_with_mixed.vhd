library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity vhdl_top_with_mixed is
    generic(
      NUM_BITS : natural
    );
    port(
        clk : in std_logic;
        d : in std_logic_vector(NUM_BITS - 1 downto 0);
        q : out std_logic_vector(NUM_BITS - 1 downto 0)
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

  signal q_int : std_logic_vector(NUM_BITS - 1 downto 0);
begin

  bits_gen : for i in NUM_BITS - 1 downto 0 generate
    begin
    verilog_module_inst : verilog_module
    port map (
      clk => clk,
      d => d(i),
      q => q_int(i)
    );

    vhdl_module : entity work.vhdl_module
    port map (
      clk => clk,
      d => q_int(i),
      q => q(i)
    );
    end generate;
    
end architecture rtl;