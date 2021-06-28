import os,sys

# Function to convert decimal to binary number
def decimalToBinary(decimal):  
    return format(decimal , '08b')
decimal1 = int(input('Please insert A: '))
decimal2 = int(input('Please insert B: '))
decimal3 = int(input('Please insert C: '))

A = decimalToBinary(decimal1)
B = decimalToBinary(decimal2)
C = decimalToBinary(decimal3)
print('A binary is:', A)
print('B binary is:', B)
print('C binary is:', C)

binary_num = list(A + B + C)
value = 0

for i in range(len(binary_num)):
	decimal = binary_num.pop()
	if decimal == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)


Binary to Decimal
# b_num = list(input("Input a binary number: "))
# value = 0

# for i in range(len(b_num)):
# 	digit = b_num.pop()
# 	if digit == '1':
# 		value = value + pow(2, i)
# print("The decimal value of the number is", value)



# def bin2dec(string_num):
# 	return str(int(string_num, 2))

# dec = int(input("輸入數字："))
# print("十進位制數為：", dec)
# print("轉換為二進位制為：", bin(dec))
# print("轉換為十進位制為：", int(dec))
# print("轉換為八進位制為：", oct(dec))
# print("轉換為十六進位制為：", hex(dec))


# # Function to convert binary to decimal number 
# def binaryToDecimal(binary): 
#     return int(binary, 2)
# result = int(00001010)
# print(result)



# def add(x, y):
# 	return x + y	# return 回傳結果
# result = add(3, 4)	# 把回傳結果加進去result 裡。
# print(result)