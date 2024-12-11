def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
 
user_profile = build_profile('kenny', 'maley',
location = 'alabama',
fav_movie = 'The Dark Knight',
fav_song = 'Mamma Said Knock You Out')
print(user_profile)