#4-2.슬라이싱
jumin = "990120-1234567"
print("성별: " + jumin[7])
print("출생년도: " + jumin[0:2])
print("출생월: " + jumin[2:4])
print("출생일: " + jumin[4:6])
print("생년월일: " + jumin[:6])
print("뒤7자리: " + jumin[7:])
#-1째자리: 7
#-2째자리: 6
#-3째자리: 5
#...
#-7째자리: 1
print("뒤7자리: " + jumin[-7:]) #1234567


#4-3.문자열처리함수
python = "Python is amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) #첫번째 문자는 upper입니까? -> True
print(len(python))
print(python.replace("Python", "Java"))
index = python.index("n") #5
print(index) #5
index = python.index("n", index + 1) #5 + 1 = 6번째 자리부터 n을 찾는다!
print(index) #15
print(python.find("n")) #n의 index를 알려준다 -> 5
print(python.find("Java")) #find에서 내가 없는 글자를 찾으면 -1를 반환
#print(python.index("Java")) #index에서 내가 없는 글자를 찾으면 오류를 반환
print(python.count("n")) #n이 총 몇번나오는지? -> 2


#4-4.문자열포맷(String formatting)
#방법1)
print("나는 %d살입니다." % 20) # %뒤에 있는 숫자를 d(정수)에 넣겠다!
print("나는 %s를 좋아해요." % "파이썬") #%s(문자열,string)
print("Apple은 %c로 시작해요" % "A") #%c(character, 한글자)
#👇 %s만 해줘도 정수건, 하나의 문자이건 다 처리가능! 👇
print("나는 %s살입니다." % 20) #나는 20살입니다.  %s 이지만 숫자가능!
print("저는 %s색과 %s색을 좋아합니다." % ("파란", "빨간")) #저는 파란색과 빨간색을 좋아합니다.

#방법2)
print("나는 {}살입니다.".format(20)) #나는 20살입니다.
print("저는 {}색과 {}색을 좋아합니다.".format("파란", "빨간")) #저는 파란색과 빨간색을 좋아합니다.
print("저는 {1}색과 {0}색을 좋아합니다.".format("파란", "빨간")) #저는 빨간색과 파란색을 좋아합니다.

#방법3)
print("저는 {age}살이며, {color}색을 좋아합니다.".format(color ="빨간", age= 20)) #저는 20살이며, 빨간색을 좋아합니다.

#방법4) (v3.6 이상~)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아합니다.") #나는 20살이며, 빨간색을 좋아합니다.


#4-5.탈출문자(escape)
#\n: 줄바꿈
#\r: 커서를 맨앞으로 이동 후, 기존 글자를 삭제해가면서 타입(수정기능!)
print("Red Apple\rPine") #"Red "가 지워지고 "Pine"으로 대체!(4자리)
#\b: 백스페이스 (한 글자 삭제),back space
print("Redd\bApple") #RedApple
#\t: 탭 tab
print("Red\tApple") #Red     Apple


#4-6.퀴즈
#Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver. com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e 갯수 + "!" 로 구성
#                 (nav)               (5)            (1)      (!)
# 예) 생성된 비밀번호 : nav51!
#방법1)
url = "http://naver.com"
규칙1 = url[-9:]
규칙2 = 규칙1[:-4]
규칙3 = 규칙2[:-2] + str(len(규칙2)) + str(규칙2.count("e")) + "!"
print(규칙3) #nav51!

#방법2)
#Ex1)
url = "http://naver.com"
#Ex2)
url = "http://youtube.com"
my_str = url.replace("http://", "") #규칙1 -> naver.com
my_str = my_str[:my_str.index(".")] #규칙2 -> naver
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(password) #nav51!
print("{0}의 비밀번호는 {1}입니다.".format(url, password))
print(f"{url}의 비밀번호는 {password}입니다.")
