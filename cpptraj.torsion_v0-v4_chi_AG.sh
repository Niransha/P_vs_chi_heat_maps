#!/bin/bash
#SBATCH --job-name=cpprmsd
#SBATCH -N 1
#SBATCH -n 20 
##SBATCH --gres=gpu:1
#SBATCH --partition=shortq7,mediumq7,longq7,shortq7-gpu,longq7-rna
##SBATCH --partition=longq7-rna
##SBATCH --mail-type=ALL
#SBATCH --time=6:00:00
##SBATCH --exclusive
##SBATCH --nodelist=nodegpu025


###################################
#load amber 18 on atlas
###################################
source /opt/ohpc/pub/apps/rnachem/amber18_gpu/amber.sh
source /opt/ohpc/pub/apps/rnachem/amber18_gpu/modules2load.txt


find $SLURM_SUBMIT_DIR -maxdepth 1 -type f \( -name "slurm-*" ! -name "slurm-$SLURM_JOB_ID.out" \) -delete

cat>input<<EOF
parm ./strip.prmtop.new
trajin ./combined_md.mdcrd 1 last 1

#multidihedral MyTorsions alpha beta gamma delta epsilon zeta resrange 4-5 out MyTorsions.dat range360

multidihedral dihtype mychi:O4':C1':N9:C4 out custom.dat
multidihedral dihtype v0:C1':C2':C3':C4' out custom.dat 
multidihedral dihtype v1:C2':C3':C4':O4' out custom.dat 
multidihedral dihtype v2:C3':C4':O4':C1' out custom.dat 
multidihedral dihtype v3:C4':O4':C1':C2' out custom.dat 
multidihedral dihtype v4:O4':C1':C2':C3' out custom.dat 

multidihedral dihtype mychi_:O4':C1':N9:C4 out custom360.dat
multidihedral dihtype v0_:C1':C2':C3':C4' out custom360.dat 
multidihedral dihtype v1_:C2':C3':C4':O4' out custom360.dat 
multidihedral dihtype v2_:C3':C4':O4':C1' out custom360.dat 
multidihedral dihtype v3_:C4':O4':C1':C2' out custom360.dat 
multidihedral dihtype v4_:O4':C1':C2':C3' out custom360.dat 

run
EOF

#cpptraj -i input

mpirun cpptraj.MPI -i input

