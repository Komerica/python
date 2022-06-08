###########
# 내장함수 #
# 구글 검색: list of python built-ins
#         -> https://docs.python.org/3/library/functions.html

# 내장함수 예시)
# input: 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir: 어떤 객체를 넘겨줬을때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# format on save를 꺼주고 실행!
# print(dir())
# import random  # 외장함수
# print(dir())
# import pickle
# print(dir())
# print(dir(random))
# 👆-> random 외장함수 안에 뭐가 있는지 보여준다!
# 📍 Result 👇
#['betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']

# lst = [1,2,3]
# print(dir(lst))
# 👆-> list에서 쓸수 있는 내장함수들이 쫙나옴!
# 📍 Result 👇
#['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


# name = "Jin"
# print(dir(name))
# 📍 Result 👇
#['capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


###########
# 외장함수 #
#   : 내장함수와는 다르게, 외장함수는 직접 import를 해서 사용해야하는 것들이다!
# 구글검색: list of python modules(외장함수 목록들)
#        ->https://docs.python.org/3/py-modindex.html

# 외장함수 예시)
# 1. glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우의 dir와 같다!)
# import glob
# print(glob.glob("*.py"))  # 확장자가 py인 모든 파일

# 2. os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())  # 현재 디렉토리
# # result -> C:\Users\Jepil Lee\Desktop\projects\python

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())  # 현재 directory의 파일 목록을 보여준다!


# 3. time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 2022-06-08 10:05:36
# Y = yyyy
# m = mm
# d = dd
# H = hh
# M = mm
# S = ss

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# # timedelta : 두 날짜 사이의 간격을 알려줌!
# today = datetime.date.today()
# print(today)  # 2022-06-08
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today+td)

import byme
byme.sign()
# 👇 Result 👇
# 모듈 외부에서 실행
# 이 프로그램은 나도코딩에 의해 만들어졌습니다.
# 유튜브: http: // youtube.com
# 이메일: nadocoding@gmail.com
