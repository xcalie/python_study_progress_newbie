
'''
python的函数主要是省略了很多条条框框
导致可读性下降
'''

def progress1 (a):
    print(a)

'''
正式代码在def以外的地方运行
也就是在使用由def定义的函数前
def内部的语句都不会执行
'''

"这里就是正式代码"
progress1(3)


'''
返回值就是在代码def结束的时候会返回一个值
值返回到正式代码继续进行
由return执行
'''
def progress2 (b):
    c = b + 1
    return c


print(progress2(4))

d = progress2(6)
print(d)


"函数也可以进行嵌套"
"这里先把9传入progress2其中使得传入的值+1并返回"
"再进入progress1其中的内容为print这个变量"
progress1(progress2(9))


"return 也有特殊用法,其在函数出现意味着函数立刻结束"
def progress3 (x):
    if (x % 2 == 1) :
        return "奇数"
    else :
        return "偶数"


progress1(progress3(15))
    

"作为对比"
def progress4 (x):
    return
    if (x % 2 == 1) :
        return "奇数"
    else :
        return "偶数"

progress1(progress4(15))