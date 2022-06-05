# 9-9. super(다중상속)
class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        # 위와 같이 다중상속(Unit, Flyable)을 받을때 👆위와 같이 super()를 쓰면..
        # ..첫번째로 상속 받는 클래스(Unit)만 __init__()함수가 호출이 된다!
        # dropship = FlyableUnit()  ->  "Unit 생성자"
        #################################################################
        # 이러한 문제가 있기 때문에 다중 상속을 할때, ..
        # ..모든 부모 클래스(Unit, Flyable)에 대해서 초기화가 필요하면, ..
        # ..따로 명시적으로..
        Unit.__init__(self)
        Flyable.__init__(self)
        # 위와 같이 하면..
        # "Unit 생성자" / "Flyable 생성자" 둘다 잘 호출이 된다!


# 드랍쉽
dropship = FlyableUnit()
# -> Unit 생성자
