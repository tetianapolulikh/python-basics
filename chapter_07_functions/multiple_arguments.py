def make_burger(*ingredients):
    print('\nMaking burger with the following ingredients: ')
    for ingredient in ingredients:
        print(f'- {ingredient}')

make_burger('ham', 'salad', 'tomato', 'sauce')
make_burger('chicken', 'cucumber')
make_burger('chicken', 'cucumber', 'bacon', 'egg', 'picles', 'onion', 'sauce')

