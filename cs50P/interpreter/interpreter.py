'''cs50p problem set 2
    22/08/2023'''
num_1, sign, num_2 = input("Expression: ").split(' ')
num_1 = float(num_1.strip())
num_2 = float(num_2.strip())
sign = sign.strip()
if sign == '+':
    print(round((num_1 + num_2), 1))
elif sign == '-':
    print(round((num_1 - num_2), 1))
elif sign == '*':
    print(round((num_1 * num_2), 1))
else:
    print(round((num_1 / num_2), 1))
