height = int(input("키(cm): "))
weight = int(input("체중(kg): "))

if 130 <= height < 190 and 25 <= weight < 100:
    print("#" * 10)
    print("이용가능")
    print("키(cm): ", height)
    print("체중(kg):", weight)
else:
    print("#" * 10)
    print("이용불가능")
    print("키(cm): " + height)
    print("체중(kg): " + weight)