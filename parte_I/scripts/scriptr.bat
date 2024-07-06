@echo off
rem Cambia el directorio a la ubicación de tu script de Python, si es necesario
cd /d C:\Users\acval\OneDrive\Escritorio\UCR\Sem VII\EstrucComp II\baseline_cache_I2024\IE0521_Tarea4_Cache\parte_I

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 400.perlbench-41B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 401.bzip2-226B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 403.gcc-16B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 410.bwaves-1963B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 416.gamess-875B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 429.mcf-184B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 433.milc-127B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 435.gromacs-111B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 436.cactusADM-1804B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 437.leslie3d-134B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 444.namd-120B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 445.gobmk-17B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 450.soplex-247B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 453.povray-887B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 454.calculix-104B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 456.hmmer-191B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 458.sjeng-1088B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 459.GemsFDTD-1169B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 462.libquantum-1343B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 464.h264ref-30B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 465.tonto-1769B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 470.lbm-1274B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 471.omnetpp-188B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 473.astar-153B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 481.wrf-1170B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 482.sphinx3-1100B.trace.txt >> resultadosr.txt

python3 cache_sim.py -s 32 -a 8 -b 64 -r r -t 483.xalancbmk-127B.trace.txt >> resultadosr.txt
