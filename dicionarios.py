# Declarando um dicionário:

mystring = "Aribabiba: viva a vida com alegria e com a gentileza. \n"

word_freq = {}
for token in mystring.split():
    if token in word_freq:
        word_freq[token] += 1
    else:
        word_freq[token] = 1

print(word_freq)
