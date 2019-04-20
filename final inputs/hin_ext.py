file = open('hin_chunk.txt', 'r')
new=open('hin_ext.txt', 'r+')
out=open('hin_extract.txt', 'r+')
arr=[line for line in file.read().split('\n')]
print(arr[0])
head='not found'
for line in arr: 
    if line=='</Sentence>':
        new.write('\n')
    else:
        lin = [word for word in line.strip().split(' ')]
        if lin[0]=='))':
            new.write(')'+head+'\n')
        elif lin[0]=='<Sentence':
            new.write('')
        elif len(lin)<=2:
            print(lin)
        elif lin[1]=='((':
            if len(lin)>3:
                head=lin[5]
            else:
                head='not found'
            new.write(lin[1]+' '+lin[2])
        else:
            new.write('('+lin[1]+' '+lin[2]+')')
