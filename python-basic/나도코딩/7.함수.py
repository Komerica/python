# 7-2.전달값과 반환값
from tabnanny import check


def open_account():
    print("새로운 계좌가 생성되었습니다.")


def deposit(balance, money):
    balance += money
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance))
    return balance


def withdraw(balance, money):
    if balance < money:
        print(f"잔고가 부족합니다. 잔고는 {balance}입니다.")
        return balance
    else:
        balance -= money
        print(f"{money}원을 인출하였습니다. 잔고는 {balance}입니다.")
        return balance


def withdraw_night(balance, money):
    commission = 100  # 수수료 100원
    if balance < money:
        print(f"잔고가 부족합니다. 잔고는 {balance}입니다.")
    else:
        balance -= money + commission
        if(balance < 0):
            print(f"잔고가 모자랍니다!")
        else:
            print(f"{money}원을 인출하였습니다. 잔고는 {balance}입니다.")
    return commission, balance


balance = 0
balance = deposit(balance, 50_000)
balance = withdraw(balance, 40_000)
commission, balance = withdraw_night(balance, 9900)

# 7-3.기본값


def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))


profile("유재석", 20, "파이선")
profile("김태호")


# 7-4.키워드값
def profile1(name, age, main_lang):
    print(name, age, main_lang)


profile1(name="유재석", main_lang="파이썬", age=20)  # 순서바뀌어도 출력가능


# 7-5.가변인자
def profile2(name, age, *languages):
    # name, age까지 출력하고 끝에 end=" "로 이어주고 바로 같은줄에 연달아서 밑에 코드까지 출력!
    print(f"이름: {name}\t나이: {age}\t", end="")
    print("언어: ", end="")
    # type(lang) = tuple -> ()
    for language in languages:
        print(language, end=" ")
    print()


profile2("하하", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
profile2("유재석", 25, "Kotlin", "Swift")


# 7-6.지역변수와 전역변수

gun = 10


def checkpoint(soldiers):
    global gun  # 이런식으로 전역변수를 함수안에서 쓰면 좋지 못한 코드!
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))


def checkpoint_return(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총: {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
gun = checkpoint_return(gun, 2)
print("남은 총: {0}".format(gun))


# 7-7.퀴즈
# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중: 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) X 키(m) X 22
# 여자 : 키(m) X 키(m) X 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명: std_weight
#         * 전달값: 키(height), 성별(gender)
# 조건2: 표준 체중은 소수점 둘째자리까지 표시
#
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

# 방법1) 내가 한거
def std_weight(height, gender):
    if gender == "남자":
        result = height * height * 22
    elif gender == "여자":
        result = height * height * 21
    return print(f"키 {height*100:.0f}cm {gender}의 표준 체중은 {result:.2f}kg 입니다.")


std_weight(1.75, "여자")

# 방법2) 유튜브 답안!(나도코딩)


def std_weight2(height, gender):
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21


height = 175
gender = "남자"
weight = round(std_weight2(height/100, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2} ")
