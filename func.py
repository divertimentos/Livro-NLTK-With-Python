# Código não funcionando. 
# Ele foi escrito para Python 2, 
# então certamente tem algum pedaço incompatível com o Python 3, que é o que eu uso.

'''
import sys

mystring = "Num buraco no chão vivia um hobbit! \n"


def wordfreq(mystring):
    print(mystring)
    word_freq = {}
    for token in mystring.split():
        if token in wordfreq(mystring):
            word_freq[token] += 1
        else:
            word_freq[token] = 1
    print(word_freq)


def main():
    str = "Isto é um programa escrito em Python."
    wordfreq(str)
if __name__ == "__main__":
    main()
'''