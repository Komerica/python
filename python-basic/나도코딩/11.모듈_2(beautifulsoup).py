# 11-6.pip install
#     : 패키지 설치
#     -> 파이썬은 수많은 패키지가 존재해서 내가 패키지를 새로 만드는것보다 이미 잘 만들어진 패키지를 잘 가져와서 쓰는게 중요!
# 📍 구글에서 "pypi" 검색!
# Web Scrapping에 아주 유명한 "Beautifulsoup"이라는 패키지
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip install beautifulsoup4
#   : beautifulsoup4 다운로드!

# pip list
#   : 현재 설치되어 있는 패키지 내용에 대해서 볼 수 있다!

# pip show beautifulsoup4
#   : 이 패키지(beautifulsoup4)에 대한 정보를 알려줌

# pip install --upgrade beautifulsoup4
#   : 최신버전 업그레이드

# pip uninstall beautifulsoup4
#   : beautifulsoup4 삭제하기
