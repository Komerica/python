# 9-12.퀴즈 #8

# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
# 방법1) 내 방법
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(f"총 {len(houses)}대의 매물이 있습니다.")
        for house in houses:
            print(house.location, house.house_type, house.deal_type,
                  house.price, house.completion_year)


houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)


House.show_detail(House)
# House.show_detail(house1)
# House.show_detail(houses)

# 방법2) 나도코딩 방법


class House2:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,
              self.price, self.completion_year)


houses2 = []
house4 = House2("강남", "아파트", "매매", "10억", "2010년")
house5 = House2("마포", "오피스텔", "전세", "5억", "2007년")
house6 = House2("송파", "빌라", "월세", "500/50", "2000년")

houses2.append(house4)
houses2.append(house5)
houses2.append(house6)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses2:
    house.show_detail()
