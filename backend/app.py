from flask import *
import datetime
from datetime import timedelta
import os
from models.yolo import DetectionModel
from detect import run

# =============================Util Functions=====================================


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


# =============================Configurations=====================================
app = Flask(__name__)
app.config['ALLOWED_EXTENSIONS'] = set(['jpg', 'png'])
app.config['UPLOAD_FOLDER'] = r'./uploads'
# 解决缓存刷新问题
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

# ==============================Flask Route=======================================


@app.after_request
# 添加header解决跨域
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    response.headers['Access-Control-Allow-Methods'] = 'POST'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, X-Requested-With'
    return response


@app.route('/')
def hello_world():
    return redirect(url_for('static', filename='./index.html'))


@app.route('/upload', methods=['GET', 'POST'])
# GET获取用户信息，POST发送模型处理后的结果
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        print(datetime.datetime.now(), file.filename)
        # 创建存放用户上传的文件
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        src_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        # 保存用户上传的文件
        file.save(src_path)
        ext = file.filename.rsplit('.', 1)[1]  # 文件后缀名
        run()
        # 返回给前端页面，前端页面显示信息
        return jsonify({'status': 1,
                        'image_url': 'http://127.0.0.1:5003/uploads/' + file.filename,
                        'draw_url': 'http://127.0.0.1:5003/tmp/exp/' + file.filename,
                        })
    return jsonify({'status': 0})


@app.route('/tmp/<path:file>', methods=['GET'])
def show_file(file):
    if request.method == 'GET' and file:
        image_data = open(f'tmp/{file}', "rb").read()
        # 传入前端的数据，一般用二进制格式传送数据
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/png'
        return response

# ======================================Main======================================


if __name__ == '__main__':
    # 加载yolo5模型
    with app.app_context():
        current_app.model = DetectionModel()
    app.run(host='127.0.0.1', port=5003, debug=True)
