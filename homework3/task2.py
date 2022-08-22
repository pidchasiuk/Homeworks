from names import get_full_name
from random import sample


def generate_names_list(number_of_names):
    names_list = []
    for i in range(number_of_names):
        names_list.append(get_full_name())
    return names_list


def company_taken_over(comp1, comp2):
    """
        :param comp1: bigger company that taking smaller
        :param comp2: smaller company that was taken over by bigger
        :return: set of two companies as one
    """
    return comp1.union(comp2)


def copy_random_items_from_list(arr):
    result_arr = []
    random_indexes = sample(range(0, len(arr) - 1), len(arr) // 2 + 1)
    for i in random_indexes:
        result_arr.append(arr[i])
    return result_arr


if __name__ == "__main__":
    eleks = generate_names_list(5)
    toshiba = copy_random_items_from_list(eleks) + generate_names_list(5)

    print(f'Eleks employees {eleks}\n'
          f'Toshiba employees {toshiba}\n'
          f'Eleks into Toshiba {company_taken_over(set(toshiba), set(eleks))}')
