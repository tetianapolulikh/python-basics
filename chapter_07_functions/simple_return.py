def city_country(city, country):
    location = f'{city}, {country}'
    return location.title()

chosen_location = city_country('lviv','ukraine')

print(chosen_location)

while True:
    print('\nPlease tell me your location: ')
    print('(enter "q" at any time to quit)')

    your_city = input('Your city: ')
    if your_city == 'q':
        break

    your_country = input('Your country: ')
    if your_country == 'q':
        break

    formated_location = city_country(your_city,  your_country)
    print(f'\nYour locatin is - {formated_location}')