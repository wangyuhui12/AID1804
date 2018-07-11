
### node properties
#### 属性
    fistChild
      描述：返回节点的第一个子节点
      语法：node node.fistChild

    lastChild
      描述：　返回指定节点的最后一个节点
      语法： node node.lastChild

    parentNode
      描述： 返回当前节点的父节点
      语法：node node.parentNode

    nextSibling
      描述： 返回当前节点的下一个兄弟节点（哥哥）
      Technical Details:
        A Node object, representing the next sibing of the node, or null if there is no next sibling.
      语法: node node.nextSibling

    previousSibling
      描述：　返回当前节点的上一个兄弟节点
        A Node object, representing the previous sibling of the node, or null if there is no previous sibling.
      语法： node node.previousSibling

### 方法

    replaceChild
      描述：节点替换
      语法：　node node.replaceChild(newChild, oldChild)

### 对象

####　方法
    getElementsByTagName()
    描述： 获取文档中指定标记名称所形成的集合（数组）
    语法： NodeList document.getElementsByTagName(TagName)

    createTextNode()
      描述: 创建文本节点
      语法：TextNode document.createTextNode(text)


### HTML DOM
    HTML DOM提供了针对处理HTML文档的API

#### 选取对象
    Element document.getElementById(string id)

    NodeList document.getElementsByTagName(string tagName)

    NodeList Element.getElementsByTagName(string tagName)

#### 属性控制
    １、对于单个单词的HTML标记属性即HTML　DOM对象属性；

    ２、对于合成词的HTML标记属性（如table标记的cellspcing、cellpadding属性)在HTML　DOM编程时，采用“驼峰标记法”命名（如cellPadding, cellSpacing)

    ３、对于HTML标记的class属性，　在HTML DOM编程时使用className取代；(因为class是ECMAScript中的关键字)

    ４、对于HTML标记的布尔属性（如单/复选框的checked、列表项的selected属性）在HTML　DOM编程时采用boolean类型表示。

    ５、在HTML DOM编程时，　某些HTML DOM对象有自己特有的属性/方法。


HTMLDocument对象

    getElementsByName()方法
      描述：获取文档中name属性相同的对象组成的集合（数组）
      语法：NodeList document.getElementsByName(string name)

#### 关于表单
    <form action="接受表单提交数据的页面的URL地址" method=''
