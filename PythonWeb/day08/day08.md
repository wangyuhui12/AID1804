#### map()
    描述： 数组成员依次调用回调函数，并且返回新数组
    语法： array object.mat(function(value[, index]){

})

## 内置对象
### Regular Expression对象（正则表达式对象）
#### 构建正则表达式对象

    直接量方式
      /正则表达式/修正符

    构造函数方式
      new RegExp('正则表达式', '修正符');

### 正则表达式
    A regular expression is a sequence of characters that forms a search pattern.

    When you search for data in a text, you can use this search pattern to describe what you are searching for.

    A regular expression can be a single character, or a more complicated pattern.

    Regular expressions can be used to perform all types of text search and text replace operations.

#### 元字符(metacharacter)
    .     Find a single character, except newline or line terminator(换行符和终止符)
    \d    Find a digit
    \D    Find a non-digit character
    \s    Find a whitespace character
    \S    Find a non-whitespace character
    \w    Find a word character  --->  [0-9a-zA-Z]
    \W    Find a non-word character

#### 量词(Quantifiers)
    n?    Matches any string that contains zero or one occurrences of n
    n*    matches any string that contains zero or more occurrences of n
    n+    Matches any string that contains at least one n
    {m}   occurrences of m
    {m,}  At least occuruences of m
    {m,n} m<=x<=n

#### 其他
    |  or
    ^  以指定字符开头
    $  以指定字符结尾
    [...]  表示在范围之内 [0-9]
    [^....] 表示不在范围之内， 如[^3-5]

#### 转义符(Escape character)

    \n   Find a new line character
    \r   Find a carriage return character
    \f   Find a form feed character(换页符)
    \\   反斜线
    \.   点.
    \*   星号
    \v   Find a vertical tab character(垂直制表符)
    \t   Find a tab character

#### 捕获组(Capture group)与非捕获组
    (...)
    (?...)


#### Modifiers(修正符)

    i     perform case-insensitive  matching
    g     perform a global match
    m     perform multiline  matching
