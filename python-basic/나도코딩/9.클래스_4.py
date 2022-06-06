from random import *

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


class Flyable:  # 공중 유닛     Ex) 드랍쉽
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):  # 공중 공격 유닛     Ex) 발키리
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상speed 0 (공중이라 지상없음)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중유닛이동]")
        self.fly(self.name, location)


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


# 9-11.스타크래프트 프로젝트 후반전


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")  # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


##################
## 실제 게임 진행 #
##################
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):  # 이 unit은 Marine 클래스의 instance인가?
        # -> unit is instance of Marine?
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))  # 공격은 랜덤으로 5~20 사이의 데미지를 받음

# 게임 종료
game_over()
