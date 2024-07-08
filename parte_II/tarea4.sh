#!/bin/bash

# L2:
C_L2=("64" "128")
A_L2=("8" "16")
# L3:
C_L3=("512" "1024")
A_L3=("16" "32")

traces=("400.perlbench-41B.trace.txt" "429.mcf-184B.trace.txt" "444.namd-120B.trace.txt" "456.hmmer-191B.trace.txt" "465.tonto-1769B.trace.txt" "482.sphinx3-1100B.trace.txt" "401.bzip2-226B.trace.txt" "433.milc-127B.trace.txt" "445.gobmk-17B.trace.txt" "458.sjeng-1088B.trace.txt" "470.lbm-1274B.trace.txt" "483.xalancbmk-127B.trace.txt" "403.gcc-16B.trace.txt" "435.gromacs-111B.trace.txt" "450.soplex-247B.trace.txt" "459.GemsFDTD-1169B.trace.txt" "471.omnetpp-188B.trace.txt" "410.bwaves-1963B.trace.txt" "436.cactusADM-1804B.trace.txt" "453.povray-887B.trace.txt" "462.libquantum-1343B.trace.txt" "473.astar-153B.trace.txt" "416.gamess-875B.trace.txt" "437.leslie3d-134B.trace.txt" "454.calculix-104B.trace.txt" "464.h264ref-30B.trace.txt" "481.wrf-1170B.trace.txt")

#L1
for trace in "${traces[@]}"
do
        
    echo "  Running L1 C=32 A=8 with trace $trace \n"	>> txt/L1/L1.txt

    python3 cache_sim.py -b 64 --l1_s 32 --l1_a 8 -t ${trace}	>> txt/L1/L1.txt

    echo "  Finished running L2 C=32 A=8 with trace $trace \n" >> txt/L1/L1.txt

done

# L2
for cap in "${C_L2[@]}"
do	
	for ways in "${A_L2[@]}"
	do
		for trace in "${traces[@]}"
		do
			echo "  Running L2 C=$cap A=$ways with trace $trace \n"	>> txt/L2/C${cap}_A${ways}.txt

			python3 cache_sim.py -b 64 --l1_s 32 --l1_a 8 --l2 --l2_s ${cap} --l2_a ${ways} -t ${trace}	>> txt/L2/C${cap}_A${ways}.txt

			echo "  Finished running L2 C=$cap A=$ways with trace $trace \n" >> txt/L2/C${cap}_A${ways}.txt

done done done

#L3
for cap in "${C_L3[@]}"
do	
	for ways in "${A_L3[@]}"
	do
		for trace in "${traces[@]}"
		do
			echo "  Running L2 C=$cap A=$ways with trace $trace \n"	>> txt/L3/C${cap}_A${ways}.txt

			python3 cache_sim.py -b 64 --l1_s 32 --l1_a 8 --l2 --l2_s 256 --l2_a 8 --l3 --l3_s ${cap} --l3_a ${ways} -t ${trace}	>> txt/L3/C${cap}_A${ways}.txt

			echo "  Finished running L2 C=$cap A=$ways with trace $trace \n" >> txt/L3/C${cap}_A${ways}.txt

done done done