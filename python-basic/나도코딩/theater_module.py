############
## 영화티켓 #
############

def price(people):  # 일반 가격
    print("{0}명 가격은 {1}원 입니다.".format(people, people*10000))


def price_morning(people):  # 조조 할인 가격
    print("{0}명 조조 할인 가격은 {1}원 입니다.".format(people, people*6000))


def price_soldier(people):  # 군인 할인 가격
    print("{0}명 가격은 {1}원 입니다.".format(people, people*4000))
