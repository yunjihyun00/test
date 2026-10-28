# 최대, 최소
temps = [25, 32, 28, 36, 27, 31]
biggest = temps[0]
for t in temps:
    if t > biggest:
        biggest = t     # 더 큰 값일 때 갱신
print(biggest)


# 빈 리스트 채우기
doubled = []
for t in temps:
    doubled.append(t * 2)
print(doubled)      # [50, 64, 56, 72, 54, 62]


# 중첩 리스트
# - 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
for row in rows:
    print(row[0], "온도", row[1])