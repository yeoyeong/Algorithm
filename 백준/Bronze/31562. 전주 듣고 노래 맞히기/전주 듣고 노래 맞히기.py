import sys
input = sys.stdin.readline 

n, m = input().split(" ")

def parse_song_info(song):
    song = song.split()
    title = song[1]  # 제목 길이에 해당하는 단어를 결합
    preview = ' '.join(song[2:])  # 나머지 부분은 전주로 설정
    return {
        'title': title,
        'preview': preview
    }

songs = []

for _ in range(int(n)):
    song = input().strip()
    song_info = parse_song_info(song)
    songs.append(song_info)
    
# 세글자 비교
def check_preview_start(songs, quiz):
    cnt = 0
    title = ""
    for song in songs:
        preview = song["preview"]
        if preview[:len(quiz)] == quiz:
            cnt += 1
            title = song["title"]
    if cnt > 1:
        return "?"
    if cnt == 0:
        return "!"
    else:
        return title


# 퀴즈 시작
def try_quiz(m):
    for _ in range(int(m)):
        quiz = input().strip()
        print(check_preview_start(songs, quiz))


try_quiz(m)