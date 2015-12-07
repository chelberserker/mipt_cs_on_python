with open('en-ru.txt', 'r') as dictionary:
    with open('input.txt', 'r') as inp:
        with open('output.txt', 'w') as out:
            dict = {}
            dictline = dictionary.readline()
            while dictline != '':
                dictline = dictline.split('\t-\t')
                dictline[1] = dictline[1].split('\n')[0]
                dict[dictline[0]] = dictline[1]
                dictline = dictionary.readline()
            line = inp.readline()
            for x in dict:
                print(x, dict[x])
            while line != '':
                line = list(line)
                word = ''
                for i in range(len(line)):
                    char = line[i]
                    if ord(char) < 65 or 90 < ord(char) < 97 or ord(char) > 122:
                        word = word.lower()
                        if word in dict and dict[word] != '=':
                            word = dict[word]
                        print(word, end='', file=out)
                        print(char, end='', file=out)
                        word = ''
                    else:
                        word += char
                line = inp.readline()
