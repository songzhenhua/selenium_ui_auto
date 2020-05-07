## 基于python2+selenium3+pytest4的UI自动化框架

>环境：Python2.7.10， selenium3.141.0， pytest4.6.6， pytest-html1.22.0， Windows-7-6.1.7601-SP1

### 特点：
- 二次封装了selenium，编写Case更加方便。  
- 采用PO设计思想，一个页面一个Page.py，并在其中定义元素和操作方法；在TestCase中直接调用页面中封装好的操作方法操作页面。  
- 一次测试只启动一次浏览器，节约时间提高效率(适合公司业务的才是最好的)。  
- 增强pytest-html报告内容，加入失败截图、用例描述列、运行日志。
- 支持命令行参数。
- 支持邮件发送报告。

### 目录结构：  
- config  
  - config.py：存放全局变量，各种配置、driver等  
- drive：各浏览器驱动文件，如chromedriver.exe  
- file
  - download：下载文件夹
  - screenshot：截图文件夹  
  - upload：上传文件夹     
- page_object：一个页面一个.py，存放页面对象、操作方法 
  - base_page.py：基础页面，封装了selenium的各种操作
  - hao123_page.py：hao123页面  
  - home_page.py：百度首页 
  - news_page.py：新闻首页  
  - search_page.py：搜索结果页 
- report：
  - report.html：pytest-html生成的报告   
- test_case
  - conftest.py：pytest特有文件，在里面增加了报告失败截图、用例描述列
  - test_home.py：百度首页测试用例
  - test_news.py：新闻首页测试用例
  - test_search.py：搜索结果页测试用例
  - demo1.py：通过加cookies免登陆的Demo
  - demo2.py：在已打开的Chrome浏览器进行调试的Demo
- util：工具包  
  - log.py：封装了日志模块
  - mail.py：封装了邮件模块，使用发送报告邮件功能需要先设置好相关配置，如用户名密码
- run.py：做为运行入口，封装了pytest运行命令；实现所有测试用例共用一个driver；实现了运行参数化(结合Jenkins使用)；log配置初始化；可配置发送报告邮件。  

### 元素定义特别用法说明：
本框架支持selenium所有的定位方法，为了提高编写速度，改进了使用方法，定义元素时方法名和方法值为一个用逗号隔开的字符串，如：
- xpath定位：i_keyword = 'xpath,//input[@id="kw"]'  # 关键字输入框
- id定位：b_search = 'id,su'  # 搜索按钮
- 其他定位方法同上，不再一一举例

在代码中使用上面定义的元素：
> self.type(self.i_keyword, "学好selenium") # 使用封装过的sendkeys方法输入搜索关键字，详见base_page.py  
> self.click(self.b_search) # 使用封装过的click方法点击搜索按钮

 ### 命令行参数：  
 Demo只添加了一个环境参数-e, 可设置测试环境preview，线上环境product，如要在线上运行测试，启动脚本输入：
 > python run.py -e product  
 
 可自行根据实际需要添加更多参数，并在run.py中的get_args()中进行修改。
 
----------------------------------------------------------------------------
实际报告如图，分别展现了一个执行失败Case的报错信息+截图，一个执行通过Case的运行日志。

![readme_report.png](https://github.com/songzhenhua/selenium_ui_auto/blob/master/readme_report.png)
