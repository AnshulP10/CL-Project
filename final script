import random
x=random.randrange(0, 22925, 1)

inp1=open('eng_fin.txt', 'r')
inp2=open('hin_fin.txt', 'r')
giza1=open('eng-hin.txt', 'r')
giza2=open('hin-eng.txt', 'r')
file=open('check.txt', 'r+')
ans=open('out.txt', 'r+')

#open text files
findEH=[l1 for l1 in giza1.read().split('\n')]
findHE=[l2 for l2 in giza2.read().split('\n')]
text1=inp1.read().split('\n\n')
text2=inp2.read().split('\n\n')

#initialise variables
flag1=0
flag2=0
prob=0
lent=0

#initializing sent arrays
sent1=[chunk1 for chunk1 in text1[x].split('\n')]
sent2=[chunk2 for chunk2 in text2[x].split('\n')]

#switching each chunk
for chunk1 in sent1:
    flag1=0
    flag2=0
    flag=0
    lent=lent+1

    if chunk1[2]=='N' or chunk1[2]=='V':
        prob=0
        head1=chunk1.split('))')[1]
        for chunk2 in sent2:
            if (chunk2[3]=='N' and chunk1[2]=='N') or (chunk2[3]=='V' and chunk1[2]=='V'):
                head2=chunk2.split('))')[1]
                for l1 in findEH:
                    word=l1.split(' ')
                    if word[0]==head1 and word[1]==head2:
                        flag1=1
                for l2 in findHE:
                    word=l2.split(' ')
                    if word[1]==head1 and word[0]==head2:
                        flag2=1
                if flag1==1 and flag2==1 and flag==0:
                    switch=chunk2
                    flag=1    
    if flag1==1 and flag2==1:
        for i in range(0, lent-1): 
            file.write(sent1[i]+'\n')
        file.write(switch+'\n')
        for i in range(lent, len(sent1)):
            file.write(sent1[i]+'\n')
        file.write('\n')
file=open('check.txt', 'r+')
arr=[sent for sent in file.read().split('\n\n')]
for sent in arr:
    text=[line for line in sent.strip().split('\n')]
    for line in text:
        lin=[word for word in line.strip().split(' ')]
        if len(lin)>0:
            if lin[0]=="((":
                for word in lin:
                    if word!='((':
                        word=word.split('(')
                        if (len(word)>1):
                            word=word[1]
                            ans.write(word+' ')
                        a=1
            else:
                for i in range(len(lin)):
                    if i!=0:
                        temp=lin[i].split(' ')
                        if (i%2==0):
                            eng=temp[0].split(')')[0];
                            ans.write(eng+' ')
    ans.write('\n')
