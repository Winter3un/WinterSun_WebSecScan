### 项目简介

该项目用于安全人员挖网站安全漏洞的时候，收集一些基础信息，并能够对网站安全进行大体的扫描测试，主要测试（sql、xss）

定位：一个辅助功能的软件
具有攻击性,请在合法渗透测试中使用，否则会有法律问题。

### 项目背景

该项目书制定于2016/5/30日，距离实习结束尚有两周时间，距离G20结束尚有3个月时间。

### 开发周期

开发此项目总时长：`31*3*24 = 2232` 小时

由于该项目进行于G20安保期间，所以G20安保工作时必须抽调足够多的时间对其进行研究工作。

### 开发人员背景

资格背景：网络安全专业，从事网络安全工作半年，了解大多数网站安全漏洞，并能够对网站安全漏洞进行手工检测。有python编程经验，能够独立开发软件。
### 开发环境
1. python2.7
2. windows10
3. python-dev
4. scrapy

### 项目构成

1. web爬虫（用于收集网站基础信息。）
2. 检测模块(用于对网站进行基础安全检测。)
3. 报告生成模块

### web爬虫模块设计

> 但是作为一项普通的技术，普通人同样可以用爬虫技术做很多很多的事情，比如：你想了解一下FreeBuf所有关于爬虫技术的文章，你就可以编写爬虫去对FreeBuf的文章进行搜索，解析。比如你想获得淘宝某类商品的价格，你可以编写爬虫自动搜索某类商品，然后获取信息，得到自己想要的结果，每天定时爬一下自己就可以决定在什么时候低价的时候买下心仪的商品了。或者说自己想收集某类信息集合成自己的数据库，但是手动复制粘贴特别的麻烦，这时候爬虫技术就可以帮上大忙了对不对？

由于web站点表示层都为html文档结构，我们可以利用python的xpath模块对其进行解析，并分析出其包含的url链接，然后再次访问属于该网站的url，继续分析。我们可以通过一个递归进行全面的网站url爬取。

其步骤如下
1. 提取出所有href属性的值（应对互联网上的各种复杂环境是远远不够的）

**难点：**
1. 如何分析form结构（使用scrapy）
2. 如何分析ajax（使用phantom.js）
3. URL相似性算法（过滤模块的使用，算法来源： [http://drops.wooyun.org/tips/5462](http://drops.wooyun.org/tips/5462)）
4. 效率提升（减少数据库交互操作，多线程）
5. 排除无关url（urlparse）

**资料收集：**
1. 《黑客大曝光：Web应用程序安全（原书第3版）》
2. [http://drops.wooyun.org/tips/6653](http://drops.wooyun.org/tips/6653 "使用sqlmapapi.py批量化扫描实践")
3. [http://scrapy-chs.readthedocs.io/zh_CN/latest/](http://scrapy-chs.readthedocs.io/zh_CN/latest/)
4. [http://www.freebuf.com/news/special/96763.html](http://www.freebuf.com/news/special/96763.html)
5. http://www.cnblogs.com/kylinlin/p/5401359.html
6. http://www.cnblogs.com/tqsummer/archive/2011/01/25/1944771.html （多线程）

### 随记：

1. 逻辑判断在request的构造以及response分析时都要用到。
2. 爬虫架构如下图
3. 考虑到