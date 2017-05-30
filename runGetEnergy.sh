#!/bin/bash -login
#PBS -m be
#PBS -M jklymak@gmail.com
#PBS -l select=1:ncpus=1
#PBS -l walltime=0:20:00
#PBS -q transfer
#PBS -A ONRDC35552400
#PBS -j oe
#PBS -N GetEnergyBudget.py


cd $PBS_O_WORKDIR
echo $PBS_O_WORKDIR
pwd

echo $PRE
echo $ITER
echo $DITER
echo $U0
ITERS=$((ITER + 2*DITER))
echo $ITERS
python GetEnergyBudget.py $PRE 0.10 ${ITERS} ${DITER}

#python GetEnergyBudget.py regrid3dlow01U10 0.10 28800
# python GetEnergyBudget.py regrid3dfullNH 0.10
rsync -av *.pickle valdez.seos.uvic.ca:leewaves17/${PRE}/
