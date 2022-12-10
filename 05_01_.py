# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# as asas asas asas абв йуйу абвгд assa

text = input("Введите текст: ")
lst = text.split(" ")

for word in lst:
    if (word.find("абв")== -1):
        print(word)
    else:
        continue
