def sort_array(source_array):

    odd_numbers = []
    odd_positions = []
    for i in range(len(source_array)):
        if source_array[i] % 2 == 1:
            odd_positions.append(i)
            odd_numbers.append(source_array[i])

    even_numbers = []
    even_positions = []
    for i in range(len(source_array)):
        if source_array[i] % 2 == 0:
            even_positions.append(i)
            even_numbers.append(source_array[i])

    sorted_odd_numbers = sorted(odd_numbers)
    new_list = [None] * len(source_array)

    odd_index = 0
    even_index = 0

    for i in range(len(source_array)):
        if odd_index < len(odd_positions) and odd_positions[odd_index] == i:
            new_list[i] = sorted_odd_numbers[odd_index]
            odd_index += 1
        else:
            new_list[i] = even_numbers[even_index]
            even_index += 1

    return new_list


if __name__ == "__main__":
    sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
