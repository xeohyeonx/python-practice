# while 반복문 : 조건 부분 (불린값으로 계산되는 식; true 면 수행부분 실행, 그걸 실행하면 다시 조건 부분으로 가서 false 가 나올때까지 실행) + 수행부분 (반복 실행하고싶은 명령부분)
# while 조건부분:
#       수행부분

# 나는 잘생겼다 3번 출력하기 (처음에는 i = 1인까 "잘생"부분 출력되고 함수 내에서 i = 2로 바뀌고, 다시 조건부분의 t/f 여부 확인하고 ....
i = 1
while i <= 3:  # i 가 3보다 작거나 같으면 밑의 수행부분을 반복하라는 뜻
    print("나는 잘생겼다")
    i += 1


# 100 이상의 수 중 23의 배수 중에 가장 작은 값 구하기.
i = 100

while (i % 23) != 0:
    i += 1

print(i)

# if:만약, else : 그렇지 않으면 = 상황별로 다른 판단하게 하려는 것. 조건부분 + 수행부분
# if 조건부분:  (이건 불린 값으로 계산되는 식. 이를 충족하면 수행부분이 실행됨. while 과 달리 반복 없음)
#    수행부분
temperature = 16
if temperature <= 10:
    print("자켓을 입는다.")
else:  # 이렇게 else 뒤에 : 콜론이 붙음.
    print("자켓을 입지 않는다.")

# elif : else 문에 안에 새로 if 가 나오는 경우. = else if 의 축약인듯 (조건 옵션이 2개가 아니라 많을때 유용)

# print_grade 함수는 파라미터로 중간고사 점수와 기말고사 점수를 받고, 최종 성적을 출력합니다.
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score

    if total >= 90:
        print("A")
    elif 80 <= total < 90:  # 사실 90 미만이라는건 안붙이고 그냥 total >= 80 만 해도 됨. 이미 90 미만인건 위 조건에 있고 그걸 통과하지 않으니 이 조건을 고려한다는 거니까.
        print("B")
    elif 70 <= total < 80:
        print("C")
    elif 60 <= total < 70:
        print("D")
    else:  # 굳이 60 미만이라고 안써도 나머지 경우는 다 여기에 해당하기 때문에 이렇게만 해도 됨.
        print("F")

# 100 이하의 자연수 중에 8의 배수이면서 12의 배수는 아닌 것을 모두 출력하는 기능
i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1  # 이건 if 문 밖에 있어야함. 안에 있으면 무한 루프

# 1000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램
i = 1
total = 0

while i < 1000:
    if i % 2 == 0 or i % 3 == 0:
        total += i
    i += 1

print(total)

# i = 1
# total = 0  누적된 합을 보관하는 변수인 total
#
# while i < 10:
#     total += i  # total = total + i와 동일
#     i += 1  # i = i + 1과 동일
#
# print(total)  : 이건 10보다 작은 자연수의 합을 출력하는 프로그램. total += i 를 매번 하는게 아닌 2 또는 3의 배수일 경우에만 하는 조건을 붙여주면 됨.

# 정수 n 의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램. n = 120
i = 1
n = 120
count = 0

while i <= n:
    if n % i == 0:
        print(i)
        count += 1
    i += 1

print("{}의 약수는 총 {}개입니다.".format(n, count))

print(2 ** 3)

# 원금 5000만원에 12% 이자율 for 28 yrs 과 11억 비교
year = 1

total_bank = 0

while year <= 28:
    total_bank = 50000000 * (1.12 ** year)
    year += 1


if  total_bank > 1100000000:
   print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(total_bank - 1100000000)))
else:
   print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(total_bank - 1100000000)))


# 모범답안

# 상수 정의
INTEREST_RATE = 0.12
APARTMENT_PRICE_2016 = 1100000000
# 변수 정의
year = 1988
bank_balance = 50000000

while year < 2016:
    bank_balance = bank_balance * (1 + INTEREST_RATE)
    year += 1

if bank_balance > APARTMENT_PRICE_2016:
    print("{}원 차이로 동일 아저씨 말씀이 맞습니다.".format(int(bank_balance - APARTMENT_PRICE_2016)))
else:
    print("{}원 차이로 미란 아주머니 말씀이 맞습니다.".format(int(APARTMENT_PRICE_2016 - bank_balance)))
