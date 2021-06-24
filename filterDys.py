interval = 60000
lineno = 3600000
while (lineno<=4740000):
    lineno = lineno + interval
    print("awk '{if (($7-$6) >= 250) print $0;}' dys_"+str(lineno)+".fa.out | awk '{if($2<=20.0) print $0;}' > dys_"+str(lineno)+"_filter.fa.out")