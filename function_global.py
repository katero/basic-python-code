x = 50

def func():
    global x

    print('x is ', x)
    x = 2
    print('changed global x to', x)

func()
print('the value of x is', x)
