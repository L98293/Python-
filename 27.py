import random as r

Com = r.choices([1, 2, 3, 4, 5, 6], k = 2)
a, b = map(int, input("2개 입력(1~6, 중복 허용)").split())
Users = (r.sample([a, b],2))

print(f"사용자 입력: {Users}")
print(f"컴퓨터 입력: {Com}")
if Users[0] in Com and Users[1] in Com:
    print("1등!")
elif Users[0] in Com or Users[1] in Com:
    print("2등!")
else:
    print("3등!")