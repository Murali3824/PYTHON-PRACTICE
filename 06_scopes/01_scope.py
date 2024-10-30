username = "murali"

def func():
    # username = "laddu"
    print(username)

print(username)
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)


def f1():
    x = 88
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def functiom(num):
    def actual(x):
        return x ** num
    return actual



f = functiom(2)
g = functiom(3)

print(f(3))
print(g(3))