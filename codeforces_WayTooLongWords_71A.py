n = int(input())
word_list = []
for i in range(n):
    word = input()
    length = len(word)
    if length <= 10:
        word_list.append(word)
    else:
        firstLetter = word[0]
        lastLetter = word[-1]        
        new_word = firstLetter + str(length - 2) + lastLetter
        word_list.append(new_word)

for i in word_list:
    print(i)