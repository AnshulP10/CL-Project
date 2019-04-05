f = open('eng_chunk.txt', 'r')
g=open('eng_ext.txt', 'r+')
final=open('eng_extr.txt', 'r+')

arr = [line for line in f.read().split('\n')]


for l in arr:
    if len(l)==0:
        with open("eng_ext.txt", "a") as newfile:
            newfile.write('\n')
    elif len(l) and l[-1]==')':
        with open("eng_ext.txt", "a") as newfile:
            newfile.write(l)

flag=0
arr1=[line for line in g.read()]
for lin in arr1:
    for c in lin:
        if c ==' ' and flag==0:
            final.write(c)
            flag=1
        elif c==" " and flag==1:
            pass
        elif c!=' ' and flag==1:
            final.write(c)
            flag=0
        else:
            final.write(c)
