# 11-1.모듈
#     : 필요한 것들끼리 부품처럼 잘 만들어진 파일!
#   *모듈화: 딱 필요한 것들끼리 부품처럼 잘 만드는 과정을 모듈화!

######################
## 모듈 가져오는 방법! #
######################

# 방법1)
# import theater_module
# theater_module.price(3)  # 3명이서 영화보러갔을때 가격
# theater_module.price_morning(4)  # 4명이서 조조할인보러 갔을때 가격
# theater_module.price_soldier(5)  # 5명의 군인이 영화보러 갔을때 가격

# 방법2)
# mv로 줄여서 표현가능!
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# 방법3)
# from random import * 와 비슷한 맥락!
# from theater_module import *
# # -> 이렇게 하면 앞에 아무것도 없이 바로 함수를 호출할 수 있다!
# price(3)
# price_morning(4)
# price_soldier(5)

# 방법4)
# from theater_module import price, price_morning  # 내가 갖고 오고 싶은 함수만 가져오기!
# # 군인이였다가 제대해서 군인할인(price_soldier)은 더이상 필요없다고 하자!
# price(3)
# price_morning(4)
# # price_solider(5) #이건 쓸 수 없음!

# 방법5)
# from theater_module import price_soldier as price
# price(4)  # -> price_solider를 price처럼 쓰는것!


# 11-2.패키지 (travel 디렉토리 참고!)
#     : 모듈들을 모아놓은 집합!(하나의 디렉토리에 여러 모듈파일을 모아놓은 것!)
# 방법1) import 문 사용
# import travel.thailand
# import travel.thailand.ThailandPackage #❌ -> 처럼 import문에서 바로 class를 가져오는건 안되지만, ..
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# 방법2) from ~ import ~ 문 사용
# ..👇 아래처럼 from으로 파일경로 설정 하고 import로 class를 불러오는 것은 -> ✔
# 📍 from ~ import ~ 구문에서는 모듈,패키지,클래스,함수 모두 import 가능!
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# 방법3)
# from travel import vietnam  # [ from ~ import ~ ] 구문이라 import에 파일 경로넣는거도 쌉가능~
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# 11-3.__all__
## from random import *
# from travel import *
# # 👆 이렇게 했을때 vietnam.VietnamPackage()에서 오류가 나는 이유는..?
# # travel directory에서 모든 module(*)을 가져오는 것처럼 보이지만,
# # 실제로는 개발자가 공개범위를 설정해준것에 한해서만 import가 된다!
# # -> 이렇게 공개범위를 설정해주는 것을 "__init__.py"라는 파일에서 한다!
# # 👉 이 파일 안에서 __all__ = ["vietnam"] 라고 작성해주면 아래의 👇 vietnam.VietnamPackage()가 작동한다! ✔
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()
# # 잘 작동을 함에도 빨간 밑줄이 나오는 것은 settings -> search linting -> python Linting:Enabled에 체크 빼주기로 해결가능
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# 11-4.모듈 직접 실행
# -> thailand.py 파일로 이동!
# 여기서 모듈이 실행되면, "Thailand 외부에서 모듈 호출"이 호출되는 것을 볼 수 있음!


# 11-5.패키지,모듈 위치
import inspect
import random
from travel import *  # 이 부분이 있어야, 아래👇 getfile(thailand)가 가능하다!
# 파일위치 추적
print(inspect.getfile(random))  # 👉 C:\Python310\lib\random.py
print(inspect.getfile(thailand))  # 👉 C:\Python310\lib\travel\thailand.py
#                                   -> (프로젝트를 할때는 만들어 놓은 모듈을 여기로 가져다 놓자!)
# 👉 c:\Users\Jepil Lee\Desktop\projects\python\python-basic\나도코딩\travel\thailand.py
trip_to = thailand.ThailandPackage()
trip_to.detail()
