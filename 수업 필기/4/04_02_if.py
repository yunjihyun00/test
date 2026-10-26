# 조건문
# if 기본 구조 - 콜론과 들여쓰기(코드 블록)
# 형식: 
# if 조건식: 
#   실행할 코드 (들여쓰기)
temp = 85
if temp > 80:               # 콜론: 블록 시작 신호
    print("온도 주의")      # 들여쓰기 안 -> 조건 참일 때만 실행
    print("점검 요망")
print("측정 종료")          # 들여쓰기 끝 -> 조건과 무관하게 항상 실행

# else: 조건이 거짓일 때
# 형식:
# if 조건문:
#   참일 때 코드
# else:
#   거짓일 때 코드

score = 55
if score >= 60:
    print("합격")
else:
    print("불합격")


# elif
# 형식:
# if ... elif ... else (위에서부터 검사, 처음 참인 곳만 실행)

score = 82
if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
else:
    print("미흡")

# 논리 연산자 and or not / 범위 조건
temp = 45
print(temp >= 20 and temp <= 60)        # True

if 20 <= temp <= 60:
    print("정상 범위")