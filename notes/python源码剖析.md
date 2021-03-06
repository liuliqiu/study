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


### 常用指令列表

| 指令               | 作用                                       |
| ---------------- | ---------------------------------------- |
| LOAD_CONST       | 将常量压入栈                                   |
| STORE_NAME       | 将栈顶部的值放入locals字典，key为name。               |
| BUILD_MAP        | 新建一个dict对象并压入栈                           |
| BUILD_LIST       | 新建一个list对象并压入栈                           |
| RETURN_VALUE     | 返回栈顶的值                                   |
| STORE_MAP        | 以栈顶值为key，第二个值为value，放入第三个值的字典            |
| LOAD_NAME        | 先后从locals、globals、builtins中查找name，然后压入栈  |
| COMPARE_OP       | 使用参数代表的比较运算比较两个栈顶值，结果压入栈。                |
| POP_JUMP_IF_TRUE | 根据弹出的栈顶元素的布尔值决定是否跳转                      |
| JUMP_ABSOLUTE    | 直接跳转到参数指定的指令位置                           |
| SETUP_LOOP       | 设置循环开始，以SETUP_LOOP，当前stack顶位置, 循环结束位置为参数新建PyTryBlock，然后压入frame.f_blockstack |
| GET_ITER         | 对栈顶值用PyObject_GetIter，获取迭代器取代当前栈顶的值      |
| FOR_ITER         | 获取栈顶迭代器的迭代值然后压入栈顶，失败时弹出栈顶迭代器，然后跳到参数指定的指令处 |
| POP_BLOCK        | 从frame.f_blockstack弹出顶部的PyTryBlock，然后从栈顶弹出值，直到栈的栈顶位置恢复到PyTryBlock设置的栈顶位置 |
| BREAK_BLOCK      | 设置 why 为 WHY_BREAK 跳到fast_block_end处，弹出f_blockstack顶部的SETUP_LOOP的PyTryBlock，然后根据其保存的栈顶位置恢复栈状态 |
| RAISE_VARARGS    | 根据参数获取栈顶的值设置异常信息，返回WHY_EXCEPTION         |
| SETUP_EXCEPT     |                                          |
| SETUP_FINALLY    |                                          |
| END_FINALLY      |                                          |
| LOAD_FAST        |                                          |
| STORT_FAST       |                                          |
| STORE_DEREF      | 将栈顶的值放入 co_freevals 中对应的PyCell对象中        |
| LOAD_DEREF       |                                          |
| LOAD_CLOSURE     | 取参数对应位置的PyCell对象，压入栈                     |
| MAKE_CLOSURE     | 弹出栈顶的PyCodeObject创建一个函数，然后弹出栈顶的tuple，设置为closure |
| BUILD_CLASS      | 弹出位于栈顶的前三个值类名、基类列表、属性字典构建一个class对象放在栈顶   |
| LOAD_ATTR        | 将栈顶元素的指定属性放在栈顶                           |
|                  |                                          |


### 循环
```
SETUP_LOOP
// init 代码，将需要迭代的对象压入栈顶
GET_ITER
FOR_ITER (postion of POP_BLOCK)
// loop 代码
JUMP_ABSOLUTE (position of FOR_ITER)
POP_BLOCK
```

### 异常处理
python会在进入异常处理结构时使用 SETUP_EXCEPT 和 SETUP_FINALLY 新建一个PyTryBlock压入frame.f_blockstack。

发生异常时，指令会调用PyErr_SetString 等设置tstate中的异常信息，并且在switch中设置 x 为NULL ,why为WHY_EXCEPTION，在PyTraceBack_Here中使用PyTracebackObject纪录当前frame信息放到tstate.curexc_traceback中。

虚拟机会从当前PyFramObject对象的f_blockstack中弹出一个PyTryBlock，然后通过PyErr_Fetch获取当前线程对象中存储的最新异常对象和traceback对象,然后就 traceback对象， 值，类型压入栈中。将why设置为WHY_NOT，然后跳转到异常处理代码。

except ，会使用 COMARE_OP 带参数10 ，比较异常的类型，成功时执行异常处理代码然后跳过END_FINNALY指令，失败时直接跳到 END_FINNALY指令。
END_FINNALY指令会重新抛出异常
finnaly时会执行处理代码然后执行END_FINNALY指令

如果异常在当前frame没有处理，会返回调用它的上一级frame，按同样的方式寻找except和finally处理,直到最外层还没有被处理的话，python 会用默认的PyErr_Print打印错误信息。

### 参数传递

函数默认值：MAKE_FUNCTION的时候，在函数压入栈前会将默认参数压入栈，然后会用默认参数构造一个tuple赋值给func的func_defaults字段。因为函数的变量名都是固定的，所以tuple会对应最后的几个参数名。
然后会在函数执行时先使用传递的参数填充localplus，之后会用默认参数填充没有传递的参数。
如果函数还有拓展位置参数和拓展健函数会放在localplus中其他参数的后面。

Python虚拟机执行 py文件时，f_locals 和 f_globals指向的是同一个PyDictObject。
但是调用函数中使用PyFrame_New 创建一个新的PyFrameObject对象时，f_locals会指向NULL。
这时局域变量会利用LOAD_FAST和STORE_FAST来操作。因为函数中的局部变量总是固定不变的，所以在编译时就能确定局部变量使用内存的位置，也能确定访问局部变量的字节码指令应该如何访问内存。

### 闭包

co_cellvars 通常是一个tuple，保存嵌套的作用域中使用的变量名集合；
co_freevars 通常是一个tuple，保存使用了的外层作用域中的变量名集合；
localplus中除了保存局部变量和栈，还有cellvars和freevars。

![localplus内存分布](https://img3.doubanio.com/view/ark_works_pic/common-largeshow/public/178704.jpg)

PyCellObject 仅仅是PyObject对象的一层通用引用包装
```c
typedef struct {
  PyObject_HEAD
  PyObject* ob_ref;
} PyCellObject;
```

外部函数会用STORE_DEREF指令设置cellvars对象，生成函数对象时会从cellvars中取出cell生成一个tuple作为函数的closure。开始执行函数时会从closure中取出cell放入freevars中。然后就可以在内部函数中使用LOAD_DEREF使用外部函数中的变量了。

### 对象模型

Python 2.2之前，Python中的内置type，是不能被继承的。因为没有在type中寻找某个属性的机制。这就是old style class。
Python 2.2 中统一了类型机制，称之为new style class机制。

metaclass对象：type

Python 2.2 开始，Python在启动时，会调用_Py_ReadyTypes然后调用PyType_Ready对类型系统进行初始化、进行填充tp_dict等操作。
获得基类tp_base，没有的话设置为object。
然后看基类是否已经出事话，没有的话先初始化基类。
然后如果没有ob_type则设置为基类的ob_type。
然后处理类型的基类列表tp_bases。
最后开始填充tp_dict。

slot，在Python内部slot可以视为PyTypeObject中定义的操作，slot还包含一些其他信息。
```c
typedef struct wrapperbase slotdef;

struct wrapperbase{
  char *name;  // 操作对应的名称
  int offset;  // 函数地址在 PyHeapTypeObject中的偏移量
  void *function;  // 
  wrapperfunc wrapper;
  char *doc;
  int flags;
  PyObject *name_strobj;
}
```
```c
typedef struct _heaptypeobject{
  PyTypeObject ht_type;
  PyNumberMethods as_number;
  PyMappingMethods as_mapping;
  PySequenceMethods as_sequence;
  PyBufferProcs as_buffer;
  PyObject *ht_name, *ht_slots;
} PyHeapTypeObejct;
```
PyHeapTypeObject的第一个域就是PyTypeObject，所以在PyTypeObject的偏移量就是在PyHeapTypeObject的偏移量。

slotdefs 中有可能同一个操作名有可能对应不同操作。所以在init_slotdefs中会用offset信息对slot进行排序。

slot和PyWrapperDescObject
```c
#define PyDescr_COMMON \
    PyObject_HEAD \
    PyTypeObject *d_type; \
    PyObject *d_name

typedef struct {
  PyDescr_COMMON;
  struct wrapperbase *d_base;
  void *d_wrapped;
} PyWrapperDescrObject;
```
PyWrapperDescrObject中的d_wrapped就是操作对应的指针，slot 放在d_base中。
tp_dict中保存 操作名道descriptord的关联。
slotptr 使用type和offset获得操作的真实函数指针。

初始化时，如果自定义的类有重写默认属性，Python会在fixup_slot_dispatchers中找到type中的tp_
方法，替换为slot中的 slot_tp_方法，slot方法中查找对应的属性，然后执行。
确定MRO (method resolve order)
函数 mro_internal
从头到尾访问类的基类列表，将每个基类的mro列表中的class对象放倒自己的基类列表中。
确定了mro列表后，会遍历mro列表，将class对象没有设置而基类有设置的操作拷贝到类class对象中。
然后Python会填充基类的子类列表tp_subclasses

### 用户自定义class
Python定义class时，实际上构造了一个function，然后调用函数返回函数的locals变量字典作为成员字典，然后使用类名、基类tuple、属性字典构造一个class对象。
构造class对象时，会先从属性字典中查找__metaclass__ ，如果没有获取到则取第一个基类的type作为该class的metaclass。
获得metaclass之后，build_class会通过PyObject_CallFunctionObjArgs调用metaclass，完成class对象的创建。

metaclass为type时会调用type_call，然后会调用type_new方法。分配PyHeapTypeObject+PyMemberDef的内存空间、初始化tp_dict、初始化各个属性。
会设置 tp_basesize为base.basesize+2 * sizeof(PyObject * )，2个PyObject为tp_dictoffset和tp_weaklistoffset。会设置tp_itemsize为base.tp_itemsize

Python通过调用class对象来创建instance对象。调用过程中会通过tp_call调用到tp_new，然后调用到object_new来创建instance对象。
其中会掉调用PyType_GenericAlloc申请 tp_basesize + tp_itemsize的内存空间。
然后会调用tp_init初始化便利。
可以通过添加属性 __new__ 和 __init__ 来添加slot覆盖tp_new 和 tp_init的调用。

PyObject_GenericGetAttr
通过tp_dictoffset找到__dict__ 

PyObject_GenericSetAttr会将属性设置在__dict__中

对于一个Python中的对象obj，如果obj.__class__中存在__get__，__set__，__del__ 三个操作，那么obj就可称为Python中的一个descriptor。

data descriptor：定义了 `__get__`，`__set__`的descriptor
no data descriptor：只定义了`__get__`的descriptor

Python会按instance属性、class属性的顺序选择属性。
如果在class属性中发现同名的 data descriptor，那么该descriptor 会优先于instance 属性被选择。
Python中的函数属性实际上是一个descriptor，func_descr_get，在其中会调用PyMethod_New绑定函数和instance和class。
PyObjectMethod调用时会将instance对象替换掉栈中的pfunc，实现增加一个参数。
staticmethod会生成PyStaticMethod_Type类型的descriptor。


