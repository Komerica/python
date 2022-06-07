# 10-1.예외처리
from multiprocessing.sharedctypes import Value


try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0]/nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다!")
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다!")
    print(err)  # Error 이름 자체를 출력해 줄 수도 있다!
    #             division by zero
# except IndexError as err:
#     print(err)  # list index out of range
# 👆 위처럼 처리를 해도 되지만 그냥 무슨 에러인지 명시하지않고 👇아래처럼 except 만 적어줘도 상관없다!
# except:  # ValueError / ZeroDivisionError가 아닌 모든 Error를 여기서 처리한다!
#     print("알 수 없는 에러가 발생하였습니다.")
#
except Exception as err:  # ValueError / ZeroDivisionError가 아닌 모든 Error가 뭔지 출력하고 싶을때 "Exception"!
    print(err)


# 10-2.에러 발생시키기
try:
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError  # 의도적으로 어떠한 Error를 발생시켜서..
        # 바로 아래👇 print문은 실행되지 않고,
        # 그 아래 👇 해당 Error를 처리하는 예외 구문("except ValueError")로 내려간다!
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")


# 10-3.사용자 정의 예외처리
#     : ValueError / ZeroDivisionError 등은 Python에서 미리 제공하는 Error이고,
#       사용자가 직접 에러를 정의해서 보여준다!

class BigNumberError(Exception):  # Exception이라는 class를 상속을 받는다!
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("***** 사용자 정의 예외처리: BigNumberError *****")
    print("한 자리 숫자 나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        # 👆 위 문제가 발생했을때 👇아래 정의한 메세지를 위의 class BigNumberError에다 던져주면..
        # ..그곳에서 메세지를 갖고 있다가..
        # 👇여기서 입력하는 메세지가 print(err)했을때 볼 수 있는 에러메세지!!!👇
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
except BigNumberError as err:
    # ..이곳에서 처리가 될때 메세지를 가지고 와서 class BigNumberError에서 갖고 있던 메세지를 받아와서 처리를 해주는 것!
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요")
    print(err)  # result: 입력값 : 10, 1    ->  내가 무슨 값을 잘 못 넣어서 오류가 발생했구나! 알 수 있다!

# 10-4.finally
#     : 예외처리 구문에서 정상적으로 수행이 되건, 오류가 발생하건 무조건 실행이 되는 부분!
#       try 구문 마지막에 쓸수 있다
finally:
    print("계산기를 이용해 주셔서 감사합니다.")


# 10-5.퀴즈 #9
# Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.
# 조건1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#        출력 메시지: "잘못된 값을 입력하였습니다."
# 조건2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
#        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
#        출력 메시지: "재고가 소진되어 더 이상 주문을 받지 않습니다."
# [코드]
# 방법1) 내 방법
class SoldOutError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


chicken = 10
waiting = 1  # 홀 안에는 현재 만석. 대기번호 1부터 시작
try:
    while(True):
        print("[남은 치킨 : {0}]". format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order < 1:
            raise ValueError
        if order > chicken:  # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다".
                  format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken <= 0:
            raise SoldOutError(f"[남은 치킨] : {chicken}")
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except SoldOutError as err:
    print(err)
    print("재고가 소진되어 더 이상 주문을 받지 않습니다.")


# 방법2) 나도코딩 방법
class SoldOutError2(Exception):
    pass


chicken = 10
waiting = 1  # 홀 안에는 현재 만석. 대기번호 1부터 시작
while(True):
    try:
        print("[남은 치킨 : {0}]". format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))

        if order > chicken:  # 남은 치킨보다 주문량이 많을때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다".
                  format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0:
            raise SoldOutError2
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError2:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break  # while문 탈출!(프로그램 종료!)
