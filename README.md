##关于CODER

`Coder是一个程序员社区的源码，目前社区还在开发中，开发进度也会和github同步`

`目前你可以下载到得可运行的版本是Coder社区的一个子系统，也就是博客系统，应用名为blog`


###**事实上事情应该是这样的：**
-------
刚开始的时候，我还在自己的小站里欢乐的整理这几年python上面的收获，**说时迟，那时快！**我的手机收到了aliyun的短信，意思就是说数据即将回收了，需要续费，可不等我打开续费窗口，aliyun就以迅雷不及掩耳盗铃的速度释放掉了我的服务器，然后才发现，今天月初，短信服务上个月被我关闭了一个月，以至于手机短信有了大概36个小时的延时，于是，我准备重新写一个blog自己用，写到一半，发现这么好的东西应该给大家一起用，于是就开始开发网络版的。

最早的时候，我准备直接用wordpress直接在我的新SERVER上部署一个就可以了，可是我对于PHP向来都是深恶痛绝的（尽管PHP本身很优秀且没有招惹我，但是不对脾气，没有办法）。

后来决定还是用python来自己实现一个，而且发现MarkDown的效率还是比较高的，且有点小文艺，于是就准备用MarkDown来记录，那么就有了第一个需要解决的问题：
> 怎么在HTML中嵌入MarkDown并集成大量的Jvascript代码，让他强大如同Desktop Client一般！

解决了MarkDown的问题，基本上就成功了一半了，然后就是如何进行分类，本着自由至上的原则，我决定还是使用Meta对每一篇文章进行标记，然后在进行数据的分析和归档。

最后，还需要进行用户的认证，这也没什么好说的。

###**怎么使用？**
------------
完全依据MarkDown语法打造的编辑器，只要你熟悉MarkDown即可快乐的书写了！这里重点介绍一下几个快捷键：
>	快速插入日期 **Ctrl+D**
>	选中文字加粗**Ctrl+B**
>	选中文字变为斜体**Ctrl+I**
>	无序列表 **Ctrl+U**
>	撤销 **Ctrl+Z**
>	插入分割线 **Ctrl+H**

###关于图片和评论
---
推荐用户将图片上传在公共空间，而后在文章内调用，因为目前还没有解决Editor.md上传图片的解决方案。
关于评论，这里评论模块是一个单独的模块，目前基本完成，用户体验还可以。

###关于目前版本的兼容性
---
>抵制万恶的IE-6-7-8是我必须去做也很乐于做的事情！

所以，不要妄想在IE-6-7-8上面使用本站！IE浏览器一律不做测试。**请尽量使用Google *Chrome* ， *Fiorefox*， *Safari*！**

###**那么我们总是会碰到各种各样的问题**
------------
事实上最难解决的问题是，作为一个Full Stack Developer，我总是被各种问题折腾的死去活来，也就是说，从前段JS,CSS到后端的业务逻辑，以至于后面的部署，等等等等的问题都必须由**全栈工程师**一个人来解决。这就是最大的问题。

>首先，关于MarkDown的在线编辑器，这里直接在github上找到了Editor.md,国人很少有这样优秀的开源项目，亲切的中文文档，和详细的example都很给力（即使这样我还是花了大概四个小时来完成这项工作）。


暂时就更新到这里吧！
