# 3-3.숫자처리함수
from random import *  # random / randrange / randint 등을 쓸때는 필수!
from random import *
from math import *
print(floor(4.99))
print(ceil(4.14))
print(sqrt(16))

# 3-4.랜덤함수
print(random())  # 0.0 ~ 1.0 미만의 임의의 값을 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값을 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값을 생성
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값을 생성
# Ex) 로또 추첨번호
print("*****Lotto Winning Numbers*****")
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값을 생성!
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값을 생성!
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값을 생성!
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값을 생성!
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값을 생성!
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값을 생성!
# Ex2) 로또 추첨번호(쉬운버전)
print("*****Lotto Winning Numbers*****")
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성
# Ex3) 로또 추첨번호(더 쉬운버전)
print("*****Lotto Winning Numbers*****")
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성


# 리스트 중 랜덤으로 뽑기!
names = ['Jp', 'Ss', 'Jh', 'Lo']
# 방법1)
num_items = len(names)
random_choice = randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay)
# 방법2) Simple way
# 👆 위 4줄을 한줄로 아래👇처럼 간단하게 처리할 수 있다!
#   -> random.choice(list)
print(choice(names))


# Quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# 조건1 : 랜덤으로 날짜를 뽑아야 함
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 X 일로 선정되었습니다.
print("*****Quiz*****")
day = randint(4, 28)
print(f"오프라인 스터디 모임 날짜는 매월 {day} 일로 선정되었습니다.")
