# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Description:
#
# @Time: 2021/9/22 09:37
import json

from flask import Flask, request

import get_dy_url

app = Flask(__name__)


@app.route('/execute/video', methods=['POST'])
def execute_video():
    if request.method == "POST":
        result = {'code': 200, 'url': ''}
        data = request.get_data()
        data_json = json.loads(data)
        share_text = data_json.get('share_text')
        if share_text is not None:
            video_url = get_dy_url.main_video(share_text)
            result['url'] = video_url
        return json.dumps(result)


@app.route('/execute/image', methods=['POST'])
def execute_image():
    if request.method == "POST":
        result = {'code': 200, 'url': ''}
        data = request.get_data()
        data_json = json.loads(data)
        share_text = data_json.get('share_text')
        if share_text is not None:
            video_url = get_dy_url.main_image(share_text)
            result['url'] = video_url
        return json.dumps(result)


if __name__ == '__main__':
    app.run(port=7775, host='127.0.0.1')
