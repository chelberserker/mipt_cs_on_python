def creatingdictionary(f):
    Dictionary = dict()
    while line != '':
        line = inp.readline()
        enword = s[:s.index('\t')]
        rword = s[s.index('\t')+3:]
        Dictionary[enword]=rword
    return Dictionary

def translation(s, Dict):
    translated = ''
    word = '' 
    for i in range(len(s)):
        if s[i] != ' ':
            word += s[i]
        else:
            if word in Dict:
                translated += Dict[word]
            else:
                translated += word
            word = ''
    return translated

inp = open('input.txt', 'r')
output = open('output.txt', 'w')
dictionary = creatingdictionary(inp)
while line != '':
    line = inp.readline()
    print(line)
    print(translation(line, dictionary, file=output))
