#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import time
from jinja2 import Template
def new():
    # f = open(os.path.join('views', 's1.html' ), 'r')
    # data = f.read()
    # f.close()
    # new_data = data.replace("{{item}}", str(time.time()))
    # return new_data
    f = open(os.path.join('views','s1.html'))
    result = f.read()

    template = Template(result)
    data = template.render(name='John Doe', user_list=['alex', 'eric','xiaojun', 'sb'])#渲染，render
    return data.encode('utf-8')

def index():
    f = open(os.path.join('views', 'index.html'), 'r')
    data = f.read()
    f.close()
    return data

def home():
    return 'home'