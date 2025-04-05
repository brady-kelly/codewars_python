# Build Tower kata
def tower_builder(n_floors):
    floor_size = 1
    floor_list = []

    for floor in range(n_floors):
        floor_list.append('*' * floor_size)
        floor_size += 2

    for i in range(len(floor_list)):
        padding = ' ' * ((len(floor_list[-1]) - len(floor_list[i])) // 2)
        floor_list[i] = f"{padding}{floor_list[i]}{padding}"
    return floor_list
