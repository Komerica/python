# Turtle Documentation: https://docs.python.org/3/library/turtle.html
import another_module

# another_module 에서 another_variable 이라는 변수를 가져옴!
print(another_module.another_variable)


# import turtle
#
# # turtle module 에서 Turtle class를 가져오는것! class는 항상 ()있어야함
# timmy = turtle.Turtle()
# 👆 위와 같이 해도 되지만, 👆

# 👇 더욱 간단하게 하기 위해서 👇
from turtle import Turtle, Screen

# turtle.Turtle() 이라고 안쳐도 됨!
timmy = Turtle() # screen 을 반짝하고 보여줌!
print(timmy)
timmy.shape("turtle")
timmy.color("green", "coral")
timmy.shapesize(5)
timmy.forward(100)

my_screen = Screen()
# canvheight = canvas height -> an attribute that's associated with that screen.
print(my_screen.canvheight)

# exitOnClick: screen이 click을 감지하면 code실행이 멈춘다!(screen 꺼짐)
my_screen.exitonclick() # height:300, width:300 화면 계속 띄워줌


