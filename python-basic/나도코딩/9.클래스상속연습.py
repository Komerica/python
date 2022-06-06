class Unit:  # 메딕
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{self.name}이 생성되었습니다. [체력: {self.hp}]")

    def move(self, direction):
        print("[지상 유닛 이동]")
        print(f"{self.name} 이(가) {direction} 방향으로 이동합니다. [속도 : {self.speed}]")


class AttackUnit(Unit):  # 파이어뱃
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage


medic1 = Unit("메딕", 50, 5)
firebat1 = AttackUnit("파이어뱃", 70, 5, 16)
medic1.move("5시")


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 120, 4, 20)
        self.seize_mode = False

    def set_seize_mode(self):
        if not Tank.seize_developed:
            return
        if not self.seize_mode:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.seize_mode = True
            self.damage *= 2
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.seize_mode = False
            self.damage /= 2


탱크1 = Tank()
탱크1.set_seize_mode()


class Flyable(Unit):  # 드랍쉽
    def __init__(self, name, hp, flying_speed):
        Unit.__init__(self, name, hp, 0)
        self.flying_speed = flying_speed

    def move(self, direction):
        print("[공중유닛이동]")
        print(
            f"{self.name} 이(가) {direction} 방향으로 날아갑니다! [속도: {self.flying_speed}]")


dropship1 = Flyable("드랍쉽", 120, 5)
dropship1.move("1시")


class FlyableAttackUnit(AttackUnit, Flyable):  # 발키리
    def __init__(self, name, hp, damage, flying_speed):
        # AttackUnit 클래스 안에 있는 멤버변수 무조건 다써줘야함!
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상speed 0 (공중이라 지상없음)
        # Flyable 클래스 안에 있는 멤버변수를 Flyable.__init__(여기안에) 무조건 다써줘야함!
        Flyable.__init__(self, name, hp, flying_speed)


valkyrie1 = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie1.move("5시")
