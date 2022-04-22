import pickle
class Sold():
    sh_fn=None
    sh_ptnc=None
    lname=None
    titl=None
    yr=None 
    wg=None 
slds_tmp=[]
with open('base.dat','rb') as file_input:
    slds_tmp=pickle.load(file_input)
    file_input.close()
slds=[[] * i for i in range (len(slds_tmp))]
for i in range (len(slds_tmp)):
    slds[i].append(slds_tmp[i].sh_fn)
    slds[i].append(slds_tmp[i].sh_ptnc)
    slds[i].append(slds_tmp[i].lname)
    slds[i].append(slds_tmp[i].titl)
    slds[i].append(slds_tmp[i].yr)
    slds[i].append(slds_tmp[i].wg)
def Exit():
    exit()
def sortfog():
    while True:
        try:
            com=int(input())
            k=0
            r=0
            p=[]
            for i in range(len(slds)):
                for j in range(k,len(slds)):
                    if slds[j][com]<slds[r][com]:
                        r=j
                p=slds[k]
                slds[k]=slds[r]
                slds[r]=p
                k+=1
                r=k
                print(slds)
            break
        except:
            print ('An exception occured in sortfog')
def append():
    while True:
        com=input()
        try:
            slds.append(*com.split())
            break
        except:
            print ('An exception occured in append')
def edit():
    com=list(map(int,input().split()))
    print (com)
    if com[1] <=1:
        slds[com[0]][com[1]]=input()[0]+'.'
    elif com[1]>=4:
        slds[com[0]][com[1]]=str(int(input()))
    else:
        slds[com[0]][com[1]]=input()
def delete():
    while True:
        com=int(input())
        try:
            slds.pop(com)
            break
        except:
            print ('An exception occured in delete')
def burn():
    with open('base.dat', 'wb') as file_output:
        pickle.dump(slds,file_output)
        file_output.close()
with open('base.dat','wb') as file_output:
    pickle.dump(slds,file_output)
    file_output.close()
def print_soldier():
    com=int(input())
    for i in range(6):
        print(slds[com][i],end=' ')
    print('')
def print_all():
    for i in range(len(slds)):
        print(i,end=') ')
        for j in range(6):
            print(slds[i][j],end=' ')
        print('')
metod={'exit':Exit,
#    'sort':sortfog,
    'append':append,
    'edit':edit,
    'delete':delete,
    'burn':burn,
    'print soldier':print_soldier,
    'print all':print_all
    }
while True:
    com=input()
    try:
        metod[com]()
    except:
        print ('An exception occured in execution')
