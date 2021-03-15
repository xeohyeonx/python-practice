x = 7
x = x + 1  # "=" 는 지정연산자. 등호 오른쪽의 값을 왼쪽 변수에 집어넣으라는 뜻


def hello():
    print("Hello!")
    print("Welcome to Codeit!")


print("함수 호출 전")
hello()
print("함수 호출 후")  # 이렇게 하면 함수 실행 순서를 볼 수 있음. 위에서 hello 라는 함수를 정의만 하고 실행은 뒤에서 나중에 하는거지.


def square(y):
    return y * y


print("함수 호출 전")
print(square(3) + square(4))
print("함수 호출 후")


# Return 이해하기 : 함수가 어떤 값을 돌려주는것. 함수가 시키는 일을 돌려주는 역할 + 함수 즉시 종료 역할도 함.
# 실행하면 square 함수 z 자리에 3이 들어가고, 그러니까 위의 square 함수로 올라가서 "함수 시작" + 9 + "Hello World!" 가 출력. "함수 끝"은 출력되지 않음. return 은 함수 즉시 종료 역할하니까
def square(z):
    print("함수 시작")
    return z * z
    print("함수 끝")  # 이건 결국 출력되지 않는 라인. = dead code (의미 없는 코드)


print(square(3))
print("Hello World!")


# return vs print : return 문이 따로 없으면, return 값이 없다고 판단해 none 이 return 됨.
def print_square(m):
    print(m * m)


def get_square(n):
    return n * n


print_square(3)  # 값은 9가 출력됨.
get_square(3)  # 이건 단순히 파라미터 안의 값 3이 위의 get_square 함수로 올라가서 이 46 라인의 get_square(3)에 9라는 값을 return 하지만, 아무것도 출력되지 않음.
print(get_square(4))  # 이렇게 뭘 출력할 지 알려줘야 출력값이 나옴

print(print_square(5))  # 우선 print_square 함수로 올라가서 m 에 5가 들어가 print(25)가 됨으로 25가 출력되고, return 문이 없으니까 48번째 줄은 print(None) 꼴이 되어버림. 그래서 None 이 출력됨.


# optional parameter : 꼭 제공하지 않아도 되는거. 기본값이 이미 설정되어있는 경우를 지칭.
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


myself("코드잇", 1, "미국")  # 옵셔널 파라미터인 "미국" 제공
print()
myself("코드잇", 1)  # 옵셔널 파라미터 제공하지 않음.


# 자주 쓰이는 표현을 더 간략하게 쓸 수 있게 해주는 문법을 'syntactic sugar' 라고 합니다.

# 다음 두 줄은 같습니다
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7


# scope = 변수가 사용 가능한 범위; (로컬 변수 vs 글로벌 변수)
# 함수 내에서 정의된 변수는 로컬 변수로, 함수 내에서만 유효. 즉 범위가 정해진 변수니까 따로 print 해도 나오지 않음. 함수 밖에서 정의된건 글로벌 변수로, 함수 안, 밖 어디서든 유효.
# 가장 먼저 함수 내에 로컬 변수가 있는지 확인하고, 그러고 없으면 글로벌 변수가 있는지 찾아보면 됨.
x = 2


def my_function():
    x = 3
    print(x)
# 이렇게 하면 가장 최근 지정한 값인 3과, 그 다음의 print(x) 에서는 글로벌 변수가 사용되니까 2가 출력됨. x = 3이 가장 최근 사용된거긴 하지만 그건 로컬 변수니까


my_function()
print(x)


# 함수에의 파라미터도 로컬
def square(x):
    return x * x


print(square(3))


# 상수 (constant) = 코드 내에서 절대로 바꾸지 않는 숫자. 모든 글자를 대문자로 씀 (상수 구별 용도)

PI = 3.14  # 원주율 파이
def calculate_area(r):
    return PI * r * r


radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))
