

def selection_sort(values):
    sorted_list = []
    for i in range(0, len(values)):
        print('first')
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
    return sorted_list


def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        print('second')
        if values[i] < values[min_index]:
            min_index = i
    return min_index


print(selection_sort([5, -1, 5, 6, 2, 6]))
