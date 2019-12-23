JK-Alfred
===

## 前言

这是个使用 Vue.Js，Ant Design of Vue，Scrapy，Python Django 所做成的**动漫观看网站**。

## 前端

我們使用 **Vue.js** 作為我們的前端開發的框架，並使用 **Webpack** 做為項目前端管理，組件使用 **Ant Design Of Vue**。

### 安裝與使用

在項目目錄安裝依賴。

```zsh
npm install # 安裝 npm 依賴
npm install ant-design-vue --save # 安裝 Ant Design 組件
npm run dev #開啟端口測試
```

我们在前端有以下界面：

+ 登入注册
+ 主界面
  - Home
  - User
    - Information
    - Favorite
    - History
  - Classification
  - About
  - Search
  - Play Video

## 后端

### 后端web使用说明

```zsh
 python manage.py runserver 0.0.0.0:8000  #外机访问命令，不需要此命令的時候可以用自己的辦法。
```

- 关于下载本项目后 后端的本地化，只有一个：将 `/home/lwl/Study/code/Python/django/mysite-master` 转变为你相应的项目地址，
- 重点在 `mysite-master/yh/view.py` 以及 `mysite-master/yh/load.py`。
- 还有 `mysite-master/mysite/settings.py` 里面需要修改。
- 如果显示 **load 模块**错误，那么 请 **pip** 删除你的 **pip Load** 模块。

### 后端的项目规划

> 老实说，我一开始没有规划好，抱着写写玩的心态写，导致最后项目有点乱。（在一个 Hello World 里面写的）

- 在 **mysite** 里面，**yh** 文件夹是我们的后端接口的主体。**yh** 中的 **yuanma-master** 文件夹是爬虫 **Scrapy** 。 然后里面的 `uanma-master/TestDemo/TestDemo/spiders/minimp4.py` 是我们的爬虫。
- 大体上如此，临近期末，很多细节没有打磨。望见谅。