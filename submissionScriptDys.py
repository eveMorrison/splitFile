interval = 60000
lineno=0
smallfile = None

while (lineno<=120000):
    lineno = lineno + interval
    if smallfile:
        smallfile.close()
    small_filename = 'dys_{}.sh'.format(lineno)
    smallfile = open(small_filename, "w")
    smallfile.write("#!/bin/bash\n")
    smallfile.write("#SBATCH --job-name=repmask_dys"+str(lineno)+"\n")
    smallfile.write("#SBATCH --partition=sixhour\n")
    smallfile.write("#SBATCH --mail-type=ALL\n")
    smallfile.write("#SBATCH --mail-user=e378m007@ku.edu\n")
    smallfile.write("#SBATCH --time=0-06:00:00\n")
    smallfile.write("#SBATCH --output=repmask_dys"+str(lineno)+"_%j.log\n")
    smallfile.write("#SBATCH --ntasks=1\n")
    smallfile.write("#SBATCH --cpus-per-task=16\n")
    smallfile.write("#SBATCH --mem=16gb\n")
    smallfile.write("\n")
    smallfile.write("module load repeatmasker/4.1.2\n")
    smallfile.write("\n")
    smallfile.write("echo \"running repeat masker\"\n")
    smallfile.write("\n")
    smallfile.write("RepeatMasker /home/e378m007/dysgenic/dys_" + str(lineno) + ".fa -engine ncbi -lib /home/e378m007/bestTEs.fa -no_is\n")
    
