class Restaurant:

    def __init__(self,restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'\nThe name of the restaurant is {self.restaurant_name} and there you can try { self.cuisine_type}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is opened now!')

restaurant = Restaurant('Sushi Box', 'chinese cuisine')


restaurant.describe_restaurant()
restaurant.open_restaurant()
