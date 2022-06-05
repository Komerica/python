# 9-4.메소드
# 일반 유닛     Ex)메딕
class Unit:  # 부모클래스
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))
# 👆 Unit class의 self.name / self.hp와
# 👇 AttackUnit의 self.name / self.hp가 겹치기 때문에 상속가능!

# 9-5.상속


class AttackUnit(Unit):  # Ex)파이어뱃     # 자식클래스
    # 공격 유닛    👆 -> 이렇게 하면 AttackUnit는 Unit 클래스를 상속받아서 만들어진 클래스!
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        # 👆 이런식으로 Unit class를 상속을 해주기때문에 👇아래 코드는 필요없음!
        # self.name = name
        # self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"
              .format(self.name, location, self.damage))  # self.name / self.damage는 위에서 정의된 멤버변수를 쓰는것!
        # location은 attack함수에서 전달받은 parameter를 그대로 가져와서 쓰는것!
        print(
            f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 : {self.damage}]")

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 파이어뱃: 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 5, 16)
firebat1.attack("5시")

# 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)


# 9-6.다중상속
#   : 부모가 2명 이상이다!

# 드랍쉽: 공중유닛, 수송기. -> 마린/파이어뱃/탱크 등을 수송. 공격 기능 X
# 날 수 있는 기능을 가진 클래스
class Flyable:  # 공중 유닛     Ex) 드랍쉽
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


dropship = Flyable(5)


class FlyableAttackUnit(AttackUnit, Flyable):  # 공중 공격 유닛     Ex) 발키리
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상speed 0 (공중이라 지상없음)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)


# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
valkyrie.move("3시")  # method overriding을 통해서 만들어진 method!


# 9-7.메소드 오버라이딩(Method Overriding)
#   : 부모클래스에서 정의한 method 말고, 자식클래스에서 정의한 method를 쓰고 싶을때
#     method를 새롭게 정의해서 사용할 수 있는데, 이를 overriding이라고 한다!

# 벌쳐 : 지상유닛, 기동성 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)


# 배틀크루저 : 공중유닛, 체력 굉장히 좋음, 공격력 굉장히 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")


# 9-8.pass
# 건물
# pass Ex1)
class BuildingUnit2(Unit):
    def __init__(self, name, hp, location):
        pass  # 오류없이 일단 넘어간다는 뜻!


# 서플라이 디폿 : 건물, 1개 건물 = 8유닛
supply_depot = BuildingUnit2("서플라이 디폿", 500, "7시")


# pass Ex2)


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    pass


game_start()
game_over()


# 9-9. super()
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # 📍 Method1) Unit class를 써서 직접적으로 상속해주는 방법
        # Unit.__init__(self, name, hp, 0)
        # 📍 Method2) super()을써서 상속해주는 방법! self 생략가능!
        super().__init__(name, hp, 0)
        self.location = location
