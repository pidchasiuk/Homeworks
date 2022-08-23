from names import get_full_name
from random import sample


def generate_names_list_with_duplicates(num):
    """
        :param num: minimum number of unique names
        :return: list with random names wit duplicates
    """
    names_list = []
    for i in range(num):
        names_list.append(get_full_name())
    random_indexes = sample(range(0, len(names_list) - 1), len(names_list) // 2 + 1)
    for i in random_indexes:
        names_list.append(names_list[i])
    return names_list


def remove_duplicates(arr):
    for i in arr:
        if arr.count(i) > 1:
            for j in range(arr.count(i) - 1):
                arr.remove(i)
    return arr


if __name__ == "__main__":
    names_arr = sorted(generate_names_list_with_duplicates(5))
    print(f'List of people: {names_arr}\n'
          f'List without duplicates {remove_duplicates(names_arr)}')
