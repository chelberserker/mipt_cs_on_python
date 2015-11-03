def createbackdict(s):
    simpledict = dict()
    enword = s[:s.index('\t')]
    russianwords = s[s.index('\t')+3:]
    for i in range(len(russianwords)):
        if (s[i]=='.')and(s[i]==',')and(s[i]=='!')and(s[i]=='?'):
            s[i] = ' '
    word = ''
    for i in range(len(russianwords)):
        if s[i] != ' ':
            word += s[i]
        else:
            simpledict[word]=enword
            word = ''
    return simpledict
    
def sortdic(A):
    #should be sorted
    return A

inp = open('input.txt', 'r')
output = open('output.txt', 'w')
dictionary = dict()
while line != '':
    line = inp.readline()
    sdic = createbackdict(line)
    dictionary.update(sdic)
    
sortdic(dictionary)   

    
    
    
        
