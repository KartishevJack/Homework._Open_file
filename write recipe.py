def write_recipe():
    list_dishes = []
    str_1 = input("Введите название блюда: ")
    str_2 = input("Введите количество ингредиентов в блюде: ")
    list_dishes += [str_1, str_2]
    for ingredient in range(int(str_2)):
        str_3_1 = input("Введите название ингридиента: ")
        str_3_2 = input("Введите количество: ")
        str_3_3 = input("Введите единицу измерения: ")
        str_3 = f'{str_3_1} | {str_3_2} | {str_3_3}'
        list_dishes.append(str_3)
    return "\n".join(list_dishes)

with open('Readme.md', 'a', encoding='utf-8') as f:
    f.write(write_recipe() + "\n\n")