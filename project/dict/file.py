word = input()

f = open('dict.txt')

for line in f:
    w = line.split(' ')[0]
    
    if w > word:
        break

    if w == word:
        print(line)
