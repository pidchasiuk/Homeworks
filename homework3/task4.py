from names import get_full_name


def generate_names_list(number_of_names):
    names_list = []
    for i in range(number_of_names):
        names_list.append(get_full_name())
    return names_list


def check_vegetables_eat(omnivores: set, vegetarians: set):
    return omnivores.union(vegetarians)


if __name__ == "__main__":
    omnivores_list = set(generate_names_list(4))
    vegetarians_list = set(generate_names_list(2))
    print(f'Omnivores list: {omnivores_list}\n'
          f'Vegetarians list: {vegetarians_list}\n'
          f'Guests who can eat vegetables and herbs: \n{check_vegetables_eat(omnivores_list, vegetarians_list)}')
