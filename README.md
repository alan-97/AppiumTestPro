# AppiumTestPro
app多进程自动化框架

# windows-appium 环境配置
1.安装node.js
  - 官方地址：https://nodejs.org/en/download/
  - cmd下输入命令 node -v可以查看Node.js 的版本。
  - 安装好Node.js后对其做一些基本设置，均在cmd下输入命令即可
1.1. 设置缓存
  - npm config set cache "D:\Program Files\nodejs\node_cache"
1.2. 设置全局模块存放路径
  - npm config set prefix "D:\Program Files\nodejs
1.3. 设置淘宝NPM镜像
  - npm config set registry "https://registry.npm.taobao.org"
  - npm install -g cnpm --registry=https://registry.npm.taobao.org
  - 通过设置NPM 镜像之后，Node.js 的一些库均可以在淘宝NPM镜像下下载。也就是说以后的npm命令，我们可以用cnpm命令代替，访问该镜像网站。在部分电脑下，可能还要配置cnpm环境，但也是非常简单。例如我的Node.js 安装在D盘，即可在环境变量中添加 D:\Program Files\nodejs\node-global

2.安装Android SDK 配置Android sdk环境
sdk环境配置：http://www.cnblogs.com/puresoul/p/4597211.html

3.安装Appium 
运行cmd
  - cnpm install -g appium 
  如果报错用以下方式安装：
  - 输入命令：npm install -g cnpm --registry=https://registry.npm.taobao.org
  - 再输入命令：cnpm install -g appium
  - 安装完成后检验appium是否成功安装输入：appium
  
4.安装Appium-doctor
  - appium-doctor可以检测Appium整体依赖环境配置情况。在cmd下输入以下命令就可以安装
  - cnpm install appium-doctor -g
  - 安装完appium-doctor 环境之后，可以通过 appium-doctor 看到如下提示说明整体环境配置成功

5.配置系统cmd环境变量
- 将路径C:\Windows\System32 添加至系统变量path中
