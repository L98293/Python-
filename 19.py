fee = 800

card = int(input("카드 잔액을 입력하세요: "))

if card >= fee:
    print("탑승가능")
else:
    print("잔액부족")