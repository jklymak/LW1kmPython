#!/bin/bash -login
#PBS -m be
#PBS -M jklymak@gmail.com
#PBS -l select=1:ncpus=1
#PBS -l walltime=00:30:00
#PBS -q transfer
#PBS -A ONRDC35552400
#PBS -j oe
#PBS -N GetSlice

# run w/ qsub -v PRE="LWRegrid2low01U02",ITER=72000 runGetSlice.sh

cd $PBS_O_WORKDIR
echo $PBS_O_WORKDIR
pwd
echo $PRE
python getSliceNc.py $PRE $ITER
#python GetEnergyBudget.py regrid3dlow01U10 0.10 28800
# python GetEnergyBudget.py regrid3dfullNH 0.10
rsync -av ../results/${PRE}/_Model/input/slices/*.nc valdez.seos.uvic.ca:leewaves17/LW4km20m/slices/
