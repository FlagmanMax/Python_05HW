# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaaaaaaaabbbbbcccdddeeef
def encode(s):
    string = ""
    i = 0
    while i<len(s):
        cnt = 1
        while i+1<len(s) and s[i] == s[i+1]:
            cnt += 1
            i += 1
        string += str(cnt) + s[i]
        i += 1
    return string

def decode(s):
    string = "" 
    i = 0
    while i<len(s):   
        start = i
        while i+1<len(s) and 48<=ord(s[i+1])<=57:
            i += 1
        stop = i+1 
        cnt = int(s[start:stop:1])
        for j in range(cnt):
            string += s[i+1]    
        i = i + 2
    return string

text_input = open("./05_HomeWork/05_04_01.txt","r")
text =  text_input.read()
text_input.close()
print(f"Исходный текст\t\t{text}")
# text = input("Введите текст:\t\t")

text = encode(text)
print(f"Закодированный текст: \t{text}")
text_output = open("./05_HomeWork/05_04_02.txt","w")
text_output.write(text)
text_output.close()

text = decode(text)
print(f"Раскодированный текст: \t{text}")
