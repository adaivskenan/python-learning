## Python 基础
1. 以#开头的语句是注释，解释器会忽略掉注释。
2. 每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
3. Python程序是大小写敏感的

## 数据类型和变量

### 数据类型

1.整数

&emsp;&emsp;Python的整数没有大小限制

2.浮点数

&emsp;&emsp;Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。

3.字符串

 1. 字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等

 2. Python还允许用r''表示''内部的字符串默认不转义
 
 ```python
print(r'\\\t\\')
 ```

 3. 用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容

 ```python
print('''line1
 ... line2
 ... line3''')
 ```
4. 布尔值 

&emsp;&emsp;只能用True False表示，大小写敏感

5. 空值 None

6. bytes

- &emsp;&emsp;Python对bytes类型的数据用带b前缀的单引号或双引号表示

&emsp;&emsp;要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。

- 在bytes中，无法显示为ASCII字符的字节，用\x##显示。

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
```

&emsp;&emsp;如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

```python
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
``` 

### 变量

1. 大小写英文、数字和_的组合，且不能用数字开头。

2. Python是动态语言，声明变量无需使用类型限定。可以 a=10 也可以 a='adaivskenan'

3. 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错，JAVA就是一种静态语言。

### 常量

&emsp;&emsp;在Python中，通常用全部大写的变量名表示常量。Python根本没有任何机制保证常量不会被改变，这只是约定写法。

### 特殊的除法

- 在Python中，有两种除法，一种除法是/，/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数。

```python
>>> 10 / 3
3.3333333333333335

>>> 9 / 3
3.0
```

- 还有一种除法是//，称为地板除，两个整数的除法仍然是整数

```python
>>> 10 // 3
3
```

## 字符串和编码

&emsp;&emsp;**字符串也是一种数据类型，但是，字符串比较特殊的是还有一个编码问题。**

### ASCII编码的由来

&emsp;&emsp;因为计算机只能处理数字，如果要处理文本，就必须先把文本转换为数字才能处理。最早的计算机在设计时采用8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），如果要表示更大的整数，就必须用更多的字节。比如两个字节可以表示的最大整数是65535，4个字节可以表示的最大整数是4294967295。

&emsp;&emsp;由于计算机是美国人发明的，因此，最早只有127个字符被编码到计算机里，也就是大小写英文字母、数字和一些符号，这个编码表被称为ASCII编码，比如大写字母A的编码是65，小写字母z的编码是122。

### 乱码的终极方案--Unicode编码

&emsp;&emsp;但是要处理中文显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。日本把日文编到Shift_JIS里，韩国把韩文编到Euc-kr里，各国有各国的标准，就会不可避免地出现冲突，结果就是，在多语言混合的文本中，显示出来会有乱码。

&emsp;&emsp;因此，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问题了。Unicode标准也在不断发展，但最常用的是用两个字节表示一个字符（如果要用到非常偏僻的字符，就需要4个字节）。现代操作系统和大多数编程语言都直接支持Unicode。**ASCII编码和Unicode编码的区别：ASCII编码是1个字节，而Unicode编码通常是2个字节。**

> 字母A用ASCII编码是十进制的65，二进制的01000001；如果把ASCII编码的A用Unicode编码，只需要在前面补0就可以，因此，A的Unicode编码是00000000 01000001。

### 空间优化大师--UTF-8编码

&emsp;&emsp;如果统一成Unicode编码，乱码问题从此消失了。但是，如果你写的文本基本上全部是英文的话，用Unicode编码比ASCII编码需要多一倍的存储空间，在存储和传输上就十分不划算。

&emsp;&emsp;所以，本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的UTF-8编码。UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果你要传输的文本包含大量英文字符，用UTF-8编码就能节省空间：

### 内存和磁盘编码的编码策略

&emsp;&emsp;**在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码或者其它编码。**

&emsp;&emsp;比如：用记事本编辑的时候，从文件读取的UTF-8字符 被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件。

### Python的字符串

&emsp;&emsp;Python 3版本中,字符串是以Unicode编码的，也就是说，Python的字符串支持多语言

```python
>>> print('包含中文的str')
包含中文的str
```

&emsp;&emsp;由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```

- ord()

&emsp;&emsp;ord()函数获取字符的整数表示

```python
>>> ord('A')
65
# Python 2会报错    
>>> ord('中')
20013
```

- chr()

&emsp;&emsp;chr()函数把编码转换为对应的字符

```python
>>> chr(66)
'B'
>>> chr(25991)
'文'
```

- encode()

&emsp;&emsp;以Unicode表示的str通过encode()方法可以编码为指定的bytes

```python
>>> 'ABC'.encode('ascii')
b'ABC'
>>> '中文'.encode('utf-8')
b'\xe4\xb8\xad\xe6\x96\x87'
```

- decode()

&emsp;&emsp;如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：

```python
>>> b'ABC'.decode('ascii')
'ABC'
>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

- len()

&emsp;&emsp;函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数

```python
>>> len('ABC')
3
>>> len('中文')
2
>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
```

- format()

```python
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'
```

- %格式化与%d %f %s %x

```python
>>> 'Hello, %s' % 'world'
'Hello, world'
>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'
# %转义
>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'
# 万能的%s
>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
# 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
>>> '%2d-%02d' % (3, 1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'
```

### 编码对比 ：python2 VS. python3

- python2打印‘中文’异常
```python
#!/usr/bin/env python

print('中文')
```

```python
File "./print2.py", line 3
# SyntaxError: Non-ASCII character '\xe4' in file ./print2.py on line 3, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
```

- python2增加编码说明打印‘中文’正常

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
print('中文')
```

```python
chmod a+x print2-1.py
./print2-1.py
中文
```

- python3无需设置编码格式也可以正常打印

```python
#!/usr/bin/env python3

print('中文')
```

## lis和tuple

