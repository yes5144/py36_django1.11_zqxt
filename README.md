# py36_django1.11_zqxt
(Django 开发内容管理系统)[https://code.ziqiangxuetang.com/django/django-cms-develop.html]

## django 
### 

yum install python-pip
pip install virtualenv virtualenvwrapper

find / -name virtualenvwrapper

### 修改~/.bash_profile或其它环境变量相关文件，添加以下语句
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/workspace
source /usr/bin/virtualenvwrapper.sh

source .bash_profile

### 创建新环境
mkvirtualenv -p /usr/local/python/bin/python3 py36_django1.11_zqxt

pip list

pip install -i https://pypi.douban.com/simple/ django==1.11.8
pip install -i https://pypi.douban.com/simple/ django-users2


### 安装 nodejs
yum install nodejs
### 安装 cnpm
npm -v
cnpm -v
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm -v

### 安装指定版本bootstrap
cnpm install bootstrap@3.3.7
cnpm install jquery@3.2.1
cnpm install vue
cnpm install vue-router

### 1. 新建一个 django project
django-admin.py startproject project_name

### 2. 新建 app
python manage.py startapp app_name

