# 8-1.표준입출력
# sep=","  ->  separator
# end = " "  -> 다음 나오는 print문과 같은 line상에 출력하고 싶을때 쓰기!
import pickle
import sys
print("Python", "Java", "JavaScript", sep=" vs ", end="?")
print("무엇이 더 재밌을까요?")

print("Python", "Java", file=sys.stdout)  # 표준출력
print("Python", "Java", file=sys.stderr)  # 표준에러로 처리하는것

# 시험 성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():  # items(): keys() + values()
    # ljust(8): 8개의 공간을 확보하고 왼쪽정렬    # rjust(4): 4개의 공간을 확보하고 오른쪽정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")  # 구버전
    print(f"{subject.ljust(8)}", f"{str(score).rjust(4)}", sep=":")  # 신버전

# 은행 대기순번표
# 001,002,003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))  # 3개공간을 확보하고 나머지 빈공간은 0으로 채워라!
    print(f"대기번호 : {str(num).zfill(3)}")  # zfill()을 쓰기 위해서는 무조건 str으로 바꿔줘야함!


# 8-2.다양한 출력 포맷
# 📍 10자리를 확보하는데, 오른쪽정렬을 하고 그 10칸 중에서 500이라는 숫자를 쓴다!
print("📍 10자리를 확보하는데, 오른쪽정렬을 하고 그 10칸 중에서 500이라는 숫자를 쓴다!")
print("{0: >10}".format(500))
print(f"{500: >10}")

# 📍 오른쪽정렬하고, 양수일때는 +로 표시, 음수일때는 -로 표시
print("📍 오른쪽정렬하고, 양수일때는 +로 표시, 음수일때는 -로 표시")
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
print(f"{500: >+10}")
print(f"{-500: >+10}")
# 👉 print("{0: >10}".format(-500))  ->  -500이 나오긴한데,
#    print("{0: >10}".format(500))   ->  일때는, +500이 안찍힘!

# 📍 왼쪽정렬하고, 빈칸은 _로 채움
print("📍 왼쪽정렬하고, 빈칸은 _로 채움")
print("{0:_<+10}".format(500))  # +500______
print("{0:_<10}".format(500))  # 500_______
print(f"{500:_<+10}")
print(f"{500:_<10}")

# 📍 3자리마다 콤마를 찍어주기 (comma)
print("📍 3자리마다 콤마를 찍어주기 (comma)")
print("{0:,}".format(100000000000))
print(f"{100000000000:,}")

# 📍 3자리마다 콤마를 찍어주기, +-부호도 붙이기
print("📍 3자리마다 콤마를 찍어주기, +-부호도 붙이기")
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
print(f"{100000000000:+,}")
print(f"{-100000000000:+,}")

# 📍 자리마다 콤마를 찍어주기, +-부호도 붙이기, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈자리는 ^로 채워주기
print("📍 자리마다 콤마를 찍어주기, +-부호도 붙이기, 자릿수 확보하기")
print("{0:^<+30,}".format(100000000000))
print(f"{100000000000:^<+30,}")
# ** 순서 **
# 1 -> :
# 2 -> ^        (빈자리 채울 문자)
# 3 -> < OR >   (정렬)
# 4 -> +        (+-부호 붙이기)
# 5 -> 30       (자릿수)
# 6 -> ,        (3자리마다 콤마찍기)

# 📍 소수점 출력
print("📍 소수점 출력")
print("{0:f}".format(5/3))
print(f"{5/3:f}")

# 📍 소수점 특정 자리수 까지만 표시
print("📍 소수점 특정 자리수 까지만 표시")
print("{0:.2f}".format(5/3))
print(f"{5/3:.2f}")


# 8-3.파일입축력
# 📍 txt파일만들고 쓰기!
print("📍 txt파일만들고 쓰기!")
score_file = open("score.txt", "w", encoding="utf8")  # w = write
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# 📍 기존 txt파일에 내용 추가
print("📍 기존 txt파일에 내용 추가")
# a = append(존재하는 파일에 내용추가)
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 📍 txt파일을 읽기
print("📍 txt파일을 읽기")
score_file = open("score.txt", "r", encoding="utf8")  # r = read
print(score_file.read())  # 파일에 있는 모든 내용 다 들고와서 출력해줌!
score_file.close()

# 📍파일내용을 한줄한줄 줄별로 읽기
print("📍파일내용을 한줄한줄 줄별로 읽기")
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="")  # 줄바꿈하기싫으면 end=""를 붙여줌!
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()

# 📍while을 이용하여 몇줄인지 모를때 txt파일불러오기
print("📍while을 이용하여 몇줄인지 모를때 txt파일불러오기")
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:  # line 변수에 더이상 남은게 없으면:
        break  # while문 멈추는방법!
    print(line, end="")  # 줄바꿈 없이 계속 출력하고싶으면 end=""
score_file.close()
print()  # 한줄띄우기

# 📍list를 이용해서 출력하기
print("📍list를 이용해서 출력하기")
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 모든 line을 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
print()  # 한줄띄우기


# 8-4.pickle
#    : 프로그램 상에서 사용하는 데이터를 파일형태로 저장해주는 것!
# import pickle  #를 무조건 해줘야함(최상단에 있음)

# 📍 pickle로 쓰기(write)
print("📍 pickle로 쓰기(write)")
#                                              pickle에서는 encoding 필요x
profile_file = open("profile.pickle", "wb")  # w = write / b = binary
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 profile_file에 저장
profile_file.close()

# 📍 pickle로 읽기(read)
print("📍 pickle로 읽기(read)")
profile_file = open("profile.pickle", "rb")  # r = read / b = binary
profile = pickle.load(profile_file)  # profile_file에 있는 정보를 profile변수에 대입!
print(profile)
profile_file.close()
# 👉정리하자면, 우리가 갖고 있는 데이터(profile)를 pickle을 이용해서 파일(profile.pickle)에다가 저장하고
#   그 파일에 있는 내용을 load(pickle.load(profile_file))를 통해서 불러와서 변수(profile;line 134)에 저장해서
#   계속 쓸수 있도록 해주는 유용한 library!


# 8-5.with
#   : 지금까지는 파일에 대한 작업을 할때,
#     1.파일을 열고 👉 open("score.txt", "r", encoding="utf8")
#     2.어떤 처리를 하고 👉 print(score_file.read())
#     3.파일을 닫는것 👉 score_file.close()
#     까지 했으면, with를 쓰면 조금 더 편하게 동일한 작업 가능!
#     (매번 닫을 필요없는듯! no close needed)

# 📍 with O / pickle O -> 파일 읽기
print("📍 with O / pickle O -> 파일 읽기(r)")
# import pickle     #pickle 을 쓸때는 무조건 써주기!
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

# 📍 with O / pickle X -> 파일 쓰고(w) 읽기(r)
print("📍 with O / pickle X -> 파일 쓰고(w) 읽기(r)")
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())


# 8-6.퀴즈
# Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 '1주차.txt' '2주차.txt' 와 같이 만듭니다.

# 방법1) 내 방법
for week in range(1, 3):  # range(1,51) 면 1~50주차까지 가능!
    with open(f"{week}주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(f"- {week} 주차 주간보고 -\n부서 :\n이름 :\n업무 요약 :")

# 방법2) 유튜브 방법(나도코딩)
for i in range(1, 3):  # range(1,51) 면 1~50주차까지 가능!
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
