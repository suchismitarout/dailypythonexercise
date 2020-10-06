def check_speed(speed):
    if speed < 70:
        print("OK")
    if speed > 70:
        diff = speed - 70
        point = diff // 5
        print("point is : ", point)
        if point > 12:
            print("License Suspended")


check_speed(140)
