import random
# num = int(input('Input a number: '))
#
# #result = num % 2
# if not num % 2:
#     print(f'{num} is even')
# else:
#     print(f'{num} is odd')


# num = int(input('Input a number: '))
#
# if num > 10 and num < 20:
#     print('YES')
# elif num > 90:
#

# elif num > 50:
#     print('> 50')
# else:
#     print('NO')

# a = int(input('Input a number 1: '))
# b = int(input('Input a number 2: '))
# c = int(input('Input a number 3: '))
#
# if a >= b and a>= c:
#     print(f'{a} is the largest')
# elif b >= a and b >= c:
#     print(f'{b} is the largest')
# else:
#     print(f'{c} is the largest')

# a = 10
# if a > 2:
#     if a < 30:
#         if a % 5 == 0:
#             print('OK')
#
# for i in range(5):
#     print(i, end=' ')
#
# print()
# for i in range(2, 5):
#     print(i, end=' ')
#
# print()
# for i in range(4, 11, 2):
#     print(i, end='  ')
#
# for i in range(6, 16, 3):
#     print(i, end='  ')

# start_range = int(input('Start :'))
# end_range = int(input('End :'))
# step_range = int(input('Step :'))
#
# for k in range(start_range, end_range, step_range):
#     print(k, end=',')

# for i in range(101):
#     x = random.randint(0, 100)
#     print(x, end=' ')

# for j in range(1, 10):
#     print()
#     for i in range(1, 10):
#         print(f'{j}*{i}={j*i}', end=' ')

start_range = int(input('Start: '))
end_range = int(input('End: '))
for n in range(start_range, end_range + 1):
   is_prime = True

   for i in range(2, n):
       if n % i == 0:
           is_prime = False
           break

   if is_prime:
       print('%d, ' % n, end='')