# Записываем файл с рецептами (Задача №1):
def write_recipes_to_file(file_name, recipes):
    with open(file_name, 'w', encoding='utf-8') as file:
        for dish, ingredients in recipes.items():
            file.write(f"{dish}\n")
            file.write(f"{len(ingredients)}\n")
            for ingredient in ingredients:
                file.write(f"{ingredient['ingredient_name']} | {ingredient['quantity']} | {ingredient['measure']}\n")

recipes = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

file_name = 'recipes.txt'
write_recipes_to_file(file_name, recipes)

# Читаем список ингридиентов из файла:
def read_recipes_from_file(file_name):
    cook_book = {}

    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            ingredients_count = int(lines[i + 1].strip())
            i += 2

            ingredients = []

            for j in range(ingredients_count):
                ingredient_info = lines[i + j].strip().split(' | ')
                ingredient_name = ingredient_info[0]
                quantity = int(ingredient_info[1])
                measure = ingredient_info[2]
                ingredient = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                ingredients.append(ingredient)

            i += ingredients_count

            cook_book[dish_name] = ingredients

    return cook_book

file_name = 'recipes.txt'
cook_book = read_recipes_from_file(file_name)

# Выводим получившийся словарь с рецептами:

for dish, ingredients in cook_book.items():
    # print(cook_book)
    print(dish)
    for ingredient in ingredients:
        print(f"{ingredient['ingredient_name']} - {ingredient['quantity']} {ingredient['measure']}")
    print()

# Задача №2:
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]

            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']


                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity
                else:

                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list

dishes = ['Запеченный картофель', 'Омлет', 'Утка по-пекински']
person_count = 99
shop_list = get_shop_list_by_dishes(dishes, person_count)

for ingredient, info in shop_list.items():
    print(f"{ingredient}: {info['quantity']} {info['measure']}")


