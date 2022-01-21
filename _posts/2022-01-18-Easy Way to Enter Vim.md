---
title: Easy way to Enter Vim
author: Heng
tags: [vim]
---

工作中存在大量文本编辑工作，提升文本编辑效率可以提高工作效率。我们需要一个文本编辑工具，它应具有以下特性：

- 全键盘，区域小
- 高效
- 天花板高
- 跨环境
- 可扩展

Vim 是不错的选择。说起 Vim，很多人会说学习曲线陡峭，但真的是这样吗？也许有一条更容易的路。

## 认识 Vim

查询维基百科：

```
vi 是一种计算机文本编辑器，由美国计算机科学家比尔·乔伊（Bill Joy）完成编写，并于 1976 年以 BSD 协议授权发布。

Vim 是从 vi 发展出来的一个文本编辑器。Vim 的第一个版本由布莱姆·米勒在 1991 年发布。最初的简称是 Vi IMitation，随着功能的不断增加，正式名称改成了 Vi IMproved。
```

在 [Vim Home](https://www.vim.org/about.php) 中：

```
What Is Vim?

Vim is a highly configurable text editor built to enable efficient text editing. It is an improved version of the vi editor distributed with most UNIX systems.

Vim is often called a "programmer's editor," and so useful for programming that many consider it an entire IDE. It's not just for programmers, though. Vim is perfect for all kinds of text editing, from composing email to editing configuration files.

Despite what the above comic suggests, Vim can be configured to work in a very simple (Notepad-like) way, called evim or Easy Vim.

What Vim Is Not?

Vim isn't an editor designed to hold its users' hands. It is a tool, the use of which must be learned.

Vim isn't a word processor. Although it can display text with various forms of highlighting and formatting, it isn't there to provide WYSIWYG editing of typeset documents. (It is great for editing TeX, though.)

* WYSIWYG: What You See Is What You Get
```

从官网的介绍中，我们认识了 Vim。

- 它是一个用来进行高效文本编辑的高度可配置的文本编辑器
- Vim 是工具，需要学习使用它
- Vim 被部分程序员作为 IDE 使用，但是它也可以作为简单的文本编辑软件使用。

Vim 的使用环境：

- Terminal, vim hello.txt
- GUI, gvim hello.txt
- Keymapping

## Let's Vim

我曾经有两次尝试使用 Vim，而又快速放弃的经历。回想起来，尝试的动机如上所述很明显，放弃的原因有很多，用错误的方式使用 Vim，没有正确的学习 Vim。接下来逐步介绍 Vim 的一些功能，主要为了尝试介绍一个进入 Vim 的简单途径。

### 先存活

**Enter**

先打开文件。

```
vim <filename>      在终端打开文件
vim -g or gvim      用GUI打开文件
```

**Out**

退出文件。

```
:q          退出
:q!         强制退出
:wq         保存退出

ZZ          保存退出
ZQ          强制退出
```

**Helper**

帮助文档

```
:vimtutor               快速入门
:help {string}          查看帮助文档
```

**Move**

移动键（Move），移动光标，或者定义操作（Operator）范围（Range）。

```
h       光标左移
j       光标下移
k       光标上移
l       光标右移

w       下一单词开头（空格或标点）
W       下一单词开头（空格）
e       下一单词尾部（空格或标点）
E       下一单词尾部（空格）
b       上一单词开头（空格）
B       上一单词尾部（空格）

$       行尾
0       硬行首（第一个字符）
^       软行首（第一个非空白字符）
-       上一行软行首
+       下一行软行首
_       当前行
gm      行中

|       10| 第 10 列

(       句首（句号分隔）
)       句尾（句号分隔）
{       段首（空行分隔）
}       段尾（空行分隔）

L       到屏幕下部
M       到屏幕中部
H       到屏幕下部

c-f     下一页
c-b     上一页
c-u     下半页
c-d     上半页

%       文件 10% 处
G       文件尾
gg      文件头

n       下一匹配单词
N       上一匹配单词

t       下一匹配字符前
T       上一匹配字符前
f       下一匹配字符
F       上一匹配字符
;       下一个 f/t/F/T 匹配
,       上一个 f/t/F/T 匹配

*       下一匹配
#       上一匹配

c-e     向上滚动一行
c-y     向下滚动一行
```

> 进入 Vim 后默认在 Normal 模式下

> Note: Range 在 Vim 中很重要！Char, Word, Line, Paragraph, Screen

**Ins**

插入键，执行命令且进入插入模式。

```
i       光标处插入
I       行首插入
a       光标后插入
A       行尾插入
o       向下打开一行
O       向上打开一行
C       改写到行尾
cc      改写当前行
s       替换字符串
S       替换当前行
gi      回到上次插入处

R       替换模式
```

> Note: 在 Insert 下 esc, ctrl-[ 回到 Normal

**Cmd**

命令键（Command），Normal 下执行的命令。

```
Y       复制行
yy      复制当前行
p       粘贴到光标后
P       粘贴到光标前
D       删除到行尾
dd      删除当前行
J       连接行
r       替换字符
x       删除光标字符
X       删除光标前字符
cc      修改当前行
<<      减少缩进当前行
>>      缩进当前行

v       选择字符，进入Visual
V       选择行，进入Visual
c-v     选择块，进入Visual

m       标记
.       重复命令
~       切换字符大小写

u       撤销
U       撤销当前行
c-r     重做

c-a     增加数字
c-x     减小数字

:       进入 Command Line

K       查询帮助
c-g     文件和当前光标信息
```

**Op**

操作键：行动，或者在光标和目标点之间的行为，目标点通过 Motion 指定。

```
d       删除
y       复制
c       修改

=       格式化
<       减少缩进
>       增加缩进
```

**Useing A Count**

多次操作

```
[count]{move}               移动多次
[count]{cmd}                命令执行，多次
{op}[count]{motion}         执行 op
[count]{op}{motion}         执行 op 多次
```

**Find**

查询  
:help search-commands

```
t           向前直到字符
T           向后直到字符
f           向前搜索字符
F           向后搜索字符
;           下一个 t,f,T,F 匹配
,           上一个 t,f,T,F 匹配

/           向前搜索
?           向后搜索
#           前一个标识符
*           下一个标识符

n           下一个匹配
N           上一个匹配
```

**Visual Mode**

可视模式，使用 v, V, c-v 进入。  
:help visual-mode

```
v               选择光标
V               行选择
c-v             块选择
```

**Text Objects**

文本对象命令只可以在 Visual 模式下或者为操作定义范围。
:help text-objects

```
a           an object
i           inner object
```

**Mark**

书签  
:help mark

```
:marks              显示所有书签
m{a-zA-Z}           记录当前光标位置到书签，小写文件内，大写全局
'a                  跳转到书签 a 所在行
`a                  跳转到书签 a 所在位置
`.                  跳转到上次编辑的行
```

**Substitue**

替换  
:help substitute

```
:[range]s/{pattern}/{string}/[flags] [count]    将 [range] 中 {pattern} 匹配到的结果替换为 {string}，

# range
.               当前行
%               当前文本
10,20           第 10 - 20 行

# flag
g               全部
c               需要确认

&               重复执行 :s
```

**Changing Case**

切换大小写  
:help case

```
~           转换字符大小写
g~          转换 motion 大小写
g~~         转换当前行大小写

gu                  改为小写
guu                 整行改为小写

gU                  改为小写
gUU                 整行改为大写
```

**Insert Mode**

在 Insert Mode 下的一些操作，避免切换到 Normal。

```
ctrl-p          提示菜单上一行
ctrl-n          提示菜单下一行
ctrl-d          向前缩进
ctrl-t          向后缩进
ctrl-w          删除单词
ctrl-f          自动缩进
ctrl-u          清空当前行
ctrl-v          插入
ctrl-r          插入寄存器中内容，或者其他内容
```

**Folding**

所有 fold 的 cmd 都以 z 开始  
:help fold-commands

```
za              切换折叠
zA              递归切换折叠
zc              折叠光标下代码
zC              折叠光标下所有代码
zo              打开一层
zO              打开光标下所有代码
```

### 配置

不建议拿别人的配置直接用。比较好的方式是把自己的 vim 知识持久化到配置文件，托管到 git，然后再 vim 的配置文件中写

```
# 根据情况修改
source ~/.vim/vim-init/init.vim
```

不断迭代自己的 vim 配置。

### 进阶

**Buffer**

多文件编辑

```
:buffers            已打开的文件
:ls                 已打开的文件
:files              已打开的文件
:bn                 下一个文件
:bp                 前一个文件
:bd                 关闭文件
:bd!                强制关闭文件
```

**Window**

对窗口的分隔和管理

```
:sp <filename>          上下切分并在新窗口打开文件
:vs <filename>          左右切分并在新窗口打开文件
c-w s                   上下切分
c-w v                   左右切分
c-w w                   循环切换到下一个
c-w W                   循环切换到上一个
c-w c                   关闭当前
c-w o                   改变其他
c-w h                   跳到左边
c-w j                   跳到下边
c-w k                   跳到上边
c-w l                   跳到右边
```

**Complex Repeat**

记录复杂操作，也被称为 macro。  
:help complex-repeat

```
q{0-9a-zA-Z"}           记录操作到命名寄存器
q                       结束记录
@{0-9a-zA-Z"}           播放寄存器宏
@@                      播放上一个宏
@:                      重复上一个 ex 命令（冒号命令）
```

**Register**

强大的寄存器功能，10 类 48 个寄存器，与 OP，Macro 组合使用。

```
:reg                      查看寄存器当前的值
"{register}               读取寄存器内容
```

**Plugin**

插件是 Vim 的核心功能，但本文不准备介绍，因为我也是一个菜鸟。

> Note: 使用 vim-plug 管理插件，[Vim Plug](https://github.com/junegunn/vim-plug)。

## 一些建议

- 可以先尝试在你熟悉的 IDE 中使用 vim 键位映射
- Vim 要学习，更要在使用中提高技艺，在使用中发现不足处，再去学习
- 不要冒进，避免被挫败感击败
- 一张 Vim Cheat Sheet for Programmers 也许可以帮助你
