# -*- coding: utf-8 -*-
import nltk # библиотека NLTK (nltk.org)

f = open("spanish.txt", "r", encoding="utf-8") # установка кодировки для правильного отображения символов испанского языка в консоли
if f.mode == 'r':
    text = f.read() # загрузка данных в режиме "только чтение" из текстового файла
print("Исходный текст:", text)
answer = input("Хотите разделить текст на предложения? (Y/N): ")
if answer == "Y" or answer == "y":
    sentences = nltk.sent_tokenize(text) # использование функции sent_tokenize из библиотеки NLTK
    print("Текст разделен на предложения:", sentences)
    input() # пустой ввод, чтобы консоль не закрывалась после выполнения программы
elif answer == "N" or answer == "n":
    print("Хорошо. Программа завершает работу.")
    exit()