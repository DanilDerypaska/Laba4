import numpy as np
import threading

# функція, що знаходить вагу елемента матриці
def weight(element, matrix):
    row_sum = sum(matrix[element[0], :]) - matrix[element[0], element[1]]
    col_sum = sum(matrix[:, element[1]]) - matrix[element[0], element[1]]
    return row_sum + col_sum

# функція, яка знаходить елементи найбільшої ваги у матриці
def find_max_weight(matrix):
    max_weight = 0
    max_weight_elements = []

    # функція, яка обробляє окремий елемент матриці
    def process_element(element):
        nonlocal max_weight, max_weight_elements

        w = weight(element, matrix)

        if w > max_weight:
            max_weight = w
            max_weight_elements = [element]
        elif w == max_weight:
            max_weight_elements.append(element)

    # створюємо список потоків
    threads = []

    # обробляємо кожен елемент матриці у окремому потоці
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            element = (i, j)
            t = threading.Thread(target=process_element, args=(element,))
            t.start()
            threads.append(t)

    # чекаємо, доки всі потоки закінчать свою роботу
    for t in threads:
        t.join()

    return max_weight, max_weight_elements

# приклад використання
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
max_weight, max_weight_elements = find_max_weight(matrix)
print("Max weight:", max_weight)
print("Elements with max weight:", max_weight_elements)
