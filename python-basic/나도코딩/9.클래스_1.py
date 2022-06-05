# 9-1.Class
# 마린: 공격유닛, 군인, 총을 쏠수 있음
name = "마린"  # 유닛의 이름
hp = 40  # 유닛의 체력
damage = 5  # 유닛의 공격력

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))


# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있음, 일반모드 /시즈모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{0} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
        name, location, damage))


attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)  # 탱크를 한마리 더 뽑으려고하면 일일이 해줘야함
# 그래서 class를 쓴다!


# 📍 👆위의 복잡한 부분을 Class를 써서 간단하게 나타내자
print("****** Class ******")


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print(f"{self.name} 유닛이 생성되었습니다.")
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        print(f"체력 {self.hp}, 공격력 {self.damage}")


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)


# 9-2.__init__
#   : 파이썬에서 쓰이는 생성자(constructor)!
#   -> 마린이나 탱크가 객체가 만들어질때 자동으로 호출되는 부분!
#   🔸객체(object): marine1, tank와 같이 어떤 클래스로부터 만들어지는 녀석들을 객체!
#   🔸인스턴스(instance): marine1, tank는 Unit 클래스의 instance(인스턴스)이다!


# 9-3.멤버변수
#   : Unit class 안의 self.name / self.hp / self.damage 가 멤버변수가 되는것!
#   -> 즉 멤버변수는 class안에서 정의된 변수! 이고 이 변수를 갖고 실제로 축약할 수 있고 사용할 수 있음!

# 레이스: 공중유닛, 비행기, 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
# " wraith1. "을 써서 멤버변수에 접근이 가능하다!
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
print(f"유닛 이름 : {wraith1.name}, 공격력 : {wraith1.damage}")

# 마인드 컨트롤: 상대방 유닛을 내것으로 만드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
