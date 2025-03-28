score = list(map(float, input().split()))

sum = 0
b = len(score)
while len(score):
    a = score[0]
    print(f"점수: {a}")
    score.pop(0)
    sum += a
avg = sum / b
print("=" * 10)
print(f"합계: {sum:.1f}")
print(f"평균: {avg:.1f}")
