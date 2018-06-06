# import nltk
import re
# print("Python and NLTK installed succesfully.")

# lst = [1, 2, 3, 4]
# print(lst)

# print("Primeiro elemento: " + str(lst[0]))  # "Primeiro elemento: 1."
# print("Último elemento: " + str(lst[-1]))
# print("Primeiros 3 elementos: " + str(lst[0:2]))
# print("Últimos 3 elementos: " + str(lst[-3:]))

#  Strings

mystring = "Num buraco no chão vivia um hobbit! \n"

print(mystring.upper().split())
print(mystring.replace(" ", ", "))
print(mystring.replace("!", "."))

if re.search("um", mystring):
    print("Encontrei um artigo indefinido!")
else:
    print("Não encontrei nada.")

# Findall:

print(re.findall("!", mystring))
