year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
# 이렇게 하면 너무 번거로우니까 문자열 포맷팅을 통해서 하면 더 편함

print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))  # 이렇게 해주면 중괄호 안에 format 뒤의 파라미터들이 순서대로 들어감.

# 이렇게도 가능.
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))
print(date_string.format(year, month, day + 1))  # 그 다음날이 출력됨


print("저는 {}, {}, {}를 좋아합니다!".format("박지성", "유재석", "빌게이츠"))
# to change the order, 중괄호 안에 번호를 쓰면 됨. numbering starts from 0
print("저는 {1}, {0}, {2}를 좋아합니다!".format("박지성", "유재석", "빌게이츠"))


num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))  # .2f는 f = floating pt, .2 = 소숫점 2째자리까지 반올림하라는 뜻. .0f라고 쓰면 정수형이 나옴.


# Boolean = 불린. 참/거짓 (따옴표 없이 True or False)
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)

print(2 > 1)
print(2 < 1)
print(3 >= 2)
print(2 == 2)  # 2는 2와 같다 라는 뜻
print(2 != 2)   # 2는 2와 같지 않다는 뜻
print("Hello" == "Hello")
print(2 > 1 and "Hello" == "Hello")  # = True and True

print(not not True)  # = not false
print(not not False)  # = not true

print(7 == 7 or (4 < 3 and 12 > 10))  # = True or (False and True) 가 되니까 값은 True

x = 3
print(x > 4 or not (x < 2 or x == 3))  # = False or not (False or True) 니까 False or (not True) = False or False = False


# 꿀팁이라네. type 이라는 함수 : 자료형을 알려줌
print(type(3))
print(type(3.0))
print(type("3"))
print(type("True"))
print(type(True))  # bool = boolean 의 줄임말


def hello():
    print("Hello world!")


print(type(hello))  # 함수도 하나의 자료형
print(type(print))  # 내장되어있는 함수라는 뜻.


# practice : ()안의 수가 짝수이면 True, 홀수이면 False 가 출력되게끔 하는 함수 만들기
def is_evenly_divisible(number):
    return number % 2 == 0


# 테스트 코드
print(is_evenly_divisible(3))
print(is_evenly_divisible(7))
print(is_evenly_divisible(8))
print(is_evenly_divisible(218))
print(is_evenly_divisible(317))