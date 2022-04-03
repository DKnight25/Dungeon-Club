import pickle
class Sold(): #Soldier -- Солдат
    sh_fn=None #Sh -- Сокращено (shortened)    First name -- Имя
    sh_ptnc=None #ptnc -- Фамилия (Patronic), у англоговорящих нет в повседневных словах полного аналога, но есть это...
    lname=None #Last name -- Фамилия
    titl=None # Title -- Звание
    yr=None # Year -- Год (Начания... Начинания... Вступления в службу)
file_input = open ('base.txt','r',encoding="utf8")
slds=[] # Soldiers -- Солдаты
while True:
     x=file_input.readline()
     if not x:break
     x=x.split()
     sd=Sold()
     sd.sh_fn=x[1]
     sd.sh_ptnc=x[2]
     lname=x[0]
     sd.titl=x[3]
     sd.yr=x[4]
     slds.append(sd)
with open('base.dat','wb') as file_output:
     pickle.dump(slds,file_output)
file_output.close()
file_input.close()
