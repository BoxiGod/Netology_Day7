def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient["ingredient_name"] not in list(ingredients.keys()):
                print(list(ingredients.keys()))
                ingredients[ingredient["ingredient_name"]] = {"measure":ingredient["measure"], "quantity":int(ingredient['quantity'])*person_count}
            else:
                print(f'ing={ingredient["ingredient_name"]}')
                ingredients[ingredient["ingredient_name"]]["quantity"] += int(ingredient['quantity'])*person_count
    return ingredients

    
with open("recipes.txt", "r", encoding="utf8") as f:
    cook_book = {}
    prev_line=""
    for counter, line in enumerate(f):
        if counter == 0 or prev_line == "\n":
            cur_recipe = line[:-1]
            cook_book[cur_recipe] = []
        ingredient = line.split(" | ")
        if len(ingredient) > 1:
            cook_book[cur_recipe].append({"ingredient_name":ingredient[0], "quantity":ingredient[1], "measure":ingredient[2][:-1]})
        prev_line = line
for cook, ingredients in cook_book.items():
    print(cook)
    for ingredient in ingredients:
        print(ingredient)


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2))



