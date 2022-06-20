#문제 1번
def plus(num1,num2):     
    return num1+num2

def minus(num1,num2):    
    return num1-num2

def multiply(num1,num2): 
    return num1*num2

def division(num1,num2): 
    return num1/num2

while(True):
    num1, num2 = map(int,input("연산을 진행할 두 숫자를 입력하시오 : ").split(" "))
    i= input("어떠한 연산을 수행할까요? ")

    if(i == '+'):
        plus(num1,num2)
    elif(i == '-'):
        minus(num1,num2)
    elif(i == '*'):
        multiply(num1,num2)
    elif(i == '/'):
        division(num1,num2)
    else:
        print("해당 연산은 지원하지 않습니다.")
