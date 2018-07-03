##复习
    1、img 相对路径 绝对路径  
    2、 a href  target 锚点的用法  
    3、table  tr  td colspan  rowspan  
    4、表单 form  
        表单标签<input type="" name="" value="">
        text
        password
        radio
        checkbox
        hidden
        file
        submit
        reset
        button
-------------------------------------------------------------------
####表单标签
    input标签 9个
    非input标签 2个
     1、文本域
      <textarea>大量的文本</textarea>
       rows cols是文本区域内可见的宽度和高度
       原本的意思，每一行显示多少个字符，显示多少行字符。
       但是由于系统编码不同，浏览器解析不同，导致显示字符数差异很大

 ####下拉列表（下拉选）
    <select>
        <option></option>
        ...
    </select>

  总结：
  1、当option没有value属性
    select标签的value值是选中的那个option标签的内容
  2、当option有value属性
    select 标签的value值是选中的那个option标签的value值

 ####表单标签总结：
      1、只有含有name属性的表单标签才可以提交数据  
      2、radio和checkbox必须设置value属性才可以提交数据  
      3、text的value是直接设置值  
        placeholder设置提示  
      4、radio和checkbox默认选中是checked  
      5、select默认选中是selected  

###css层叠样式表
####内联样式
      <span style="color:#f00;font-size:30px">内联样式的使用</span>
      内联样式在标签的style属性中写样式
      内联样式使用不多  
       * 不能重写  
       * 内联样式优先级最高  
       项目代码完全不适用内联， 只有在学习和调试过程中
####内部样式
    在head标签中，写style标签
    在style标签内部写样式
    选择器{
        属性： 值；
     }
     样式代码可以重用，但只能在本html中重用，在项目中使用不多
     
 [百度](http://baidu.com)
 ![01](./01.jpg)
 ####外部样式
 * 创建一个 .css文件
 * 
 
 ####创建样式表的规则特性
 * 层叠效果     
      >多个样式作用在同一个标签上
      如果样式属性不重复
      那么这些样式都会产生效果
 * 继承  
    * 父级元素的样式会继承给子元素
    * 子元素可以重新写样式，不适用父级元素的样式
 * 优先级
    * 优先级最低的：浏览器默认样式
    * 优先级最高的 内联样式
    
    * 内部样式和外部样式--就近优先
    * 以被影响标签为基准， 哪个样式离这个标签近就使用哪个样式的效果
    
 ####上午小作业
    1、css3中使用方式
    2、css层叠
    3、css继承
    4、优先级












