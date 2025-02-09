--G12, computer science and engineering, computer technology G88*
--József Iván Gafo
--Marcos González
--3/10/2022
LIBRARY ieee;
USE ieee.std_logic_1164.all;
Entity P2_2 is
	port(
        --inputs of both players
		r1,p1,t1 : In std_logic;
		r2,p2,t2 : In std_logic;
        --output
		g1,g2: out std_logic
		);
end P2_2;
architecture game of P2_2 is
-- signals, wires s1 and s2, that goes from the first encoders to the results logic block
signal s1:std_logic_vector(1 downto 0);
signal s2:std_logic_vector(1 downto 0);

begin
    --Encoder of player1 (for the game)
	process(p1,r1,t1)
		begin
                if p1 = '1' and r1 = '0' and t1 = '0' then
                    s1<="01";
                elsif p1 = '0' and r1 = '1' and t1 = '0' then
                    s1<="10";
                elsif p1 = '0' and r1 = '0' and t1 = '1' then
                    s1<="11";
                else
                    s1 <="00";
                end if;
	end process;
	--Encoder of player 2 (for the game)
	process(p2,r2,t2)
		begin
				if p2 = '1' and r2 = '0' and t2 = '0' then
					s2<="01";
				elsif p2 = '0' and r2 = '1' and t2 = '0' then
					s2<="10";
				elsif p2 = '0' and r2 = '0' and t2 = '1' then
					s2<="11";
				else
					s2 <="00";
				end if;
        
		end process;
    --Here we implement the logic of the game
    process(s1,s2)
        begin
                --both players don't play
                if s1="00" and s2="00" then
                    g1<='0';
                    g2<='0';
                --p1 don't play, wins p2
                elsif s1="00" then
                    g1<='0';
                    g2<='1';
                --p2 don't play, wins p1
                elsif s2="00" then
                    g1<='1';
                    g2<='0';
                --draw
                elsif s1=s2 then 
                    g1<='1';
                    g2<='1';
                -- Here, we take all the cases in which player 1 wins, if none of them occur, then s2 would win.

                --paper (01) wins rock(10)
                elsif s1="01" and s2="10" then 
                    g1<='1';
                    g2<='0';
                -- rock (01) wins scissors (11)
                elsif s1="10" and s2="11" then 
                    g1<='1';
                    g2<='0';
                -- scissors (11) wins paper (01)
                elsif s1="11" and s2="01" then
                    g1<='1';
                    g2<='0';
                --when p2 wins
                else 
                    g1<='0';
                    g2<='1' ;  
                end if;
        end process;
end game;