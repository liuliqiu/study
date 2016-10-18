## 源代码的组织

| 文件夹     | 主要用途                        | 源代码  |
| ------- | --------------------------- | ---- |
| Include | Python提供的所有头文件              | 重点部分 |
| Python  | Compiler和执行引擎部分             | 重点部分 |
| Objects | 所有Python的内建对象               | 重点部分 |
| Parser  | Python解释器中的Scanner和Parser部分 |      |
| Modules | 所有用C语言编写的模块                 |      |
| Lib     | Python语言编写的Python标准库        |      |

## 内建对象

```c
typedef struct _typeobject {
    PyObject_VAR_HEAD
    char *tp_name;
    int tp_basicsize, tp_itemsize;
    destructor tp_dealloc;
    printfunc tp_print;
    
    hashfunc tp_hash;
    ternaryfunc tp_call;
}
#define PyObject_HEAD       \
    int ob_refcnt;          \
    struct _typeobject *ob_type;

#define PyObject_VAR_HEAD 	\
    PyObject_HEAD           \
    int ob_size;
```
tp_as_number
tp_as_sequence
tp_as_mapping

COL (Concrete Object Layer)

| python类型 | ob_type           |
| -------- | ----------------- |
| object   | PyBaseObject_Type |
| type     | PyType_Type       |
| int      | PyInt_Type        |


### int
```c
typedef struct {
    PyObject_HEAD
    long ob_ival;
}
```

##### 小整数对象池 

small_ints: [-5, 257)，使用时直接根据索引获取整数对象，并且不释放小整数的内存

```c
static PyIntObject *small_ints[NSMALLNEGINTS + NSMALLPOSINTS];
```

##### 通用整数对象池
使用block 维护一个int对象数组， block_list维护一个block单项链表
另外使用free_list维护一个int对象链表，其中使用未使用int对象的 ob_type 作为指向下一个int对象的指针
需要使用整数对象时从free_list中寻找可用int对象。没找到时初始化一个block然后加入block_list链表，然后将block中所有int对象加入free_list链表
整数对象释放内存时，将int对象加入free_list链表

### long
python 使用 带有一个 digit 数组的可变对象来表示一个long类型对象。
其中 ob_size的绝对值 表示数组的长度，同时ob_size的符号表示long对象的符号。
digit 由机器在编译时决定，digit 为32位时 digit 数组的进制位 2 ^ 30 
digit 位 16 位时 digit数组的进制位 2 ^ 15

```c
// value = SUM(for i=0 through abs(ob_size)-1) ob_digit[i] * 2**(SHIFT*i)
struct _longobject {
  PyObject_VAR_HEAD
  digit ob_digit[1];
}
```

### python3 int
使用python2中long的方式来表示对象
同时使用small_ints来缓存小整数，并且移除了python2种的 block_list, free_list 机制，使用python通用的内存池来缓存大整数

### str
```c
typedef struct {
    PyObject_VAR_HEAD;
    long ob_shash;   // hash值
    int ob_sstate;   // intern
    char ob_sval[1];
} PyStringObject;
```
##### 字符缓冲池
```c
#define UCHAR_MAX 0xff
static PyStringObject *characters[UCHAR_MAX + 1];
```

##### intern
python 编译时会对 看起来像标识符的字符串intern， 运行时长度为0或者1的字符串会被intern，其他字符串可以调用内置的intern函数来intern
被intern 的对象在整个python的运行期间，系统中都只有唯一的一个对象。
使用dict 保存intern的对象

### list
```c
typedef struct {
    PyObject_VAR_HEAD
    PyObject **ob_item;
    int allocated;      // 可容纳的元素的总数
}PyListObject;
```

### free_lists, num_free_lists
对于 PyListObject, PyDictObject, PyFrameObject 等对象
Python 使用了free_list 的重用对象机制。
维护本应该销毁的对象，供创建新对象时使用。
对于PyListObject但是ob_item指向的空间会被销毁。

### dict
```c
typedef struct {
    Py_ssize_t me_hash;
    PyObject *me_key;
    PyObject *me_value;
} PyDictEntry;

#define PyDict_MINSIZE 8
typedef struct _dictobject PyDictObject;
struct _dictobject { 
    PyObject_HEAD
    Py_ssize_t ma_fill;    // 元素个数: Active + Dummy
    Py_ssize_t ma_used;    // 元素个数: Active
    Py_ssize_t ma_mask;
    PyDictEntry *ma_table;
    PyDictEntry *(*ma_lookup)(PyDictObject *mp, PyObject *key, long hash);
    PyDictEntry ma_smalltable[PyDict_MINSIZE];
};
```

## 编译与执行
编译时一个名字空间编译成一个PyCodeObject对象，然后写入pyc文件。执行时从Pyc文件中读入PyCodeObject对象，初始化一个PyFrameObject对象。PyFrameObject对象中保存运行时的stack、locals、globals、builtins等数据。

### PyCodeObject对象
```c
typedef struct {
    PyObject_HEAD
    int co_argcount; /* #arguments, except *args */
    int co_nlocals; /* #local variables */
    int co_stacksize; /* #entries needed for evaluation stack */
    int co_flags;
    PyObject *co_code; /* string, instruction opcodes */
    PyObject *co_consts; /* list (constants used) */
    PyObject *co_names; /* list of strings (names used) */
    PyObject *co_varnames; /* tuple of strings (local variable used) */
    PyObject *co_freevars; /* tuple of strings (free variable used) */
    PyObject *co_cellvars; /* tuple of strings (cell variable used) */
    PyObject *co_filename; /* string (where it was loaded from) */
    PyObject *co_name; /* string (name, for reference) */
    int co_firstlineno; /* first source line number */
    PyObject *co_lnotab; /* string (encoding addr<->lineno mapping) */
    void *co_zombiefram; /* for optimization only */
} PyCodeObject;
```

### marshal
```c
typedef struct {
    FILE *fp;
    int error;
    int depth;
    PyObject *str;
    char *ptr;
    char *end;
    PyObject *strings; /* dict on marshal, list on unmarshal */
    int version;
} WFILE;
```

将string写入pyc文件时，如果是intern字符串，第一次写入时写入intern 和 字符串，之后的写入stringref 和 这是文件中第几个intern字符串。不是intern字符串时写入 string和字符串。

python 内置模块 dis 用于解析code对象

### PyFrameObject 对象

初始化时，会计算locals、cellvars、freevals、stack占用的长度，分配多余的内存空间，这些空间用f_localsplus访问。
其中stack放在对象的最后面。
f_localsplus重的locals 时为了提高虚拟机的访问速度的。
初始化时会把f.f_lasti 设为 -1。
执行时会用变量opcode、oparg保存当前指令和参数。next_instr指向下一条指令、stack_pointer指向栈顶。

### 运行
指令跳跃
通过判断直接判断下条指令是否为某条特殊指令，如果为真则通过goto直接跳转到下条指令，加快两条经常连续执行的指令的执行速度。
通过宏 PREDICT 进行快速跳转
通过宏PREDICTED 和 PREDICTED_WITH_ARG 定义加入用于快速的定位


### 常用指令列表ßßßßßßßßßßßßßß

| 指令               | 作用                                      |
| ---------------- | --------------------------------------- |
| LOAD_CONST       | 将常量压入栈                                  |
| STORE_NAME       | 将栈顶部的值放入locals字典，key为name。              |
| BUILD_MAP        | 新建一个dict对象并压入栈                          |
| BUILD_LIST       | 新建一个list对象并压入栈                          |
| RETURN_VALUE     | 返回栈顶的值                                  |
| STORE_MAP        | 以栈顶值为key，第二个值为value，放入第三个值的字典           |
| LOAD_NAME        | 先后从locals、globals、builtins中查找name，然后压入栈 |
| COMPARE_OP       | 使用参数代表的比较运算比较两个栈顶值，结果压入栈。               |
| POP_JUMP_IF_TRUE | 根据弹出的栈顶元素的布尔值决定是否跳转                     |
|                  |                                         |
|                  |                                         |











