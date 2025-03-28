y, s = map(int, input().split())

if s == 1 or s == 2:
    print(f"현재 나이는 {2025-((y // 10000) + 1900)}살 입니다")
elif s == 3 or s == 4:
    print(f"현재 나이는 {2025-((y // 10000) + 2000)}살 입니다")
else:
    print("존재하지 않습니다.")