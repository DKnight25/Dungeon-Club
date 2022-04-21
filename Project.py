import pickle
class Sold(): #Soldier -- Солдат
    sh_fn=None #Sh -- Сокращено (shortened)    First name -- Имя
    sh_ptnc=None #ptnc -- Отчество (Patronic), у англоговорящих нет в повседневных словах полного аналога, но есть это...
    lname=None #Last name -- Фамилия
    titl=None # Title -- Звание [A,К,Хамар,СтаршийСержант,2003,5700]
    yr=None # Year -- Год (Начания... Начинания... Вступления в службу)
    wg=None # Wage -- Оплата (Оклад)
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
    sd.wg=x[5]
    slds.append(sd)
def Exit():
    exit()
def sortfog():
    com=input()
def append():
    while True:
        com=list(input().split())
        try:
            slds.append([com[:6]])
            break
        except:
            pass
def edit():
    com=input()
    
def delete():
    while True:
        com=int(input())
        try:
            slds.pop(com)
            break
        except:
            pass
def burn():
    pass
def print_soldier():
    com=input()
    for i in range(len(slds)):
        if slds[i][2]==com:
            print(i,end=')')
            for j in range(6):
                print(slds[i][j],end=' ')
            print('')
            break
def print_all():
    for i in range(len(slds)):
        for j in range(6):
            print(slds[i][j],end=' ')
        print('')
metod={
    'exit':Exit
    'sort':sortfog
    'append':append
    'edit':edit
    'delete':delete
    'burn':burn
    'print soldier':print_soldier
    'print all':print_all
    }
while True:
    com=input()
    if com=='exit':
        break
    if com=='sort':
        com=input()
        if com=='lname':
            pass
        if com=='wage':
            pass
        if com=='year':
            pass
    if com=='burn':
        #Запись в файл под тем же или новым именем
        pass
