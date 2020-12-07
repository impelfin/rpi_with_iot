import calc_func

a = int(input('Input First Number : '))
b = int(input('Input Second Number : '))

print('{} + {} = {} '.format(a, b, calc_func.add(a, b)))
print('{} - {} = {} '.format(a, b, calc_func.sub(a, b)))