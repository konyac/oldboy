#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import re

com = '<p class="mb10 cmp-txtshow" id="textShowMore">上海</p><>1.发送大量开发建设的刻录机疯狂拉升<sdafjkldfjkl jkasjdfkls>'

ret = re.sub(r'<[\w=\-\s"/]*>','', com)
print(ret)
# content = "<1>23abc456"
# new_content = re.sub('<', 'sb', content)
# # new_content = re.sub('\d+', 'sb', content, 1)
# print(new_content)
