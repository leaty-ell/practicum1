#9
def origin_playlist():
    print("Введите плей-лист папы:")
    playlist = []
    while True:
        song = input()
        if song == "":
            break
        playlist.append(song)
    return playlist

def reversed_playlist(playlist):
    print("Плей-лист мамы:")
    i = len(playlist) - 1
    while i >= 0:
        print(playlist[i])
        i -= 1

playlist = origin_playlist()
reversed_playlist(playlist)