# 6-1.if
from random import *
weather = input("날씨가 어때요")
if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요없음!")

temp = int(input("기온이 어때요?"))
if 30 <= temp:
    print("너무 더워요. 나가지마!")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨임ㅋ")
elif 0 <= temp < 10:
    print("외투 챙겨!")
else:
    print("너무 추워요 나가지마세요!")

# 6-2.for
lst = [1, 2, 3, 4, 5]
for waiting_num in lst:
    print("대기번호 : {0}".format(waiting_num))
# 👇range를 이용하여 더 간단하게 쓰는 방법
for waiting_num in range(1, 6):  # 1,2,3,4,5
    print("대기번호 : {0}".format(waiting_num))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}님, 커피가 준비되었습니다.".format(customer))

# 6-3.while
customer = "sasa"
index = 5
while index >= 1:
    print("{0}님 커피가 준비되었습니다. 호출 {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다!")

# 무한루프 예시
# 손님 = "아이언맨"
# count = 0
# while True:
#     print("{0}님, {1}호출했습니다!".format(손님, count))1
#     count += 1

customer = "토르"
person = "Unknown"
while person != customer:
    print("{0}님, 커피 준비됐습니다.".format(customer))
    person = input("Your name?")

# 6-4.continue와 break
absent = [2, 5]
no_book = [7]
for student in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue  # absent에 있는 숫자가 걸리면 바로 다음 반복으로 넘어감!(continue)
    elif student in no_book:
        print("오늘 수업 여기 까지! {0}는 교무실로 따라와!".format(student))
        break
    print("{0}, 책 읽어봐".format(student))

# 6-5.한줄 for
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)

# Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 :2명

# 방법1) 내가한 방식
count = 0
passengers = range(1, 51)  # type -> range

for passenger in passengers:
    time = randrange(5, 51)  # 5분 ~ 50분 소요시간 랜덤
    if 5 <= time <= 15:
        count += 1
        print(f"[O] {passenger}번째 손님 (소요시간 : {time}분)")
    else:
        print(f"[ ] {passenger}번째 손님 (소요시간 : {time}분)")
print(f"총 탑승 승객 :{count}명")

# 방법2) 유튜브에서 한 방식!
#from random import *
count = 0
for passenger in range(1, 51):
    time = randrange(5, 51)  # 5분 ~ 50분 소요시간 랜덤
    if 5 <= time <= 15:  # 5 ~ 15분 이내의 손님 매칭성공한 경우
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(passenger, time))
        count += 1
    else:  # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(passenger, time))
print("총 탑승 승객 :{0}명".format(count))
