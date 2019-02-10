
def shows_prompt():

    print('Shows\n')

    view_shows()

    print('\t1) Add a show\n' +
          '\t2) Delete a show\n' +
          '\t3) Back\n'-
          )
    try:
        usr_input = int(input('\n>'))
    except Exception:
        shows_prompt()

    if usr_input == 1:
        show_builder()
    elif usr_input == 2:
        remove_show()
    elif usr_input == 3:
        main_prompt()
    else:
        shows_prompt()


def playlist_prompt():
    print('Playlist menu:\n' +
            '\t1) Play song\n' +
            '\t2) View playlist\n' +
            '\t3) Add to playlist\n' +
            '\t4) Remove song\n' +
            '\t5) Back\n')

    try:
        usr_input = int(input('\n>'))
    except Exception:
        playlist_prompt()

    if usr_input == 1:
        play_songs()
    elif usr_input == 2:
        view_songs()
    elif usr_input == 3:
        song_builder()
    elif usr_input == 4:
        remove_song()
    elif usr_input == 5:
        main_prompt()
    else:
        playlist_prompt()

def main_prompt():
    print('YouStream:\n'
            '\n\t1) View Shows'
            '\n\t2) View your playlist'
            '\n\t3) Exit')

    try:
        usr_input = int(input('\n>'))
    except Exception:
        main_prompt()

    if usr_input == 1:
        shows_prompt()
    elif usr_input == 2:
        playlist_prompt()
    elif usr_input == 3:
        exit()
    else:
        main_prompt()


def show_builder():
    tmp_list = []
    field_list = ['Title', 'Rating']

    for field in field_list:
        tmp = input(f'what is the shows {field}:').lower()
        tmp_list.append(tmp)

    shows_list.append(tmp_list)
    shows_prompt()


def view_shows():
    if len(shows_list) > 0:
        for show in shows_list:
            print(f'Title: {show[0]}, Rating: {show[1]}')
    else:
        print('Shows are unavailable...\n')


def remove_show():
    print("\n What show do you want to remove?:")
    rm_title = input('\n> ').lower()
    for show in shows_list:
        if show[0] == rm_title:
            show_index = shows_list.index(show)
            shows_list.pop(show_index)
    shows_prompt()


def remove_song():
    print("\n What song do you want to remove?:")
    rm_title = input('\n> ').lower()
    for song in songs_list:
        if song[0] == rm_title:
            song_index = songs_list.index(song)
            songs_list.pop(song_index)
    playlist_prompt()


def view_songs():
    if len(songs_list) > 0:
        for song in songs_list:
            print(f'Title: {song[0]}, Duration: {song[1]}')
    else:
        print('Songs are unavailable...\n')
    playlist_prompt()


def song_builder():
    tmp_list = []
    field_list = ['Title', 'Duration']

    for field in field_list:
        # 'What is the shows ' + field + ': '
        tmp = input(f'what is the songs {field}:').lower()
        tmp_list.append(tmp)

    songs_list.append(tmp_list)
    print(songs_list)
    playlist_prompt()


def play_songs():
    print("\n What song do you want to listen to?:")
    song_player = input('\n> ').lower()
    for song in songs_list:
        if song[0] == song_player:
            print(f'Now playing: {song[0]}, Duration: {song[1]}')
    playlist_prompt()


shows_list = []
songs_list = []
main_prompt()
