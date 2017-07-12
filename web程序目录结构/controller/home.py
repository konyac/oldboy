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


class IndexHandler(tornado.web.RequestHandler):
    def get(self, page):
        # if not page:#如果不填page的情况
        #     page =1
        try:
            page = int(page)  # page默认接收到的是个字符串，转化成数字型，
        except:  # 转化失败，填入了字符型或者其他
            page = 1
        if page < 1:
            page = 1
        # print(page)
        # 每页显示5条数据
        # page是当前页
        # 第一页显示0:5 LIST_INFO[0:5],切片是包含前面不含后面
        # 第二页显示5:10 LIST_INFO[5:10]
        # start (page-1)*5
        # end page*5
        start = (page - 1) * 5  # 显示的起始和结束的公式
        end = page * 5
        current_list = LIST_INFO[start:end]

        all_page, c = divmod(len(LIST_INFO), 5)  # 每页显示5个数据,如果余数大于0则+1
        if c > 0:
            all_page += 1
        temp_page = ""
        # s，e
        # all_page:总页数 current_page:当前页
        # range(当前页-5，当前页+5+1)
        # 当 总前页≤11时，显示1，总前页
        # 当 总页数>11时
        # 如果当前页≤6，显示的还是1,11
        # 如果当前页>6,
        # 如果 当前页+5>总页数
        # 显示 总页数-10，总页数
        # else 显示 当前页-5，当前页+5
        if all_page <= 11:
            s = 1
            e = 11
        else:
            if page <= 6:
                s = 1
                e = 11
            else:
                if (page + 5) > all_page:
                    s = all_page - 10
                    e = all_page
                else:
                    s = page - 5
                    e = page + 5
        for p in range(s, e+1):  # 要显示的页码起始结束的控制
            if p == page:
                t_page = """<a class="active" href="/index/%r">%s</a>
                            """ % (p, p )
            else:
                t_page = """<a href="/index/%r">%s</a>
            """ % (p , p )
            temp_page += t_page

        self.render("home/index.html", list_info=current_list, current_page=page,
                    str_page=temp_page)  # home前面不加/，current_page记住当前页，

    def post(self, page, ):
        username = self.get_argument("username", None)
        email = self.get_argument("email", None)
        temp = {"username": username, "email": email}
        LIST_INFO.append(temp)
        self.redirect("/index/" + page)  # page拿到的本来就是字符串
