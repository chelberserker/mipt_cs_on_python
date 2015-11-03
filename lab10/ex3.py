input = open('input.txt', 'r')
output = open('output.txt', 'w')
s = input.read()
s = s.lower()
for i in range(len(s)):
    if (s[i]=='.')and(s[i]==',')and(s[i]=='!')and(s[i]=='?'):
        s[i] = ' '
word = ''
dictionary = dict()
for i in range(len(s)):
    if s[i] != ' ':
        word += s[i]
    else:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    word = ''
mx = 0
for keys in dictionary:
    mx = max(mx, dictionary[keys])

