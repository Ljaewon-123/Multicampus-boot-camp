'''
총 3대의 매물
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
'''


class House:
  #매물 초기화
  def __init__(self, location, house_type, deal_type, price, completion_year):
    self.location = location
    self.house_type = house_type
    self.deal_type = deal_type
    self.price = price
    self.completion_year = completion_year

  #매물 정보 표시
  def show_detail(self):
    print(self.location,
    self.house_type,
    self.deal_type ,
    self.price,
    self.completion_year )

# 객체를 리스트에 넣는다는게 신기

house = []
house1 = House("강남","아파트","매매","10억","2010년")
house2 = House("마포","오피스텔","전세","5억","2007년")
house3 = House("송파","빌라","월세","500/50","2000년")

house.append(house1)
house.append(house2)
house.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(house)))
for house in house:
  house.show_detail()