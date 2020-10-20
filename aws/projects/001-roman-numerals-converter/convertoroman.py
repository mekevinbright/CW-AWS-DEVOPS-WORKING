def convert(decimal_num):
    roman = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    num_to_roman = ''
    for i in roman.keys():
        num_to_roman += roman[i]*(decimal_num//i)
        decimal_num %= i
    return num_to_roman

print(convert(3999))






def convert(num):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    number_roman = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            number_roman += syb[i]
            num -= val[i]
        i += 1
    return (number_roman)


def InttoRoman(number):
    romandict = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V': 5, 'IV':4, 'I':1}
    if (not number.isdigit()) or ((int(number) > 3999) or (int(number) < 1)):
        return 0
    number = int(number)    
    result = ""
    for key, value in romandict.items():
        while number >= value:
            quotient = number // value 
            result += key * quotient
            number %= value
    return result




# gfsfgs
# fdgdg
# dafdfa
