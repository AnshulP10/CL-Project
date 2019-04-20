file=open('eng_extract.txt', 'r')
out=open('eng_fin.txt', 'r+')
arr=[line for line in file.read().split('\n')]
head='can not find'
flag=0
for line in arr:
    if len(line)==0:
        head=''
    string=[word for word in line.strip().split(' ')]
    for word in string:
        if flag==1:
            head=word
            flag=0
        if string[0]=='(NP':
            if word=='(NN' or word=='(NNP' or word=='(NNS' or word=='(NNP' or word=='(NNPS' or word=='(PRP' or word=='(PRP$':
                flag=1
        elif string[0]=='(VP':
            if word=='(VB' or word=='(VBD' or word=='(VBN' or word=='(VBG' or word=='(VBP':
                flag=1
    out.write(line+head+'\n')
    head='can not find'             
