from random import randint
in_file=open('samis.dat',encoding="utf8")
out_file_temp=open('base.txt','w',encoding="utf8")
alph=in_file.readline()[0:-2]
tits=list(in_file.readline().split())
for fam in list(in_file.readline().split()):
    print(fam,alph[randint(0,len(alph)-1)]+'. '+alph[randint(0,len(alph)-1)]+'.',tits[randint(0,len(tits)-1)],randint(1950,2023),file=out_file_temp)
out_file_temp.close()
