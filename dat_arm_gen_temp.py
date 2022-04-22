from random import randint
in_file=open('samis.dat',encoding="utf8")
out_file_temp=open('base.txt','w',encoding="utf8")
alph=in_file.readline()[0:-2]
tits=list(in_file.readline().split())
lnams = list(in_file.readline().split())
for fam in lnams:
    tnum =randint(0,len(tits)-1)
    print(fam,alph[randint(0,len(alph)-1)]+'. '+alph[randint(0,len(alph)-1)]+'.',tits[tnum],randint(1950,2023),tnum*1000//2+5000,file=out_file_temp)
out_file_temp.close()
