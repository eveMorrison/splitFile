interval = 60000
lineno = 900000
while (lineno<=1740000):
    lineno = lineno + interval
    #print("awk '{if (($7-$6) >= 250) print $0;}' nondys_"+str(lineno)+".fa.out | awk '{if($2<=20.0) print $0;}' > nondys_"+str(lineno)+"_filter.fa.out")
    #print("wc -l nondys_"+str(lineno)+"_filter.fa.out ")
    #print("perl build_dictionary.pl --rm /home/e378m007/nondysgenic/repMaskOut/nondys_"+str(lineno)+"_filter.fa.out --unknown > nondys_"+str(lineno)+"_dict.txt")
    print("wc -l nondys_"+str(lineno)+"_dict.txt")