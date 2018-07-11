sudo apt-get install openjdk-8-jdk


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
    (?:...)


#### Modifiers(修正符)

    i(ignore)     perform case-insensitive  matching
    g(global)     perform a global match
    m(multiline)     perform multiline  matching

#### test() method

    Tests for a match in a string. Returns true or false

    Syntax:
      bool  RegExpObject.test(string)

## DOM 编程
    JavaScript 由 ECMAScript(简称ES),DOM和BOM组成

    ECMAScript： 关键字、保留关键字、流程语句、数据类型、内置对象；

    DOM(Document Objec Model): 提供了操作HTML/XML文档相关的API(Application Programming Interface);

    DOM由DOM Core, HTML DOM和XML DOM组成；
      The DOM is a document model loaded in the browser and representing the document as a noded tree, where each node represents part of the document.

    DOM Core: 提供处理HTML和XML文档的API;

    HTML DOM: 提供处理HTML文档的API;

    XML DOM: 提供处理XML文档的API;

### 节点(DOM nodes)

    The entire document is a document node


#### nodeType(节点类型)
    1  ELEMENT_NODE(元素节点) HTML标记
    2  ATTRIBUTE_NODE(属性节点) HTML标记的属性
    3  TEXT_NODE(文本节点)  纯文本
    8  COMMENT_NODE(注释节点)  HTML注释
    9  DOCUMENT_NODE(文档节点)  整个HTML文档

#### 节点的关系

    子节点： 某一个节点是另外一个节点的直接下一级节点； 如<a><b>..</b></a>

    父节点: 一个节点是另一个节点的直接上一级节点；

    兄弟节点： 同一个父节点的所有子节点

#### Properties(属性)

    nodeName
      描述：获取节点的名称
      语法：string node.nodeName


    nodeValue
      描述：获取节点值
      语法：string node.nodeValue

    nodeType
      描述：获取节点的类型
      语法：　string node.nodeName

    childNodes
      描述：返回节点内所有的子节点形成的集合（数组）
      语法：NodeList node.childNodes

#### 方法

    appendChild()
    描述： 追加子节点
    语法：Node node.appendChild(Node)

    说明：　返回的是新插入的子节点

    removeChild()
    描述：删除子节点
    语法：Node  node.removeChild(node)

#### document Object (inherit Node)

#### Properties
    documentElement
    Descript：返回文档的根元素
    Syntax：Element document.documentElement

#### method
    getElementById()

    descript: 根据对象ID来获取元素
    Syntax: Element  document.getElementById()

    createElement()
    描述：创建元素节点
    语法： Element document.createElement(string tagName)

### Element　对象（继承自Node)
####　方法
    getAttribute()
    描述：获取属性值
    语法：　string Element.getAttribute(string name)

    setAttribute（）
    描述: 设置属性
    语法：　void Element.setAttribute(string name, string value)

    removeAttribute()
    描述：删除属性
    语法：void Element.removeAttribute(string name)

    hasAttribute()
    描述：　返回是否存在指定属性
    语法：　bool Element.hasAttribute(string name)

### Finding HTML ELements

    document.getElementById(id)
        Find an element by element id

    document.getElementByTagName(name)
        Find elements by tag name

    document.getElementsByClassName(name)
        Find elements by class name

### Changing HTML  Elements

    element.innerHTML = new html content
          Change the inner HTML　of an element

    element.attribute = new value
          Change the attribute value of an HTML element


### Changing HTML Content
    The eariest way to modify the content of an HTML element is by using the innerHTML property.
    To change the content of an HTML element, use this syntax:
      document.getElementById(id).innerHTML = new HTML

### Changing the value of an Attribute
    To change the value of an HTML attribute, use this syntax:
      document.getElementById(id).attribute = new value

### Changing HTML style
    To change the style of an HTML element, use the syntax:
        document.getElementById(id).style.property = new style

### Using Events
    The HTML DOM allows you to execute code when an event occurs.
    Events are generated by the browser when "things happen" to HTML elements:
      An element is clicked on
      The page has loaded
      Input fields are changed
