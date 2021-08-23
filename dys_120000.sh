#!/bin/bash
#SBATCH --job-name=repmask_dys120000
#SBATCH --partition=sixhour
#SBATCH --mail-type=ALL
#SBATCH --mail-user=e378m007@ku.edu
#SBATCH --time=0-06:00:00
#SBATCH --output=repmask_dys120000_%j.log
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=16gb

module load repeatmasker/4.1.2

echo "running repeat masker"

RepeatMasker /home/e378m007/dysgenic/dys_120000.fa -engine ncbi -lib /home/e378m007/bestTEs.fa -no_is
