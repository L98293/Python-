import random as r

Users = r.choice(["가위", "바위", "보"])
Com =  r.choice(["가위", "바위", "보"])

print(f"사용자 입력값: {Users} \n컴퓨터 입력값: {Com}")

if Users == Com:
    print("비겼음")
elif Users == "가위" and Com == "바위" or Users == "바위" and Com == "보" or Users == "보" and Com == "가위":
    print("졌음")
else:
    print("이겼음")