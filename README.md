MicroMsg_platform
=================
##### 微信公众平台通用代码
  
  
### 使用方法：  
#### 1.将app 放入主目录
#### 2.配置setting.py,如Installedapp加入app.weixin1,admin
#### 3.配置总url：
```
     from django.contrib import admin
     admin.autodiscover()
     ##added by tulpar,2014/01/27,for MicroChat
     urlpatterns = patterns('',
	   url(r'^weixin1/$', 'app.weixin1.views.main', name='weixin1'),
    ) 
```
