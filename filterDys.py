interval = 60000
lineno = 120000
while (lineno<=540000):
    lineno = lineno + interval
    #print("awk '{if (($7-$6) >= 250) print $0;}' dys_"+str(lineno)+".fa.out | awk '{if($2<=20.0) print $0;}' > dys_"+str(lineno)+"_filter.fa.out")
    #print("perl build_dictionary.pl --rm /home/e378m007/dysgenic/repMaskOut/dys_" + str(lineno) + "_filter.fa.out --unknown > dys" + str(lineno) + "_dict.txt")
    print("perl one_code_to_find_them_all.pl --rm /home/e378m007/dysgenic/repMaskOut/dys_"+ str(lineno) +"_filter.fa.out --ltr /home/e378m007/dys"+ str(lineno) +"_dict.txt --strict --unknown --fasta /home/e378m007/dysgenic/dys_" + str(lineno) + ".fa --flanking 500") 
