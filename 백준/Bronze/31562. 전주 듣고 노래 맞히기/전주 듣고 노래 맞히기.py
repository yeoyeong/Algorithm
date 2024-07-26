# 리스트에 겹치는게 여러개 일 경우 ?
# 저장된 노래가 없을 경우 !
# 정환이 아는 개수 N, 시도할 개수 M

# 제목 길이 + 제목 + 음이름 
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


# try_quiz = list(input().strip() for _ in range(int(n)))

# print(songs)

def try_quiz(m):
    result = []
    for _ in range(int(m)):
        quiz = input().strip()
        result.append(check_preview_start(songs, quiz))
    return result
    
    

def check_preview_start(songs, quiz):
    cnt = 0
    title = ""
    for song in songs:
        preview = song["preview"]
        # 첫 세 글자가 target_preview와 일치하는지 확인
        if preview[:len(quiz)] == quiz:
            cnt += 1
            title = song["title"]
    if cnt > 1:
        return "?"
    if cnt == 0:
        return "!"
    else:
        return title



results = try_quiz(m)

for result in results:
    print(result)

# 실행 시켰을 때 E D E 가