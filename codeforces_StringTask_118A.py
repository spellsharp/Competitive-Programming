inputString = input()
inputString = inputString.lower()

removedVowel = ''
for character in inputString:
    if character in ['a', 'e', 'i', 'o', 'u','y']:
        continue
    elif character.isalpha():
        removedVowel = removedVowel + character

temp = ''
for character in removedVowel:
    temp = temp + '.' + character

print(temp)