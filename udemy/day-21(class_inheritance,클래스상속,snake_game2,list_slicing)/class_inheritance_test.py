class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")


class Labrador(Dog):
    # 이니셜라이저에서 super()를 호출하는 것을 추천하지만 필수는 아닙니다!!
    def __init__(self):
        self.temperament = "friendly"


리트리버 = Labrador()
# 위에 super()를 호출해주지 않았지만, Dog부모를 상속하기 때문에 bark()는 쓸 수 있다!
리트리버.bark()