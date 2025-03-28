#수강 신청 프로그램

names = ["홍길동", "일지매"]
print(f"현재 프로그래밍 수강 신청자는 {names}입니다.")
a_name = input("추가할 학생 이름: ")
print(f"{a_name} 학생의 신청이 완료되었습니다.")
names.append(a_name)
print(f"현재 이 과목의 최종 신청자는 {names}입니다.")

print(" ")

print(f"현재 이 과목의 최종 신청자는 {names}입니다.")
r_name = input("철회할 학생 이름: ")

if r_name in names:
    names.remove(r_name)
    print(f"{r_name} 학생의 수강 철회가 완료되었습니다")
print(f"현재 이 과목의 최종 신청자는 {names}입니다.")
print(" ")

print(f"현재 이 과목의 최종 신청자는 {names}입니다.")
l_name = input("변경 전 이름: ")
n_name = input("변경 후 이름: ")
while True:
    if l_name in names:
        names[names.index(l_name)] = n_name
        print(f"요청하신 대로 {l_name}을(를) {n_name}(으)로 변경하였습니다.")
        print(f"현재 이 가목의 최종 신청자는 {names}입니다.")
        break
    else:
        print("요청하신 내용을 찾을 수 없습니다.")
        break
