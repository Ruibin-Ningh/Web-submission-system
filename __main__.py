
import os
import time
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

# 设置上传文件保存的目录
upload_folder = 'data'
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)

# 用于存储用户信息的全局变量
user_info = {}


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global user_info
    if request.method == 'POST':
        # 检查是否有文件被上传
        if 'file' not in request.files:
            return '没有文件上传'

        file = request.files['file']

        # 检查文件名是否为空
        if file.filename == '':
            return '文件名不能为空'

        # 获取用户输入的姓名和负责项目
        name = request.form['name']
        project = request.form['project']

        # 获取文件的原始文件名（包括后缀）
        original_filename = file.filename

        # 构建文件名：[姓名-负责项目].[原始后缀]
        filename = f"{name}-{project}.{original_filename.split('.')[-1]}"

        # 存储用户信息
        user_info = {'name': name, 'project': project}

        # 服务端确认上传
        print(f"{filename} 请求上传文件，文件后缀：{original_filename.split('.')[-1]} [ y/n ]")

        # 模拟等待用户确认
        time.sleep(3)

        # 用户确认上传
        if input() == 'y':
            # 保存上传的文件到指定目录，并使用构建的文件名
            file.save(os.path.join(upload_folder, filename))
            print('上传成功')
            return render_template('message.html', message='文件上传成功')  # 显示上传成功消息
        else:
            print('上传失败')
            return render_template('message.html', message='文件上传被拒绝')  # 显示上传失败消息

    return render_template('index.html', user_info=user_info)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)