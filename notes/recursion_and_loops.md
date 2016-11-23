# 递归 Recursion
递归是指在函数的定义中使用函数自身的方法
递归：有递有归
> 计算理论可以证明递归的作用可以完全替换循环
> 正则表达式的计算能力不如上下文无关文法

有穷自动机: 关于存储量极其有限的计算机的很好的模型。
上下文无关法: 

# 尾调用
尾调用是指一个函数里的最后一个动作是一个函数调用的情形：即这个调用的返回值直接被当前函数返回的情形。 

# 循环

# 有穷自动机 - 正则语言

有穷自动机  M:(Q, ∑, δ, q, F)
状态集      Q:有穷集合
输入字母表  ∑:有穷集合
动作规则    δ:Q×∑→Q
起始状态    q:q∈Q
接受状态集  F:F是Q的子集1

M接受w      : w = w1 w2 ... wn : 
机器M的语言 A:{w|M接受w}, 机器M接受的全部字符串集
如果一个语言被一台有穷自动机识别，则称它是正则语言

确定性有穷自动机    DFA
非确定性有穷自动机  NFA
每一台NFA都可以转换成一台等价的DFA
NFA 和 DFA 的区别在于动作规则不同 NFA: Q×∑→P(Q), P表示幂集

# 上下文无关法则
下推自动机


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


[1]: https://zh.wikipedia.org/wiki/%E9%80%92%E5%BD%92_(%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6) "递归"
