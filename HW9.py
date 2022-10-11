"""Задание 1"""
my_list = list[input('Введите 5 чисел через пробел:')]
print(my_list)


"""Задание 2"""
A = [1, 2, 3, 4, 5]
A.remove(5)
print(A)


"""Задание 3"""
A = []
A.extend(input('Введите 10 чисел:'))
N = input('Введите одно число:')
print(A.count(N))


"""Задание 4"""
A = []
N = input('Введите число:')
B = 'Введите количество чисел, равное '
C = ':'
A.extend(input(B + N + C))
A.reverse()
print(A)


"""Задание 5"""
A = [input(f'Введите число № {i}:') for i in range(1,6)]
C = [i for i in A if int(i) > 5]
print(C)

# """Задание 6"""
A = []
N = input('Введите число:')
B = 'Введите количество чисел, равное '
C = ':'
A.extend(input(B + N + C))
A.sort()
print("Наибольшее число:", A[-1])
