import random as r
cum = r.randint(1, 20)

while True:
    a = int(input("숫자입력(종료0): "))
    if a > cum:
        print("더 작은 숫자 입력")
        continue
    if a < cum:
        print("더 큰 숫자 입력")
        continue
    if a == cum:
        print("정답!!")
        break