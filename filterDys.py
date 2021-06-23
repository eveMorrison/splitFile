interval = 60000
lineno = 0
while (lineno<=5670924):
    lineno = lineno + interval
    print("awk ‘{if (($7-$6) >= 250) print $0;}’ nondys_"+str(lineno)+".fa.out | awk ‘{if($2<=20.0) print $0;}’ > nondys_"+str(lineno)+"_filter.fa.out")