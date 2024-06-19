def int_to_roman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    roman_numeral = ""
    
    while number:
        div = number // num[i]
        number %= num[i]
  
        while div:
            roman_numeral += sym[i]
            div -= 1
        i -= 1
    
    return roman_numeral
  
if __name__ == "__main__":
    number = 1954
    print("O número convertido para romano é: ", end="")
    print(int_to_roman(number))
