#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import tornado.web

LIST_INFO = [
    {
        "username": "alex",
        "email": "cjx222@163.com"
    },
]
for i in range(99):
    temp = {"username": "alex" + str(i), "email": "cuicui0624@" + str(i + 100) + ".com"}
    LIST_INFO.append(temp)  # 伪造一些LIST数据


class Pagination:
    def __init__(self, current_page, all_item):
        """
        :param current_page: 当前页
        :param all_item: 条目个数
        """
        all_page, c = divmod(all_item, 5)
        if c > 0:
            all_page += 1
        """以上代码计算分页总数"""
        try:
            current_page = int(current_page)  # page默认接收到的是个字符串，转化成数字型，
        except:  # 转化失败，填入了字符型或者其他
            current_page = 1
        if current_page < 1:
            current_page = 1
        """以上代码获取符合规则的当前页码"""
        self.current_page = current_page
        self.all_page = all_page

    @property  # 特性，以属性的方式，执行方法
    def start(self):
        """
        数据的切片的起始位置
        :return: 返回切片的起始值
        """
        return (self.current_page - 1) * 5

    @property
    def end(self):
        """
        数据切片的结束位置
        :return: 返回切片的结束值
        """
        return self.current_page * 5

    def page_str(self, base_url):
        """
        :param base_url: 基础的url前缀
        :return: html 分页字符串
        """

        """
        # s，e
        # all_page:总页数 current_page:当前页
        # range(当前页-5，当前页+5+1)
        # 当 总前页≤11时，显示1，总前页
        # 当 总页数>11时
        # 如果当前页≤6，显示的还是1,11
        # 如果当前页>6,
        # 如果 当前页+5>总页数
        # 显示 总页数-10，总页数
        # else 显示 当前页-5，当前页+5"""
        if self.all_page <= 11:
            s = 1
            e = 11
        else:
            if self.current_page <= 6:
                s = 1
                e = 11
            else:
                if (self.current_page + 5) > self.all_page:
                    s = self.all_page - 10
                    e = self.all_page
                else:
                    s = self.current_page - 5
                    e = self.current_page + 5
        temp_page = ""
        #首页
        first_page= """<a href="%s/1">首页</a>""" % (base_url)
        temp_page+=first_page
        #上一页
        if self.current_page==1:
            pre_page = """<a href="javascript:void(0)">上一页</a>"""
        else:
            pre_page = """<a href="%s/%s">上一页</a>"""%(base_url,self.current_page-1)
        temp_page+=pre_page
        for p in range(s, e + 1):  # 要显示的页码起始结束的控制
            if p == self.current_page:
                t_page = """<a class="active" href="%s/%s">%s</a>
                                    """ % (base_url, p, p)
            else:
                t_page = """<a href="%s/%s">%s</a>
                    """ % (base_url, p, p)
            temp_page += t_page
        # 下一页
        if self.current_page >= self.all_page:
            last_page = """<a href="javascript:void(0)">下一页</a>"""
        else:
            last_page = """<a href="%s/%s">下一页</a>""" % (base_url, self.current_page + 1)
        temp_page += last_page
        #尾页
        end_page = """<a href="%s/%s">尾页</a>""" % (base_url,self.all_page)
        temp_page+=end_page
        return temp_page

class IndexHandler(tornado.web.RequestHandler):
    def get(self, page):
        page_obj = Pagination(page,len(LIST_INFO))
        current_list = LIST_INFO[page_obj.start:page_obj.end]
        temp_page = page_obj.page_str("/index")
        self.render("home/index.html", list_info=current_list, current_page=page_obj.current_page,
                    str_page=temp_page)  # home前面不加/，current_page记住当前页，

    def post(self, page, ):
        username = self.get_argument("username", None)
        email = self.get_argument("email", None)
        temp = {"username": username, "email": email}
        LIST_INFO.append(temp)
        self.redirect("/index/" + page)  # page拿到的本来就是字符串
