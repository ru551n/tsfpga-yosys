library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity vhdl_module is
  port(
    clk : in std_logic;
    d : in std_logic;
    q : out std_logic
  );
end entity;

architecture rtl of vhdl_module is
begin

  process(clk)
  begin
    if rising_edge(clk) then
      q <= d;
    end if;
  end process;
    
end architecture;