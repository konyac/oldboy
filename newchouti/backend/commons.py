#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import random
import hashlib,time,collections

def generate_verification_code():
    ''' 随机生成6位的验证码 '''
    # 注意： 这里我们生成的是0-9A-Za-z的列表，当然你也可以指定这个list，这里很灵活
    # 比如： code_list = ['P','y','t','h','o','n','T','a','b'] # PythonTab的字母
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z的ASCII码
        code_list.append(chr(i))
    for i in range(97, 123):  # a-z的ASCII码
        code_list.append(chr(i))

    myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回.是个list
    verification_code = ''.join(myslice)  # list to string
    # print code_list
    # print type(myslice)
    return verification_code


def generate_verification_code2():
    ''' 随机生成6位的验证码 '''
    code_list = []
    for i in range(2):
        random_num = random.randint(0, 9)  # 随机生成0-9的数字
        # 利用random.randint()函数生成一个随机整数a，使得65<=a<=90
        # 对应从“A”到“Z”的ASCII码
        a = random.randint(65, 90)
        b = random.randint(97, 122)
        random_uppercase_letter = chr(a)
        random_lowercase_letter = chr(b)

        code_list.append(str(random_num))
        code_list.append(random_uppercase_letter)
        code_list.append(random_lowercase_letter)
    verification_code = ''.join(code_list)
    return verification_code

def generate_md5(value):
    r = str(time.time())
    obj = hashlib.md5(r.encode('utf-8'))
    obj.update(value.encode('utf-8'))
    return obj.hexdigest()

def tree_search(d_dic, comment_obj):
    '''
    
    :param d_dic: 已经存在的评论树字典
    :param comment_obj: 要添加的评论。这个是子评论是回复
    :return: 
    '''
    # 在comment_dic中一个一个的寻找其回复的评论
    # 检查当前评论的 reply_id 和 comment_dic中已有评论的nid是否相同，
    #   如果相同，表示就是回复的此信息
    #   如果不同，则需要去 comment_dic 的所有子元素中寻找，一直找，如果一系列中未找，则继续向下找
    for k, v_dic in d_dic.items():
        # 找回复的评论，将自己添加到其对应的字典中，例如： {（评论一）： {（回复一）：{},（回复二）：{}}}
        if k[0] == comment_obj[2]:#检测到是对他的回复
            d_dic[k][comment_obj] = collections.OrderedDict()#添加到子评论中
            return
        else:
            # 在当前第一个跟元素中递归的去寻找父亲
            tree_search(d_dic[k], comment_obj)


def build_tree(comment_list):
    """
    
    :param comment_list: 传入的评论列表。每一个评论是元组【（评论1），（评论2）】
    :return: 
    """

    comment_dic = collections.OrderedDict()#创建一个有序的字典，作为评论树字典

    for comment_obj in comment_list:
        print(comment_obj)
        #comment_obj 单个评论。(1, '1111', None, 'cjx', datetime.datetime(2017, 11, 16, 15, 49, 44), 0, 0, 1)
        if comment_obj[2] is None:#判断回复id是否是空
            # 如果是根评论，添加到comment_dic[评论对象] ＝ {}，添加这个评论到评论树字典里，同时他的值也是个有序字典
            comment_dic[comment_obj] = collections.OrderedDict()#{(根评论)：{}，}
        else:
            # 如果是回复的评论，则需要在 comment_dic 中找到其回复的评论
            tree_search(comment_dic, comment_obj)
    return comment_dic

if __name__ == '__main__':
    code = generate_verification_code()
    code2 = generate_verification_code2()
    print(code)
    print(code2)