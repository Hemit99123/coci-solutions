word = input()
new_word = ""

for letter in word:
    if not letter in "CAMBRIDGE":
        new_word += letter

print(new_word)