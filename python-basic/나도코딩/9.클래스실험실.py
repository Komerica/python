# 9-10.스타크래프트 프로젝트 전반전
class Unit:  # Ex) 메딕
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))  # self.name / name 둘다 써도됨.

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):  # Ex)파이어뱃, 마린
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"
              .format(self.name, location, self.damage))


class Marine(AttackUnit):  # 마린
    def __init__(self):  # 유닛 세부사항이 👇처럼 이미 다 정해져서 나오면 self만 적어주고 멤버변수는 따로 적어줄필요없음!
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):  # 스팀팩 : 일정시간 동안 이동/공격 속도를 증가, 체력 10 감소
        if self.hp > 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


class Tank(AttackUnit):  # 시저탱크
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
    # -> 시즈모드 개발하면 모든 탱크에 똑같이 적용돼서 함수를 만들지 않고 👇아래처럼 개발여부로 나타내준다!
    seize_developed = False  # 시즈모드 개발여부

    def __init__(self):  # 유닛 세부사항이 👇처럼 이미 다 정해져서 나오면 self만 적어주고 멤버변수는 따로 적어줄필요없음!
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        # 👇👇 시저탱크가 처음 태어나면 시즈모드는 당연히 False!
        # 이처럼 이미 False로 정해져서 나오는거라 멤버변수로, 즉, __init__(self, seize_mode)처럼 전달해주지 않는다
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return  # -> 시즈모드가 아니면 아무것도 return해주지 않는다!
        # 현재 시즈모드가 아닐때 -> 시즈모드
        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
            # 현재 시드모드 일때 -> 시즈모드 해제
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Flyable(Unit):  # 공중 유닛     Ex) 드랍쉽
    def __init__(self, name, hp, speed, flying_speed):
        Unit.__init__(self, name, hp, 0)
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):  # 공중 공격 유닛     Ex) 발키리
    def __init__(self, name, hp, damage, flying_speed):
        # AttackUnit.__init__(self, name, hp, 0, damage)  # 지상speed 0 (공중이라 지상없음)
        # Flyable.__init__(self, name, hp, 0, flying_speed)
        # 👆위 두줄 처럼 이런식으로 Unit을 부모로 갖고 있는 AttackUnit + Flyable 클래스를 두개다 초기화 해주면
        # Unit에 들어 있는 print("{0} 유닛이 생성되었습니다.".format(name)) 메세지가 두번 출력되는 것을 볼 수 있음!
        # 그래서 super()을 써서 AttackUnit / Flyable 클래스 중 하나만 초기화를 해줄 수 있다! 그럼 메세지가 하나만 출력됨!
        super().__init__(name, hp, 0, damage)
        self.flying_speed = flying_speed

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)


class Valkyrie(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "발키리", 80, 6, 6)


발키리1 = Valkyrie()


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드(해제 상태)

    def clocking(self):
        if self.clocked == True:  # 클로킹 모드(True) -> 모드 해제(False)
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:  # 클로킹 모드 해제(False) -> 모드 설정(True)
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True
