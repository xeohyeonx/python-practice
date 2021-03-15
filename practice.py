# 거스름돈 계산 my version
def calculate_change(payment, cost):
    # 코드를 작성하세요.
    a = int((payment - cost) / 50000)
    b = int((payment - cost - 50000*a) / 10000)
    c = int((payment - cost - 50000*a - 10000*b) / 5000)
    d = int((payment - cost - 50000*a - 10000*b - 5000*c) / 1000)
    print("50000원 지폐: {}장".format(a))
    print("10000원 지폐: {}장".format(b))
    print("5000원 지폐: {}장".format(c))
    print("1000원 지폐: {}장".format(d))

# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)


# 모범 답안
def calculate_change(payment, cost):
    change = payment - cost  # 거스름돈 총액

    fifty_count = change // 50000  # 50,000원 지폐. //는 버림나눗셈
    ten_count = (change % 50000) // 10000  # 10,000원 지폐. %는 나머지를 알려주는 연산이니까 거스름돈을 50000으로 나눈 나머지를 10000으로 버림나눗셈한다는 뜻.
    five_count = (change % 10000) // 5000  # 5,000원 지폐
    one_count = (change % 5000) // 1000  # 1,000원 지폐

    # 답 출력
    print("50000원 지폐: {}장".format(fifty_count))
    print("10000원 지폐: {}장".format(ten_count))
    print("5000원 지폐: {}장".format(five_count))
    print("1000원 지폐: {}장".format(one_count))


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)