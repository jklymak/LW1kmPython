#!/bin/bash -login
#PBS -m be
#PBS -M jklymak@gmail.com
#PBS -l select=1:ncpus=1
#PBS -l walltime=0:55:30
#PBS -q transfer
#PBS -A ONRDC35552400
#PBS -j oe
#PBS -N mdstonetcdf

# qsub -v PRE=LW1km20h runmdstonetcdf.sh

cd $PBS_O_WORKDIR
echo $PATH
which python
free -tg
for ITER in 720000 721800 723600
do
    echo $ITER
    python mdstonetcdf.py $PRE $ITER
#    python mdstonetcdfW.py $PRE $ITER
#    python mdscombine.py $PRE $ITER
done
#rsync -av ../results/$PRE/_Model/input/*.nc valdez.seos.uvic.ca:leewaves15/LWCoarse4/$PRE/
