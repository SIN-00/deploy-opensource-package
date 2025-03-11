"""

Chapter 1
Python Advanced(1) - Python Variable Scope
Keyword - scope, global, nonlocal, locals, globals..

"""

# Ex1
a = 10 # Global variable

def foo():
    # Read global variable 
    print('Ex1 >', a)

foo()

# Read global variable
print('Ex1 >', a)

# Ex2
b = 20

def bar():
    b = 30 # Local variable
    print('Ex2 >', b)
bar()
print('Ex2 >', b)

# Ex3
c = 40

def foobar():
    #c = c + 10
    #c = 10
    #c +=10 다안됨 UnboundLocalError
    print('Ex3 >',c)

foobar()

# Ex4

d = 50
def barfoo():
    global d #global이라는 예약어를 통해 전역변수를 쓰고 수정할 수 있음 근데 지양함
    d = 60
    d += 100
    print('Ex4 >',d)

barfoo()

print('Ex4 >', d)

# Ex5(중요) 클로저 패턴
# 상위 영역의 있는 변수를 하위 영역에서 수정하려고할 떄는 nonlocal 예약어 필수
def outer():
    e = 70 # 지역변수 
    def inner(): #이 두영역이 공유가 되고 있는가? -> UnboundLocalError
        nonlocal e #이거 추가해줘야함
        e += 10
        print('Ex5 >',e)
    return inner
in_test = outer()

in_test()
