# Function to convert decimal to binary number
def decimalToBinary(decimal):  
    return format(decimal , '08b')
word = int(input('請問你想查什麼字: '))

result = decimalToBinary(word)
print(result)