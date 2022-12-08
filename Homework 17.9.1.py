sequence = input("Введите числа через пробел: ")
array = [int(a) for a in sequence.split()]

number = int(input("Введите число: "))
if number % 1 == 0:
    array.append(number)

def sorting (array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]
    return array

print ("Отсортированный список: ", sorting (array))

def binary_search(array, number, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] == number:
        return middle
    elif number < array[middle]:
        return binary_search(array, number, left, middle - 1)
    else:
        return binary_search(array, number, middle + 1, right)

print("Позиция элемента, который меньше введенного числа: ", binary_search(array, number, 0, len(array) -1))
