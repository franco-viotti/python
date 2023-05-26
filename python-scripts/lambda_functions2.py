def testfunc(num):
    return lambda x: x*num

result1 = testfunc(10)
print(result1(9))
