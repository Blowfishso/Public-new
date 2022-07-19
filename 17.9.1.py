array = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
element = int(input('Введите число: '))
array.append(element)

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x


def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


if element == array[0]:
    print('Введенное число минимально и равно 0')
elif element == array[-1]:
    print(f'Введенное число максимально и равно {element}')
else:
    print(f'Номер позиции числа, которое меньше введенного: {binary_search(array, element, 0, len(array))}')

