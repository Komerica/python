################
#5-1.리스트 [] #
################
from random import *
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호는 몇번째칸에 타고있는가?
print(subway.index("조세호"))  # 1

# 다음 정류장에서 하하가 탔다
subway.append("하하")
print(subway)

# 유재석/조세호 사이에 정형돈이 탔다!
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는사람을 뒤에서부터 한명씩 꺼냄
print(subway.pop())  # 하하
print(subway)  # ['유재석', '정형돈', '조세호', '박명수']
print(subway.pop())  # 박명수
print(subway)  # ['유재석', '정형돈', '조세호']
print(subway.pop())  # 조세호
print(subway)  # ['유재석', '정형돈']

subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬sort
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 리스트 내 모든 내용 삭제!
# num_list.clear()
print(num_list)

# 다양한 자료형과 같이 사용가능!
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

####################################
#5-2.사전(dictionary) {} {1: "hi"} #
####################################
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])  # 유재석
print(cabinet[100])  # 김태호
print(cabinet.get(3))  # 유재석

# print(cabinet[5]) #없는 key값을 대괄호이용하여 불러오려고 하면 오류 + 프로그램종료
print(cabinet.get(5))  # 없는 key값을 get을 이용해 가져오면 오류x -> None출력
print(cabinet.get(5, "사용가능"))  # key5의 값이 없으면 "사용가능"으로 default값을 설정해줌

print(3 in cabinet)  # 3이라는 key가 있으면 True -> True
print(5 in cabinet)  # 5라는 key가 없으니까 False

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])  # 유재석
print(cabinet["B-100"])  # 김태호

# 새손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# keys만 출력
print(cabinet.keys())  # dict_keys(['B-100', 'C-20'])

# value만 출력
print(cabinet.values())  # dict_values(['김태호', '조세호'])

# 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)


##################
#5-3.튜플(tuple) #
##################
#   : 리스트와는 다르게 내용변경/추가를 할 수 없음!
#     So, 할수있는게 딱히 많이 없음 BUT, 속도가 list보다 빠름!
menu = ("돈까스", "치즈까스")  # 튜플만드는 방법!
print(menu[0])
print(menu[1])

# menu.add("생선까스") #오류 (값 추가 못함)

##튜플의 활용#
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby) #김종국 20 코딩
# 👆일반적으로 이렇게 하나하나 변수를 선언 해줘야하는 것에 반해,
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)
# 👆튜플로 작성하면 바로 한번에 값을 넣을 수 있다!


#################
#5-4.세트 set{} #
#################
#   : 중복안됨, 순서없음
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python 모두 할 수 있는 개발자?)
print(java & python)  # 방법1
print(java.intersection(python))  # 방법2

# 합집합 (java 할 수 있거나 python할 수 있거나)
print(java | python)  # 방법1
print(java.union(python))  # 방법2

# 차집합 (Java는 할 줄 알지만 python은 할줄 모르는 개발자)
print(java - python)  # 방법1
print(java.difference(python))  # 방법2

# python할줄아는사람이 늘어남!
python.add("김태호")
print(python)

# java를 까먹음!
java.remove("김태호")
print(java)


#####################
#5-5.자료구조의 변경 #
#####################
# 커피숍
menu = {"커피", "우유", "주스"}  # set {}
print(menu, type(menu))

menu = list(menu)  # list []
print(menu, type(menu))

menu = tuple(menu)  # tuple ()
print(menu, type(menu))

menu = set(menu)  # set {}
print(menu, type(menu))

menu = dict(menu) # dict(dictionary) {1: "hi"}
print(menu, type(menu))


###########
### Quiz ##
###########
# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석를을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1영은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 당첨 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
#  -- 당첨자 발표 --
#  치킨 당첨자 : 1
#  커피 당첨자 : [2, 3, 4]
#  -- 축하합니다 --

# (활용 예제)
print("********Quiz********")
lst = [1, 2, 3, 4, 5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

# 방법1) (내가한 방법)
print("********Answer1********")
comment = {1: "hi", 2: "안녕", 3: "바이", 4: "응", 5: "댓글", 6: "comment", 7: "그래", 8: "케미", 9: "jp", 10: "jh",
           11: "ss", 12: "감사", 13: "고맙", 14: "응응", 15: "고맙다", 16: "고맙네", 17: "하하", 18: "븅신", 19: "그..", 20: "헤헤"}
# comment = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(sample(comment,2))
당첨자 = sample(list(comment), 4)
shuffle(당첨자)
print(당첨자)
치킨당첨자 = 당첨자.pop()  # 맨뒤에 있는 숫자 return함!
커피당첨자 = 당첨자

print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {치킨당첨자}")
print(f"커피 당첨자 : {커피당첨자}")
print("-- 축하합니다 --")


# 방법2) 유튜브 답안
print("********Answer2********")
users = range(1, 21)  # 1부터 20까지 숫자를 생성
users = list(users)  # list
shuffle(users)
print(users)

winners = sample(users, 4)  # 1명 치킨, 3명 커피

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")
