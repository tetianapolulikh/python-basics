def make_album(musician_name, album_name, songs_number = None):
    album = {'name':musician_name, 'album': album_name}
    if songs_number:
        album['songs'] = songs_number
    return album

ready_album = make_album('Michael Jackson', 'Bad')
print(ready_album)

ready_album = make_album('Madonna', 'Who"s That Girl', songs_number = 4)
print(ready_album)