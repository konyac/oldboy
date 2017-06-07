#!/usr/bin/env python
# -*- coding:utf-8 -*-
import itchat
from itchat.content import TEXT



itchat.auto_login()
list=itchat.get_friends()
memberList = itchat.update_chatroom('翰林')
print(list)

print(memberList)
# itchat.send_msg(list)