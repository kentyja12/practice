import random

word = {".":"ピリオド",",":"カンマ",":":"コロン",";":"セミコロン"}

def game():
    word = {".":"ピリオド",",":"カンマ",":":"コロン",";":"セミコロン"}
    wordk = list(word.keys())
    return random.choice(wordk)

while 1:
    x = game()
    print("この記号は？",x)
    ans = input(">>>")
    if ans == "exit":
        exit()
    if word[x] == ans:
        print("Correct.")
    else:
        print("Mistake.")