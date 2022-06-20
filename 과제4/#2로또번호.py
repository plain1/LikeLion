#문제 2번
import random
import time

def lotto():
    number = random.sample(range(1,46),6)
    number.sort()
    for i in range(1,6):
        print("%d ..."%i)
        a = time.sleep(2)
    print("로또번호는!!")
    print(number)

while(True):
    a = input("로또번호 추출을 시작합니까?(y/n) :")
    if a == "y":
        print("번호 추출중...")
        lotto()
    else:
        print("로또 추출을 종료합니다.")