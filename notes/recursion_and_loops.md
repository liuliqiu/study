# 递归 Recursion
递归是指在函数的定义中使用函数自身的方法
递归：有递有归

# 尾调用
尾调用是指一个函数里的最后一个动作是一个函数调用的情形：即这个调用的返回值直接被当前函数返回的情形。 

# 循环

```
def loop(x):
    while not_end(x):
        x = next_value(x)
    return get_result(x)
```
```
def recursion(x):
    if not_end(x):
        return recursion(next_value(x))
    else:
        return get_result(x)
```
```
def r(x):
    if not_end(x):
        return g(x, r(f(x)))
    else:
        return v(x)
```
```
r(x)
g(x, r(f(x)))
g(x, g(f(x), r(f(f(x)))))
g(x, g(f(x), g(f(f(x))), r(f(f(f(x))))))
g(x, g(f(x), g(f(f(x))), g(f(f(f(x))), r(f(f(f(f(x))))))))
g(x, g(f(x), g(f(f(x))), g(f(f(f(x))), v(x)))))
reduce(g, reverse([x, f(x), f(f(x)), f(f(f(x))), ..., v(x)]))
```
结合律



