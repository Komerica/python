# 🟪 *args
# parameter name "args" is the convention followed by many developers (But we can use any name for "args")
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


result = add(1, 2, 3, 4)
print(result)


# data type "tuple"로 들어간다!
def test(*args):
    print(type(args))   # tuple
    print(args[0])      # 1이 print된다!
    for n in args:      # tuple이라 iterable임!
        print(n)


test(1, 2, 3)


# 🟪 **kwargs: keyword arguments
#   : It gives us a way to name the values that we're passing in to this function.
def calculate(**kwargs):
    print("**kwargs")
    print(kwargs)           # {'add': 3, 'multiply': 5}
    print(type(kwargs))     # <class 'dict'>
    # add: key,  3: value  /  multiply: key,  5: value
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(kwargs["add"])        # 3
    print(kwargs["multiply"])   # 5


calculate(add=3, multiply=5)


def calculate2(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate2(2, add=3, multiply=5)


# 🟪 **kw in class!
#   : This allows us to create a Class with lots of optional keyword!
class Car:
    def __init__(self, **kw):
        # kw["make"]를 안하고 kw.get("make")를 해서 장점은..
        # instance를 만들때 값을 안 넣어도 print를 하면 에러를 주지않고 None으로 출력! ↓ 참고
        self.make1 = kw.get("make")
        self.model_1 = kw["model_2"]
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# ↓     {"make": "Nissan", "model_2": "GT-R"}   ->  kw["model_2"] = "GT-R"
# my_car = Car(make="Nissan", model_2="GT-R")
my_car = Car(model_2="GT-R", color="Skyline")
print(my_car.model_1)
print(my_car.make1)     # kw.get("make") 의 장점은 instance를 만들때 값을 부여하지 않은 argument에 대해서 에러를 내지 않고 None을 출력함
print(my_car.color)     # Skyline


# 🟪 *args + **kw
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)  # 4 (7, 3, 0) {'x': 10, 'y': 64}

