### 循环语句
#### for 语句
    for(expr1;expr2;expr3){
        .....
    }
    说明：
      expr1, 在循环之前无条件的执行一次，一般用于变量初始化；

      expr2, 在每次循环前执行一次， 用来判断能否进入循环体；

      expr3, 在循环后执行一次，　一般用于步长的计算；

      for语句的表达式可以省略其中任何一个或全部；

      for(n=1; n<=10; n++){
        alert("Hello world!");
      }

#### for...in语句
    for(key in array){
      ...
      ...
    }

#### with 语句
    with 语句的作用是将代码的作用于设置到一个特定的对象中。

    ex:
    var qs = location.search.substring(1);
    var hostName = location.hostName;
    var url = location.href;
    相当于：
    with(location){
      var qs = search.substring(1);
      var hostName = hostName;
      var url = href;
    }
    说明：　
      由于大量使用with语句会导致性能下降，同时也会给调试代码造成困难，因此，在开发大型应用程序时，　不建议使用with语句。

#### while　语句
    while(条件表达式){
      ...
      ...
    }
    死循环：　条件永远为真的循环语句。

    for 语句和while语句同属“当型循环(先判断后执行)”，所以可以互换；

#### break 语句　: 结束switch及循环语句

#### continue　语句：　跳过当前的循环而进行下一次的循环

    &gt;      >
    &lt;      <
    &amp;     &
    &#39;     '
    &apos;    "
    &nbsp;   not breaking space

### 内置对象
#### 构建String对象
    １、直接量方式
      'string' 或者　"String"

    ２、构建函数方式
      new String('string')

#### 属性
    length
    描述：　返回字符串的长度

    语法：　int object.length

#### 方法

    toLowerCase()
    描述：　将字符转换成小写字母
    语法： string object.toLowerCase(void)

    toUperCase()
    描述：将字符转换大写字母
    语法： string object.toUpperCase(void)

    substr()
    描述：Extracts the characters from a string, beginning at a specified start position, and through the specified number of character截取字符串
    语法： string object.substr(int start[, int length])
    object.substr(index, length)
    说明：
      1、 字符串从0开始编号；
      2、 如果省略length参数，则返回到字符串结尾之间的字符
      3、 如果start参数为负数， 则倒数；

    substring
    描述： 截取字符串
    语法：string object.substring(int start[, int end])
    说明：
      1、返回的字符串包含起始位， 不包含结束位；
      2、如果省略end参数， 则返回到字符串结尾之间的字符。

    indexOf
    描述： 返回字符串第一次出现的位置，如果没有出现则返回-1
    语法：int object.indexOf(string)

    lastIndexOf
    描述：　返回字符串最后一次出现的位置，如果没有则返回-1
    语法：int object.lastIndexOf(string)

    UUID,　通用唯一识别码，　其形态为8-4-4-4-12, 其作用是为保证文件名的唯一性。

    webp格式是Google推出的一种图像格式，　其仅被Google　Chrome浏览器支持，　其特点是相比jpeg文件来说，字节数更小

    京东商品展示图片采用动态缩放实现的(lua)

    replace()　方法
    描述：字符串替换
    语法：
    string object.replace(string search, string replacement)
    string object.replace(object RegExp, string replacement)

    ES6　新增方法
      trim()
      描述删除第一个字符之前及最后一个字符之后的空白
      语法：
        string object.trim(void)

    startWith()
    描述：检测字符是否以指定字符开头
    语法： bool  object.startsWith(string)

    endsWith()
    描述： 检测字符是否以指定字符结尾
    语法：bool object.endsWith(string)

#### Math对象
    Math对象是一个静态对象。
    属性：　
      Math.PI,圆周率

      Math.SQRT2
        2的平方根
    方法：
      Math.ceil()
      描述： 舍一取整
      语法：number Math.ceil(number)

      Math.floor()

      Math.pow()
      描述：幂运算
      语法：number Math.pow(base, exp)

      Math.sqrt()
      描述：　平方根
      语法： number Math.sqrt(number)

      Math.min()
      描述：最小值
      语法：number Math.min(num1, num2, ...)

      Math.max()
      描述： 最大值
      语法：number Math.max(num1, num2, ...)

      Math.random()
      描述：产生介于0~1之间的随机数(0<=X<1)  >
      语法： number Math.random(void)

      Math.round()

      描述： 四舍五入(仅保留到整数位置)

      语法：number Math.round(number)

#### Date对象
    构建Date对象

      new Date()

####　方法
    getYear()
    描述：　获取年份从公元1900年到现在经历的年份
    语法：int object.getYear(void)

    getFullYear()
    描述：获取年份
    语法： int object.getFullYear(void)

    getMonth()
    描述： 获取月份（取值范围为0-11）
    语法： int object.getMonth(void)

    getDate()
    描述： 获取日期（几号）
    语法：int object.getDate(void)

    getDay()
    描述：　获取星期的第几天（０为星期日，　以此类推）
    语法：　int object.getDay(void)

    getHours()
    描述：　获取小时
    语法： int object.getHours(void)

    getMinutes()
    描述: 获取分钟数
    语法： int object.getMinutes(void)

    getTime()
    描述： 返回从公元1970年到现在的毫秒数
    语法： int object.getTime(void)
    toUTCString()/toGMTString()
    描述: 将日期转换成UTC/GMT格式
    语法：string object.toUTCString(void)
      string object.toGMTString(void)

    ES6 新增的方法

      Date.now() 静态方法
      描述：返回从公元1970年到现在的毫秒数
      语法：int Date.now(void)
      说明：该方法为静态方法

#### Array对象

#### 方法
    unshift()
    描述： 在数组的开头添加一个或个成员，并返回数组的新长度
    语法：int object.unshift(value, ...)

    shift()
    描述：　删除数组的第一个成员，　并且返回该成员
    语法：mixed object.shift(void)

    push()
    描述：在数组的末尾添加一个或多个成员， 并返回数组的新长度
    语法：int object.push(value, ...)

    pop()

#### 数组遍历 --- forEach()语句
    object.forEach(function(value[, index]){

    });
