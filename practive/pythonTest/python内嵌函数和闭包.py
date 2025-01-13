def outer():
    x = 1
    print('I am from outer')
    def inner():
        print("I am form inner")
        print(x)  # 可以访问外部变量，但outer没有返回inner
    inner()  # 在outer内部直接调用

outer() 

# 内嵌和闭包都可以访问外部函数的变量，但如果要修改外部变量，需要在内部用关键字nonlocal声明，再修改。
# nonlocal 允许内部函数修改外部变量
# 闭包"记住"了创建时的环境。
# 只读取外部变量：不需要 nonlocal，修改外部变量：需要 nonlocal 声明


