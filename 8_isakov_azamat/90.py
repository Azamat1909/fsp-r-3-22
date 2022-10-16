# Двенадцать дней Рождества. Напишите программу, которая будет сама строить куплеты этой песенки. В программе должна присутствовать функция для отображения одного
# куплета. В качестве входного параметра она должна принимать порядковый номер дня, а в качестве результата возвращать готовый куплет. Далее
# в основной программе эта функция должна быть вызвана 12 раз подряд.

im_numerals = __import__('89')

songs_vers = ('Twelve drummers drumming', 'Eleven pipers piping', 'Ten lords a-leaping', 'Nine ladies dancing', 'Eight maids a-milking',
              'Seven swans a-swimming', 'Six geese a-laying', 'Five gold rings(five golden rings)', 'Four calling birds', 'Three French hens', 'Two turtledoves')


def create_vers(x):
    print(
        f'On the {im_numerals.find_numerals(day)} day of Christmas, my true love sent to me')
    if day == 1:
        print('A partridge in a pear tree.')
    else:
        for str in songs_vers[-x + 1::]:
            print(str)
        print('And a partridge in a pear tree.')


day = int(input('Enter the day: '))

create_vers(day)
