def pattern(str,len):
    for i in range(0,len):
        j=len-1-i
        for k in range(0,len):
            if(k==i or k==j):
                print(str[k],end='')
            else:
                print(end =" ")
        print(" ")
str ="SireeshNaresh"
len=len(str)
pattern(str,len);
