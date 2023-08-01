x = input()

def Capitalization(word):
    if word[0].isupper():
        return word
    else:
        new_word = word[1:]
        letter = word[0]
        letter = letter.capitalize()
        last_word = letter + new_word
        return last_word

print(Capitalization(x))
