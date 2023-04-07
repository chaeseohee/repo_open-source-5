"""
# Code 09-01
coffee = 0

coffee = int(input("어떤 커피 드릴까요?(1:보통, 2:설탕. 3:블랙)"))

print()
print("#1. 뜨거운 물을 준비한다. ")
print("#2. 종이컵을 준비한다. ")

if coffee == 1:
    print("#3. 보통커피를 탄다. ")
elif coffee == 2:
    print("#3. 설탕커피를 탄다. ")
elif coffee == 3:
    print("#3. 블랙커피를 탄다. ")
else:
    print("#3. 아무거나 탄다. ")

print("#4. 물을 붓는다. ")
print("#5. 스푼으로 젓는다. ")
print()
print("손님~ 커피 여기 있습니다. ")
"""

"""
# Code 09-02
coffee=0

def coffee_machin(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다. ")
    print("#2. (자동으로) 종이컵을 준비한다. ")

    if coffee == 1:
        print("#3. (자동으로) 보통커피를 탄다. ")
    elif coffee == 2:
        print("#3. (자동으로) 설탕커피를 탄다. ")
    elif coffee == 3:
        print("#3. (자동으로) 블랙커피를 탄다. ")
    else:
        print("#3. (자동으로) 아무거나 탄다. ")

    print("#4. (자동으로) 물을 붓는다. ")
    print("#5. (자동으로) 스푼으로 젓는다. ")
    print()

coffee=int(input("어떤 커피 드릴까요?(1.보통, 2:설탕, 3.블랙)"))
coffee_machin(coffee)
print("손님~ 커피 여기 있습니다. ")
"""

"""
# Code 09-03
coffee = 0

def coffee_machin(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다. ")
    print("#2. (자동으로) 종이컵을 준비한다. ")

    if coffee == 1:
        print("#3. (자동으로) 보통커피를 탄다. ")
    elif coffee == 2:
        print("#3. (자동으로) 설탕커피를 탄다. ")
    elif coffee == 3:
        print("#3. (자동으로) 블랙커피를 탄다. ")
    else:
        print("#3. (자동으로) 아무거나 탄다. ")

    print("#4. (자동으로) 물을 붓는다. ")
    print("#5. (자동으로) 스푼으로 젓는다. ")
    print()


coffee = int(input("A손님, 어떤 커피 드릴까요?(1.보통, 2:설탕, 3.블랙)"))
coffee_machin(coffee)
print("A손님~ 커피 여기 있습니다. ")

coffee = int(input("B손님, 어떤 커피 드릴까요?(1.보통, 2:설탕, 3.블랙)"))
coffee_machin(coffee)
print("B손님~ 커피 여기 있습니다. ")

coffee = int(input("C손님, 어떤 커피 드릴까요?(1.보통, 2:설탕, 3.블랙)"))
coffee_machin(coffee)
print("C손님~ 커피 여기 있습니다. ")
"""

"""
# Code 09-04
def plus(v1, v2):
    result = 0
    result = v1 + v2
    return result

hap = 0

hap = plus(100, 200)
print("100과 200의 plus() 함수 결과는 %d" % hap)
"""

"""
# Code 09-05
def calc(v1, v2, op):
    result = 0
    if op == '+':
        result = v1 + v2
    elif op == '-':
        result = v1 - v2
    elif op == '*':
        result = v1 * v2
    elif op == '/':
        result = v1 / v2
    return result


res = 0;
val1, val2, oper = 0, 0, ""

oper = input("계산을 입력하세요(+, -, *, /): ")
val1 = int(input("첫 번째 수를 입력하세요: "))
val2 = int(input("두 번째 수를 입력하세요: "))

res = calc(val1, val2, oper)
print("##계산기: %d %s %d = %d" % (val1, oper, val2, res))
"""

"""
# Code 09-06

def func1():
    a=10
    print("func1()에서 a값 %d" % a)

def func2():
    print("func2()에서 a값 %d" % a)

a=20

func1()
func2()
"""

"""
# Code 09-07

def func1():
    global a
    a=10
    print("func1()에서 a값 %d" % a)

def func2():
    print("func2()에서 a값 %d" % a)

a=20

func1()
func2()
"""

"""
# Code 09-08

def func1():
    result=100
    return result

def func2():
    print("반환값이 없는 함수 실행")

hap=0

hap=func1()
print("func1()에서 돌려준 값 ==> %d" %hap)
func2()
"""

"""
# Code 09-09

def multi(v1, v2):
    retList = []
    res1 = v1 + v2
    res2 = v1 - v2
    retList.append(res1)
    retList.append(res2)
    return retList

myList=[]
hap, sub=0,0

myList=multi(100,200)
hap=myList[0]
sub=myList[1]
print("multi()에서 돌려준 값 ==> %d %d" %(hap, sub))
"""

"""
# Code 09-10

def para2_func(v1, v2):
    result = 0
    result = v1 + v2
    return result


def para3_func(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = 0

hap = para2_func(10, 20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap = para3_func(10, 20, 30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)
"""

"""""
# Code 09-11

def para_func(v1,v2,v3=0):
    result=0
    result=v1+v2+v3
    return result

hap=0

hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과: %d" %hap)
hap=para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과: %d" %hap)
"""

# Code 09-12
"""
def para_func(*para):
    result = 0
    for num in para:
        result = result + num
    return result

hap=0

hap=para_func(10,20)
print("매개변수가 2개인 함수를 호출한 결과 ==> %d" % hap)
hap=para_func(10,20,30)
print("매개변수가 3개인 함수를 호출한 결과 ==> %d" % hap)
"""

# Code 09-13
"""
import random

def getNumber():
    return random.randrange(1,46)

lotto=[]
num=0

print("** 로또 추첨을 시작합니다. **\n")

while True:
    num=getNumber()
    if lotto.count(num)==0:
        lotto.append(num)
    if len(lotto)>=6:
        break

print("추첨된 로또 번호 ==> ", end='')
lotto.sort()
for i in range(0,6):
    print("%d " %lotto[i], end='')
"""

# Code 09-14
"""
from myTurtle import *
import turtle

inSTr = ''
swidth, sheight = 300, 300
tX, tY, tAngle, tSize = [0] * 4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.speed(5)
inStr = getString()

for sh in inStr:
    tX, tY, tAngle, txtSize = getXYAS(swidth, sheight)
    r, g, b = getRGB()

    turtle.goto(tX, tY)
    turtle.left(tAngle)

    turtle.pencolor((r, g, b))
    turtle.write(sh, font=('맑은고딕', txtSize, 'bold'))

turtle.done()
"""

"""
# 실습 4-1 [A]
from typing import Any

class FixedStack:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity
"""

"""
# 실습 4-1 [B]
    def push(self, value: Any) -> None:
        if self.is_full():            
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():             
             raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():          
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0
"""

"""
# 실습 4-1 [C]
    def find(self, value: Any) -> Any:
        for i in range(self.ptr - 1, -1, -1): 
            if self.stk[i] == value:
                return i  
        return -1        

    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.ptr):  
            if self.stk[i] == value:
                c += 1          
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> None:
        if self.is_empty():  
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])
"""

"""
# 실습 4-3 [A]
from typing import Any

class FixedQueue:

    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0     
        self.front = 0 
        self.rear = 0  
        self.capacity = capacity      
        self.que = [None] * capacity  

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity
"""

"""
# 실습 4-3 [B]
    def enque(self, x: Any) -> None:       
        if self.is_full():
            raise FixedQueue.Full  
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
"""

"""
# 실습 4-3 [C]
    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty 
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
"""

"""
# 실습 4-3 [D]
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty  
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:  
                return idx
        return -1 

    def count(self, value: Any) -> bool:
        c = 0
        for i in range(self.no):  
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value: 
                c += 1  
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():  
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end=' ')
            print()
"""