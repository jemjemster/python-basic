# -*- coding: utf-8 -*-
"""파이썬300제 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yTKH9QFi8UUSyijq4lyyVsJIoSqfl-p9

## 분기문 
- 101번 ~ 130번
"""

#101번
# bool 타입

#102번 
print( 3 == 5 )

#103번 
print(3 < 5)

#104번 
x = 4
print(1 < x < 5)

#105번 
print ((3 == 3) and (4 != 3))

#106번 
print(3 => 4) 
# x >= y , x <= y 연산자만 가능

#107번 
if 4 < 3:
    print("Hello World")    
# 조건 만족이 안되기때문에 출력이 안된다.

#108번 
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# 4 < 3 이 미성립되므로 Hi, there이 출력된다.

#109번 
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")

#110번
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

#111번
user = input("입력:")
print(user * 2)

#112번
user = input("숫자를 입력하세요:")
print(int(user) + 10 )

#113번
user = input("")
if int(user) % 2 == 0:
  print("짝수")
else:
  print("홀수")

#114번
user = input("입력값: ")
num = 20 + int(user)

if num > 255:
  print("출력값:",255)
else:
  print("출력값:",num)

#115번
user = input("입력값: ")
num = int(user) - 20

if num < 0:
  print("출력값:",0)

elif num > 255:
  print("출력값:",255)

else:
  print("출력값:", num)

#116번 시간에 왜 -2를 쓰는지 모르겠다.

#117번
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은?")

if user in fruit:
  print("정답입니다.")
else:
  print("오답입니다.")

#118번
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("종목명:")

if user in warn_investment_list:
  print("투자 경고 종목입니다.")
else:
  print("투자 경고 종목이 아닙니다.")

#119번
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가 좋아하는 계절은:" )
if user in fruit.keys():
  print("정답입니다.")
else:
  print("오답입니다.")

#120번
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")

if user in fruit.values():
  print("정답입니다.")
else:
   print("오답입니다.")

#121번
user = input("")

if user.islower():
  print(user.upper())
else:
  print(user.lower())

#122번
user = input("score:" )

if 81 <= int(user) <= 100:
  print("grade is A")
elif 61 <= int(user) <= 80:
  print("grade is B")
elif 41 <= int(user) <= 60:
  print("grade is C")
elif 21 <= int(user) <= 40:
  print("grade is D")
else:
  print("grase is E")

#123번 안됨 
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

#124번
num1 = input("input number1:" )
num2 = input("input number2:")
num3 = input("input number3:")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
  print(num1)
elif num2 >= num1 and num2 >= num3:
  print(num2)
else:
  print(num3)

#125번
num = input("휴대전화 번호 입력: ")
num = num.split("-")[0]
if num == "011":
   tel = "SKT"
elif num == "016":
   tel = "KT"   
elif num == "019":
   tel = "LGU"
else:
   tel = "알수없음"
print(f"당신은 {tel} 사용자입니다.")

#126번
num = input("우편번호: ")
num = num[:3]

if num in ["010", "011", "012"]:
  print("강북구")
elif num in["014", "015", "016"]:
  print("도봉구")
else:
  print("노원구")

#127번
주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
else:
    print("여자")

#128번
주민번호 = input("주민등록번호: ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

#129번 몰라

#130번 몰라

"""## 반복문
- 131번 ~ 150번 
"""

#131번 리스트에 있는 목록 나온다.
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

#132번 for문 핵심은 "들여쓰기된 코드가 자료구조에 저장된 데이터 개수만큼 반복된다" 
# 과일이 3가지 종류이므로 #####이 3번 반복
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

#133번

#134번

#135번

#136번

#137번

#138번

#139번

#140번

#141번

#142번

#143번

#144번

#145번

#146번

#147번

#148번

#149번

#150번