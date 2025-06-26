class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'\nThe name of the restaurant is {self.restaurant_name} and there you can try { self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is opened now!')

restaurant_1 = Restaurant('Sushi Box', 'chinese cuisine')
restaurant_2 = Restaurant('Pizza Hut', 'italian cuisine')
restaurant_3 = Restaurant('Puzata Hata', 'ukrainian cuisine')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()