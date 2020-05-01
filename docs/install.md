# 安装说明
## 1. 环境依赖
1. python 3.x
2. pywin32
3. Tesseract-OCR

## 2. 源码安装
### 2.1 安装python3.x
下载地址：[https://www.python.org/ftp/python/](https://www.python.org/ftp/python/)

### 2.2 生成虚拟环境
```bash
# 1. 命令行中执行，可以不是项目根目录 
pip install virtualenv

# 2. cmd 切换项目根目录
cd xxxxx

# 3. 生成虚拟环境（相对项目根目录）  
virtualenv venv

# 4. 激活虚拟环境（相对项目根目录）
venv\Scripts\activate.bat
```

### 2.3 安装依赖库
注意：windows 安装扩展包：[地址](https://www.lfd.uci.edu/~gohlke/pythonlibs/)
```bash
pip install data/lib/pywin32-227-cp38-cp38-win_amd64.whl
pip install -r requirements.txt
```

### 2.4 安装Tesseract(验证码自动识别)
下载地址：[https://digi.bib.uni-mannheim.de/tesseract/](https://digi.bib.uni-mannheim.de/tesseract/)   
源码：[Github](https://github.com/UB-Mannheim/tesseract)

<font color="red">**注意：需要添加中文支持** </font> 
#### 1. 配置环境变量
将C:\Program Files\Tesseract-OCR 添加到环境变量中即可   
运行 tesseract -v 查看版本

## 3. 验证码训练