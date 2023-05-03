
single_two_digit = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'fifth',
                    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
                    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sexteen',
                    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
ten_digit = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
             70: 'seventy', 80: 'eighty', 90: 'ninety'}


def num_to_word(num):
    if 0 <= num < 1000:
        if num < 20:
            print(single_two_digit[num])
        elif num % 100 > 0:
            if 19 < num < 100 and num % 10 > 0:
                print(ten_digit[num // 10 * 10], single_two_digit[num % 10])
            elif num < 100 and num % 10 == 0:
                print(ten_digit[num])
            elif num % 100 < 20:
                print(single_two_digit[num // 100], 'hundred',
                      single_two_digit[num % 100])
            elif num % 100 % 10 > 0:
                print(single_two_digit[num // 100], 'hundred',
                      ten_digit[num % 100 // 10 * 10], single_two_digit[num % 100 % 10])
            elif num % 100 % 10 == 0:
                print(single_two_digit[num // 100],
                      'hundred', ten_digit[num % 100 // 10 * 10])
        else:
            print(single_two_digit[num // 100], 'hundred')


num = int(input('Enter num (0-1000): '))
num_to_word(num)
