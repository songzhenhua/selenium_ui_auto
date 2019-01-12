本来想写一个基于selenium+pytest的UI自动化框架，框架基本功能完成写demo case的时候，发现业务前端编写不规范，且产品更新频繁，光是编写&调试element的xpath或css表达式就非常浪费时间。

此时发现Katalon这个工具，专业团队维护、终身免费、持续更新，因为是基于selenium开发的，所以selenium有的功能都有。可视化操作，可录制脚本，支持POM，代码能力不强也可以使用；也有代码编辑模式，高级用户可以定制功能。因为脚本编写&调试速度比用selenium写框架强多了，所以现在我已经用Katalon了，安利给大家。


目录结构：
config：配置文件
drive：各浏览器drive，目前代码中没用到此文件夹，我直接把Chrome的drive放到Chrome安装文件夹并加了系统变量
file：上传、下载、截图文件夹
pageObject：一个页面一个.py，存放页面对象、操作方法
report：报告、日志
testCase：用例
util：工具包


如果继续开发的话，TODO：
加入log功能
加入HTML报告&发送邮件功能
加入配置文件，区分线上/测试等各种场景
加入图片对比功能（好像也没什么用，现在页面到处都是动态的）


----------------------------------------------------------------------------
pytest testProjectList.py --html=report.html	执行用例，输出html报告
pytest testProjectList.py --junitxml=report.xml	执行用例，输出JunitXML报告
在report文件夹执行pytest -s ../testCase/prdb/test_Crf.py --html=report.html