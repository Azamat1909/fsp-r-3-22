# Только слова. Напишите функцию, которая будет принимать строку и возвращать список без слов строки без знаков препинания.
def highlist_words(str):
    punct_marks = ['!', ',', '.', '?', '-', ':', ';']
    list = []
    for x in str:
        if x not in punct_marks:
            list.append(x)
    str = ''.join(list)
    str = str.split()

    return str


if __name__ == '__main__':
    sentence = input('Enter sentence: ')
    print(highlist_words(sentence))
