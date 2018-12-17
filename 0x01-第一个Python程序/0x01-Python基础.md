## Python简介
    Python是著名的“龟叔”Guido van Rossum在1989年发布的，Python是一门解释行语言。

### Python适合开发哪些类型的应用呢？

1. 首选是网络应用，包括网站、后台服务等等；

2. 其次是许多日常需要的小工具，包括系统管理员需要的脚本任务等等；

3. 另外就是把其他语言开发的程序再包装起来，方便使用。

### Python的缺点。

1. 第一个缺点就是运行速度慢，和C程序相比非常慢，因为Python是解释型语言，你的代码在执行时会一行一行地翻译成CPU能理解的机器码，这个翻译过程非常耗时，所以很慢。而C程序是运行前直接编译成CPU能执行的机器码，所以非常快。

2. 第二个缺点就是代码不能加密。如果要发布你的Python程序，实际上就是发布源代码，这一点跟C语言不同，C语言不用发布源代码，只需要把编译后的机器码（也就是你在Windows上常见的xxx.exe文件）发布出去。要从机器码反推出C代码是不可能的，所以，凡是编译型的语言，都没有这个问题，而解释型的语言，则必须把源码发布出去。


## Python安装

如果你正在使用Mac，系统是OS X>=10.9，那么系统自带的Python版本是2.7。安装最新的Python 3.7方法如下：（需要提前安装好Homebrew）运行Python时，请打开终端，然后运行python3。

```shell
brew install python3
```
### python多版本

```shell
//进入python 2.* 版本
python
//进入python 3.* 版本
python3
```

## Python解释器

Python有多种解释器，其中CPython是默认的解释器

## 命令行模式 VS. Python交互模式

### 命令行模式

在命令行模式下，可以执行python进入Python交互式环境，也可以执行python hello.py运行一个.py文件

### Python交互模式

在命令行模式下敲命令python，就看到类似如下的一堆文本输出，然后就进入到Python交互模式，它的提示符是>>>。在Python交互模式下输入exit()或者quit()并回车或者 Ctrl-D，就退出了Python交互模式，并回到命令行模式

### PK结果

Python交互式环境会把每一行Python代码的结果自动打印出来，但是，直接运行Python代码却不会。Python交互模式的代码是输入一行，执行一行，而命令行模式下直接运行.py文件是一次性执行该文件内的所有代码。可见，Python交互模式主要是为了调试Python代码用的，也便于初学者学习，它不是正式运行Python代码的环境！

## 如何直接运行Python程序

文件的开头直接输入运行环境即可

```python
#!/usr/bin/env python3
```

## 参考文献
[廖雪峰的Python教程][1]


  [1]: https://www.liaoxuefeng.com