a = int(input())

if 210 <= a < 250:
    print("보통")
elif 250 <= a < 300:
    print("상")
elif 300 <= a < 375:
    print("특")
elif a >= 375 or a < 210:
    print("측정 불가")