
import math
class PageInfo(object):
    '''
    current_page:当前页
    per_page：每页显示数量
    QuerySet：sql查询出的QuerySet对象
    url_path：分页跳转路径
    max_page：显示的分页器最多数量，-1则全显示

    views方法里，将PageInfo构造后，传到template html页面，调用{{pageinfo.get_page}}即可显示,样式在css里设置
    ul的class:k_page_ul
    上一页a标签的class:k_page_pre
    页码a标签的class:k_page
    下一页a标签的class:k_page_next
    当前页li标签class: k_current_page
    '''
    def __init__(self,current_page,per_page,QuerySet,url_path,max_page=-1,*args,**kwargs):
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1

        self.per_page = per_page
        self.QuerySet = QuerySet
        self.url_path = url_path
        self.max_page = max_page

    # 第一页，0～10 不包括10
    # 第二页，10～20 不包括20
    # ...
    def start(self):
        return (self.current_page - 1) * self.per_page

    def end(self):
        return self.current_page * self.per_page

    def page_num(self):
        total_num = self.QuerySet.count()
        return math.ceil(total_num / self.per_page)

    def get_list(self):
        return self.QuerySet[self.start():self.end()]

    def get_page(self):
        total_page = self.page_num()
        if total_page == 0:
            return ''
        print(self.max_page,total_page)
        if self.max_page > total_page or self.max_page == -1:
            self.max_page = total_page

        prepage_num = math.ceil((self.max_page - 1)/2)#当前页 的前面有多少页码
        aftpage_num = (self.max_page - 1) - prepage_num #当前页 的后面有多少页码
        if self.current_page - prepage_num <= 0:
            #如果前面没那么多页，前面有多少页，显示多少
            prepage_num = self.current_page - 1
            #后面的页码来补位
            aftpage_num = self.max_page - 1 - prepage_num

        if self.current_page + aftpage_num > total_page:
            #超出页码
            prepage_num = prepage_num + aftpage_num

        #页码放入数组以便遍历
        pages = [self.current_page]
        if prepage_num != 0:
            pre_page = -1
            for i in range(prepage_num):
                if pre_page==-1:
                    pre_page = self.current_page - 1
                else:
                    pre_page -=1
                if pre_page > 0 and pre_page not in pages:
                    pages.append(pre_page)
        if aftpage_num != 0:
            aft_page = -1
            for k in range(aftpage_num):
                if aft_page == -1:
                    aft_page = self.current_page + 1
                else:
                    aft_page += 1
                if aft_page <= total_page and aft_page not in pages:
                    pages.append(aft_page)

        pages = sorted(pages,reverse=False)

        #分页器
        pages_html = '<ul class="k_page_ul">'
        pre_num = self.current_page - 1
        next_num = self.current_page + 1
        #上一页
        url = self.url_path + '?page={}'
        if self.current_page != 1:
            pages_html += '<li><a class="k_page_pre" href="' + url.format(str(pre_num)) + '">上一页</a></li>'
        #中间页码
        for i in pages:
            current_class = 'k_current_page' if self.current_page == i else ''
            pages_html += '<li class="'+current_class+'"><a class="k_page" href="'+url.format(str(i))+'">'+str(i)+'</a></li>'
        #下一页
        print(total_page)
        if self.current_page != total_page :
            pages_html += '<li><a class="k_page_next" href="' + url.format(str(next_num)) + '">下一页</a></li>'

        return pages_html+"</ul>"
