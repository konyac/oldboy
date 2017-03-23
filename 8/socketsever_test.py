#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socketserver
r=socketserver.ThreadingTCPServer()
r.serve_forever()