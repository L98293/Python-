print(f"{'*' *3} 도형 넗이 계산 {'*'*3}")

print ("1. 삼각형 2. 사각형 3. 원")

a = input()
print(f"도형종류: {a}")
height = int(input())
width = int(input())

print(f"밑변(cm): {width}")
if a == 1:
    print(f"삼각형 넓이는 {(height) * (width) // 2}cm^2입니다.")
elif a == 2:
    print(f"사각형의 넓이는 {(height) * (width)}cm^2입니다")
else:
    r = int(input())
    pi = 3.14
    print("원의 넓이는", ((r ** 2) * pi), "입니다"))

# 특이사항: 버그났는데 어디가 틀린지 몰라서 포기함