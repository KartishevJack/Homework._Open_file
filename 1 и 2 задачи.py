from pprint import pprint
cook_book = {}

def add_recipe(file):
    str_1 = file.readline().strip()
    str_2 = file.readline().strip()
    if str_2 == "":
        return None
    else:
        list_ingredients = []
        for ingredient in range(int(str_2)):
            dict_ingredients = {}
            str_3 = file.readline().strip() # Яйцо | 2 | шт
            list_3 = str_3.split(" | ") # ['Яйцо', '2', 'шт'] <class 'list'>
            dict_ingredients['ingredient_name'] = list_3[0]
            dict_ingredients['quantity'] = list_3[1]
            dict_ingredients['measure'] = list_3[2]
            list_ingredients.append(dict_ingredients)
        cook_book[str_1] = list_ingredients
        str_4 = file.readline()
        return cook_book

with open('Readme.md', encoding='utf-8') as f:
    while not (add_recipe(f) is None):
        add_recipe(f)

pprint(cook_book)

dict_ingredients = {}

def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        list_ing = cook_book[dish] # Список словарей
        for ing in list_ing: # {'ingredient_name': 'Яйцо',
                             #  'measure': 'шт', 'quantity': '2'}
            if ing['ingredient_name'] not in  dict_ingredients: # 'Яйцо'
                dict_ingredients[ing['ingredient_name']] = \
                    {'measure': ing['measure'],
                     'quantity': str(int(ing['quantity'])*person_count)}
            else:
                dict_ingredients[ing['ingredient_name']]['quantity'] = (
                    str(person_count * int(ing['quantity']) +
                        int(dict_ingredients[ing['ingredient_name']]['quantity'])))

dishes = ["Омлет", "Фахитос"]
get_shop_list_by_dishes(dishes, 2)

print("")
pprint(dict_ingredients)