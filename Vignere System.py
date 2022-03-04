#!/usr/bin/env python3
###############################################
# Name: vignere system.py
# Author: Yuanheng Gan
#
# Description: decrypts input file using vignere
# cipher with key passed as input and passes user the decrypted message
###############################################

crypt = []
crypt = input("input the encrypted text seperated with space:").split()
key = input("input the key word:")#for key: A=0, B=1,...

letter_number_dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,
                    'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}

def letter_to_number(letters,numbers):#把letters导出为一个numbers的list
    for letter in letters:
        letter = letter.upper()
        numbers.append(letter_number_dic[letter])

def key_letter_to_number(letters,numbers):
    for letter  in letters:
        letter = letter.upper()
        numbers.append(letter_number_dic[letter]-1)

def get_letter(val):
    for key, value in letter_number_dic.items():
         if val == value:
             return key
 
    return "key doesn't exist"

def number_to_letter(numbers,letters):#把numbers list导出为letters list
    for number in numbers:
        letters.append(get_letter(number))

def vingnere_decode(crypt_input, key_input):
    crypt_number = []
    for i in crypt_input:
        letter_number = []
        letter_to_number(i,letter_number)
        crypt_number.append(letter_number)
    #key letter convert to a number list
    key_number = []
    key_letter_to_number(key_input,key_number)
    #decryption
    for index_1 in range(len(crypt_number)):
        for index_2 in range(len(crypt_number[index_1])):
            crypt_number[index_1][index_2] = (crypt_number[index_1][index_2]-key_number[index_2 % len(key_number)]) % 26
    #convert excrypted number to text
    crypt_message = []
    for index_1 in range(len(crypt_number)):
        decrypted_words = []
        number_to_letter(crypt_number[index_1],decrypted_words)
        crypt_message.append("".join(decrypted_words))
    print(" ".join(crypt_message))


vingnere_decode(crypt,key)





    