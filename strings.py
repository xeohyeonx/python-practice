# 문자열 : 'ㅇㅇ' or "oo" (문자열도 사칙연산=문자열 연결이 가능)

print("hello" + "world")

print("hello" * 3)

print("코드잇")
print("유재석")  # 따옴표는 출력값에서는 안나오고, 입력할때 이게 문자열이라는걸 보여주는 장치

# print('I'm excited to learn Python!') : apostrophe 뒷부분이 따옴표로 포함이 안됨. 그니까 I만 문자열로 인식되고 뒷부분은 따옴표가 앞뒤로 제대로 안됐으니까 error
print("I'm excited to learn Python!")  # 이런식으로 ""를 쓰면 가운데의 '가 그냥 문자열 안에 포함된 내용인걸로 제대로 인식됨.

# print("I'm "excited" to learn Python!") 과 같이 ""안에 또 ""가 있는 경우에는 문자열 내에 사용된 모든 따옴표 앞에 역슬래쉬(=원화표시)를 쓰면 됨.
print("I\'m \"excited\" to learn Python!")

# 형 변환 = type conversion / casting = 정수를 소수로, 문자열을 정수로 등 자료형을 변환하는것
print(int(3.8))  # 이걸 실행하면 3이 나옴. 왜냐면 int=integer, 즉 정수를 뜻하는거니까
print(float(3))  # float = floating point = 소수형

print(int("2") + int("5"))  # int()는 괄호 안의 값을 정수형으로 바꾸라는 뜻이니까 문자열 ""가 정수가 됨.

print(float("1.1") + float("2.5"))

print(str(2) + str(5))  # str = string = 문자열. 즉 괄호 안의 값을 문자열로 바꿔주는것

age = 7
# print("제 나이는" + age + "살입니다.") : 문자열과 정수형(age)을 연결시킬 수 없어서 error
print("제 나이는" + str(age) + "살입니다.")  # 이렇게 age 를 문자열로 바꿔줘야함.

# print(int("Hello World")) 은 오류. hello world 는 숫자형으로 바꿀 수 없는 값.