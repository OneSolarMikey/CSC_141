#

def make_album(artist_name, album_title, songs=None):
    '''Describing albums'''
    album_info = {'name': artist_name, 'title': album_title}
    if songs:
        album_info['songs'] = songs
    return album_info

album = make_album('Radiohead', 'A Moon Shaped Pool')
print(album)
album = make_album('Joji', 'Nectar')
print(album)
album = make_album('NWA', 'Straight Outta Compton', songs=13)
print(album)