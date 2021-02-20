# 2 задание
print("")
print("Счётчик слов в файле:")
import string

words = {}
with open("task2data.txt", 'r') as file:
    for line in file:
        for word in line.split(" "):
            exclude = set(string.punctuation)
            cleaned_word = "".join(ch for ch in word if ch not in exclude)
            if cleaned_word not in words:
                words[cleaned_word] = 0
            words[cleaned_word] += 1

print(words)
