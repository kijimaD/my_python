def adder(x):
    def fun(y):
        return x + y
    return fun


adder5 = adder(5)
print(adder5(10))

adder7 = adder(7)
print(adder7(10))