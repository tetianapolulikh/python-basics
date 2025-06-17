def build_profile(name, last, **user_info):
    user_info['first_name'] = name
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Tetiana', 'Polulikh', location = 'Europe', sex = 'female' )
print(user_profile)
