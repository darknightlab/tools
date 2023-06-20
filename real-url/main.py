# 一个网页，接受get请求，从url参数中读取rid，并获取urlpath，传入自己的函数处理，这个函数返回一个网址，把用户302重定向到这个网址
import flask
from flask import redirect
import importlib
import json

app = flask.Flask(__name__)


@app.route("/<platform_name>/<rid>", methods=["GET"])
def process_request(platform_name, rid):
    redirect_url = process_rid(platform_name, rid)
    return redirect(redirect_url, code=302)


def process_rid(platform_name, rid):
    # 导入 ./platform_name.py, 并执行get_real_url
    p = importlib.import_module(platform_name)
    return json.loads(p.get_real_url(rid))["m3u8"]


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 80
    app.run(
        host=host,
        port=port,
    )
