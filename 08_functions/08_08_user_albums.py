#

def make_album(artist_name, album_title, songs=None):
    '''Describing albums'''
    album_info = {'name': artist_name, 'title': album_title}
    if songs:
        album_info['songs'] = songs
    return album_info

while True:
    print("\nEnter your favorite artist's album.")
    print("(If you wish to exit, enter quit)")

    artist = input("Artist name:").title()
    if artist == 'quit':
        break

    album = input("Album title:").title()
    if album == 'quit':
        break

    user_album = make_album(artist, album)
    print(f"\n{user_album}")