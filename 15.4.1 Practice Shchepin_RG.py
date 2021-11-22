def simpletext (text):
    for i in '!"\@#%^$&*()_+,./:;<>=`~{}[]|?':
        i.replace(i, "")
    return text.split()

def most_common(text, long=0):
    most_comWord = []
    maxcount = 0
    for word in text:
        if len(word) > long:
            count_w = text.count(word)
            if count_w > maxcount and count_w > 2:
                maxcount = count_w
                most_comWord = [word]
            elif count_w == maxcount:
                most_comWord.append(word)
    return list(set(most_comWord))

def mostLongEn (text):
    most_long_words = []
    long_of_word = 0
    abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in text:
        for b in i:
            if b not in abc:
                bEN = False
            else:
                bEN = True
        if bEN:
            long = len(i)
            if long > long_of_word:
                long_of_word = long
                most_long_words = [i]
            elif long == long_of_word:
                most_long_words.append(i)
    return list(set(most_long_words))

a = input("Введите название файла в формате Имя_файла.txt")

with open(a, 'rt', encoding='utf8') as yourfile:
    filetext = yourfile.read()

filetext = simpletext(filetext)

print("Наиболее часто встречающееся слово:", most_common(filetext, 3))
print("Наиболее длинное английское слово", mostLongEn(filetext))



