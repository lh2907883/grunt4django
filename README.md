# grunt4django

### 主要功能

**grunt4django**, 在django的runserver命令在之后，启动本地的grunt进程（`grunt default`可以自定义，一般是**watch**）,在退出时kill grunt进程,并且根据需要在html页面的head部分添加**livereload**脚本支持

### 实现原理
**gruntserver.py**模块继承**StaticfilesRunserverCommand**, 调用基类的**inner_run**然后根据配置文件设置的*GRUNT_DIR*找到grunt目录,运行`grunt default`

**middleware.py**模块里面实现了一个叫**LiveReloadMiddleware**的中间件,拦截所有**'text/html', 'application/xhtml+xml'**的响应,并在响应head里面添加

    <script src="http://localhost:35729/livereload.js"></script>
只要保证**grunt**的**livereload**任务正常运行,并且成功启动了**watch**任务,它就能工作,并在html,js,css等文件编辑保存时,自动刷新页面

### 安装和配置 
安装

    sudo pip install grunt4django

*settings.py* 添加下面配置
    
    # grunt目录（这个目录是相对于settings.py文件的 ）
    GRUNT_DIR = '../grunt'
    
    # 注册app, 这样gruntserver命令才能被 python manage.py识别
    INSTALLED_APPS = (
        ...
        'grunt4django',
    )
    
    # 注册LiveReloadMiddleware中间件
    MIDDLEWARE_CLASSES = (
        ...
        'grunt4django.middleware.LiveReloadMiddleware',
    )
使用示例见 <https://github.com/lh2907883/whatsdjango>

### 项目启动
	# 使用 gruntserver 代替之前的 runserver
	python manage.py gruntserver

### Pip打包和发布

官方教程见 <https://packaging.python.org/en/latest/distributing/>

#####打包环境准备：
1. sudo pip install twine
2. sudo pip install wheel

#####打包:
1. cd 到模块目录
2. sudo python setup.py bdist_wheel --universal
3. 到 <https://pypi.python.org/pypi?%3Aaction=register_form> 上去注册一个帐号 
4. sudo python setup.py register #登录帐号
5. sudo python setup.py sdist bdist_wheel upload  #上传模块代码到pip
6. 打开<https://pypi.python.org/pypi?%3Aaction=submit_form>
7. 上传 myproject.egg-info/PKG-INFO 然后点`Add Package Info`，这样才算真正在pip上发布模块
