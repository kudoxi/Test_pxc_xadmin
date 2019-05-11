from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.
def test(req):
    #创建数据
    # models.Foo.objects.create(caption='ttt')
    # models.Foo.objects.create(caption='aaa')
    # models.Foo.objects.create(caption='wwe')
    # models.UserType.objects.create(title = '2b用户',fo_id=1)
    # models.UserType.objects.create(title = '普通用户',fo_id=2)
    # models.UserType.objects.create(title = 'nb用户',fo_id=3)
    # models.UserInfo.objects.create(name='aaa',age=12,ut_id=1)
    # models.UserInfo.objects.create(name='bbb',age=16,ut_id=2)
    # models.UserInfo.objects.create(name='ccc',age=14,ut_id=3)
    # models.UserInfo.objects.create(name='ddd',age=14,ut_id=3)
    # models.UserInfo.objects.create(name='eee',age=16,ut_id=2)

    # for i in range(100):
    #     name = 'root'+ str(i)
    #     models.UserInfo.objects.create(name=name, age=16, ut_id=random.choice([1,2,3]))
    #获取数据
    res = models.UserInfo.objects.all()
    for i in res:
        print('name',i.name)
        print('age',i.age)
        print('utid',i.ut_id)
        print('utype',i.ut.title)
        #print('caption',i.ut.fo.caption)

    #查看第一条
    res0 = models.UserInfo.objects.all().first()
    print('name', res0.name)
    print('age', res0.age)
    print('utid', res0.ut_id)
    print('utype', res0.ut.title)
    #print('caption', i.ut.fo.caption)

    #反向查询
    res1 = models.UserType.objects.all().first()
    #属于某一用户类型的所有用户
    for i in res1.userinfo_set.all():
        print(res1.title,i.name)


    #只查询个别字段_返回携带字典的QuerySet
    res2 = models.UserInfo.objects.all().values('name', 'age', 'ut__title')#QuerySet[{'name':'aaa','age':12}]
    for i in res2:
        print(i,type(i))
        print('name',i['name'])
        print('age',i['age'])
        print('ut__title',i['ut__title'])
        #print('ut',i.ut.title) 报错提示不存在

    #只查询个别字段_返回携带元组的QuerySet
    res3 = models.UserInfo.objects.all().values_list('name', 'age')#QuerySet[('aaa',12),('ccc',23)]
    for i in res3:
        print(i)
        print('name',i[0])
        print('age',i[1])

    return HttpResponse("aasa")


from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def test_page(req):
    params = {}
    current_page = req.GET.get('page')
    userlist = models.UserInfo.objects.all()

    page_obj = Paginator(userlist,10)
    '''page_obj
    per_page:每页显示条目数量
    count：数据总数
    num_pages :总页数
    page_range:总页数的索引范围 如（1,100）
    page:page对象
    '''

    try:
        posts = page_obj.page(current_page)#当前显示第几页
    except PageNotAnInteger as e:          #判断非整数传参
        posts = page_obj.page(1)
    except EmptyPage as e:                 #判断负数和空
        posts = page_obj.page(1)
    '''posts
    has_next                    是否有下一页
    next_page_number            下一页页码
    has_previous                是否有上一页
    previous_page_number        上一页页码
    object_list                 分页之后的数据列表
    number                      当前页
    '''
    params['userlist'] = posts
    return render(req, 'test_page.html', params)

from utils.pager import PageInfo
def test_page_self(req):
    params = {}
    user_obj = models.UserInfo.objects.all()
    print(type(user_obj))
    page_obj = PageInfo(req.GET.get('page'),10,user_obj,req.path,5)
    userlist = page_obj.get_list()
    params['userlist'] = userlist
    params['page_obj'] = page_obj
    return render(req, 'test_page_self.html', params)

#标记某一字符串为安全的
from django.utils.safestring import mark_safe
def test_mark(req):
    temp = "<a href='www.baidu.com'>百度</a>"
    new_temp = mark_safe(temp)
    return render(req, 'test_mark.html', {'new_temp':new_temp})