from django.shortcuts import render
from django.http import HttpResponse
from . import models
import random

# Create your views here.
def test(req):
    #创建数据
    # models.Foo.objects.create(caption='ttt')
    # models.Foo.objects.create(caption='aaa')
    # models.Foo.objects.create(caption='wwe')
    # models.UserType.objects.create(title = '2b用户',fo_id=1)
    # models.UserType.objects.create(title = '普通用户',fo_id=2)
    # models.UserType.objects.create(title = 'nb用户',fo_id=3)

    # models.UserType.objects.create(title = '2b用户')
    # models.UserType.objects.create(title = '普通用户')
    # models.UserType.objects.create(title = 'nb用户')
    # models.UserInfos.objects.create(name='aaa',age=12,ut_id=1)
    # models.UserInfos.objects.create(name='bbb',age=16,ut_id=2)
    # models.UserInfos.objects.create(name='ccc',age=14,ut_id=3)
    # models.UserInfos.objects.create(name='ddd',age=14,ut_id=3)
    # models.UserInfos.objects.create(name='eee',age=16,ut_id=2)
    #
    # for i in range(100):
    #     name = 'root'+ str(i)
    #     models.UserInfos.objects.create(name=name, age=16, ut_id=random.choice([1,2,3]))
    #获取数据
    res = models.UserInfos.objects.all()
    print('*&*&*&*&*&*&*&*&*',res.query)
    for i in res:
        print('name',i.name)
        print('age',i.age)
        print('utid',i.ut_id)
        print('utype',i.ut.title)
        #print('caption',i.ut.fo.caption)

    #查看第一条
    res0 = models.UserInfos.objects.all().first()
    print('name', res0.name)
    print('age', res0.age)
    print('utid', res0.ut_id)
    print('utype', res0.ut.title)
    #print('caption', i.ut.fo.caption)

    #反向查询
    res1 = models.UserType.objects.all().first()
    #属于某一用户类型的所有用户
    for i in res1.userinfos_set.all():
        print(res1.title,i.name)


    #只查询个别字段_返回携带字典的QuerySet
    res2 = models.UserInfos.objects.all().values('name', 'age', 'ut__title')#QuerySet[{'name':'aaa','age':12}]
    for i in res2:
        print(i,type(i))
        print('name',i['name'])
        print('age',i['age'])
        print('ut__title',i['ut__title'])
        #print('ut',i.ut.title) 报错提示不存在

    #只查询个别字段_返回携带元组的QuerySet
    res3 = models.UserInfos.objects.all().values_list('name', 'age')#QuerySet[('aaa',12),('ccc',23)]
    for i in res3:
        print(i)
        print('name',i[0])
        print('age',i[1])

    #only,返回对象
    res4 = models.UserInfos.objects.all().only('id','name')
    for i in res4:
        print('id',i.id)
        print('name',i.name)
        print('age',i.age)#还可以拿到id,name之外的字段，但是会又去查询一次数据库，非常不友好，建议只取only的字段

    #defer,返回除了xxx之外的所有字段（id肯定会取）
    res4 = models.UserInfos.objects.all().defer('name')


    #排序
    models.UserInfos.objects.all().order_by('-id','age')

    #条件
    models.UserInfos.objects.exclude(id=1)#!=
    models.UserInfos.objects.filter(id__gt=2)#>
    models.UserInfos.objects.filter(id__gte=2)#>=
    models.UserInfos.objects.filter(id__lt=2)#<
    models.UserInfos.objects.filter(id__lte=2)#<=
    models.UserInfos.objects.filter(id__in=[2,3,4])#in
    models.UserInfos.objects.in_bulk([1,2,3])#根据主键id in 查询
    models.UserInfos.objects.filter(id__range=[2,10])#between and
    models.UserInfos.objects.filter(name__startswith='a')
    models.UserInfos.objects.filter(name__contains='root')

    from django.db.models import Count,Sum,Max,Min,F,Q
    #F-----所有年龄加1
    models.UserInfos.objects.all().update(age=F('age')+1)
    #Q-----写法1
    models.UserInfos.objects.filter(Q(id=1) | Q(id=2) & Q(name__contains='root'))#or
    # Q-----写法2
    #(id=1 or id=2 or (id=4 and name='aaa')) and (name='bbb' or name='ccc'))
    q1 = Q()
    q1.connector = "OR"
    q1.children.append(('id',1))
    q1.children.append(('id',2))

    q2 = Q()
    q2.connector = "OR"
    q2.children.append(('name','bbb'))
    q2.children.append(('name','ccc'))

    q3 = Q()
    q3.connector = "AND"
    q3.children.append(('id',4))
    q3.children.append(('name__contains','aaa'))
    q1.add(q3,'OR')

    con = Q()
    con.add(q1,'AND')
    con.add(q2,'AND')

    #动态生成条件
    condition_dict = {
        'k1':[1,2,3],
        'k2':[3,4,5],
        'k3':[5,6,2]
    }
    con = Q()
    for k,v in condition_dict.items():
        q = Q()
        q.connector = 'OR'
        for i in v:
            q.children.append(('id',i))

        con.add(q,'AND')
    models.UserInfos.objects.filter(con)
    #extra
    exv = models.UserInfos.objects.all().extra(
        tables=['ORMdemo_usertype'],#在from UserInfos后面拼接usertype
        select={
            'n':'select count(1) from ORMdemo_usertype where id > %s and id < %s',#额外的field,重命名为n
            'm':'select count(1) from ORMdemo_usertype where id > %s and id < %s'#额外的field,重命名为m
        },
        select_params=[1,9,4,8],#field的占位填充字符，按照顺序填充

        where=['ORMdemo_usertype.id = ORMdemo_userinfos.ut_id',#where 条件里拼接
               'ORMdemo_userinfos.id=1 or ORMdemo_userinfos.id = %s',#同时查两张表时，注意id前写表名，防止ambigious报错
               'name=%s'],
        params=[1,'root'],#where的占位填充字符
        order_by=['-ORMdemo_userinfos.id'],#排序
    )
    print(exv.query)
    #SELECT (select count(1) from ORMdemo_usertype where id > 1 and id < 9) AS `n`,
    # (select count(1) from ORMdemo_usertype where id > 4 and id < 8) AS `m`,
    #`ORMdemo_userinfos`.`id`,`ORMdemo_userinfos`.`name`,`ORMdemo_userinfos`.`age`,`ORMdemo_userinfos`.`ut_id`
    # FROM `ORMdemo_userinfos` , `ORMdemo_usertype`
    # WHERE (ORMdemo_usertype.id = ORMdemo_userinfos.ut_id)
    # AND (ORMdemo_userinfos.id=1 or ORMdemo_userinfos.id = 1)
    # AND (name=root)
    # ORDER BY (`ORMdemo_userinfos`.id) DESC
    print('extra:')
    for i in exv:
        print(i.name,i.age,i.n)

    #原生sql语句
    from django.db import connection,connections
    cursor = connection.cursor()
    cursor2 = connections['default'].cursor()#使用默认数据库，还可以填写settings.py里设置的其他数据库
    cursor.execute("select * from ORMdemo_usertype where id = %s",[1])
    row = cursor.fetchone()
    row2 = cursor.fetchall()
    print('原生：',row,row2)

    #根据查询结果的列名生成userinfo对象
    res = models.UserInfos.objects.raw('select * from ORMdemo_userinfo')
    #如果查询的是别的表，列名需要和userinfo表的字段名一样,只有这样，它才能转换为UserInfos对象
    res = models.UserInfos.objects.raw('select title as name,id as ut_id from ORMdemo_usertype')
    #或者这样定义别名,db2数据库
    name_map = {'i':'ut_id','title':'name'}
    models.UserInfos.objects.raw('select * from ORMdemo_usertype',translations=name_map,using='db2')

    #分组，统计每个组有多少人,每个组的id总和，每个组年龄最大为多，最小为多少
    v = models.UserInfos.objects.values('ut_id').annotate(
        utn=Count('id'),uts=Sum('id'),uta=Max('age'),uti=Min('age'))
    print('sql:',v.query)
    #  SELECT `ORMdemo_userinfos`.`ut_id`,
    #  SUM(`ORMdemo_userinfos`.`id`) AS `uts`,
    #  MAX(`ORMdemo_userinfos`.`age`) AS `uta`,
    #  COUNT(`ORMdemo_userinfos`.`id`) AS `utn`,
    #  MIN(`ORMdemo_userinfos`.`age`) AS `uti`
    #  FROM `ORMdemo_userinfos` GROUP BY `ORMdemo_userinfos`.`ut_id`
    #  ORDER BY NULL

    #统计，分组后每组人员个数大于30的组
    v2 = models.UserInfos.objects.values('ut_id').annotate(utn=Count('id')).filter(utn__gt=30)
    print('sql 2:',v2.query)
    #SELECT `ORMdemo_userinfos`.`ut_id`, COUNT(`ORMdemo_userinfos`.`id`) AS `utn`
    # FROM `ORMdemo_userinfos`
    # GROUP BY `ORMdemo_userinfos`.`ut_id`
    # HAVING COUNT(`ORMdemo_userinfos`.`id`) > 30
    # ORDER BY NULL

    #去重
    models.UserInfos.objects.values('ut_id').distinct()#mysql,sqllite不可传参
    models.UserInfos.objects.distinct('ut_id')#PostgreSQL传参

    #倒序
    models.UserInfos.objects.all().order_by('-id').reverse()#必须要有order_by，reverse才生效

    #查询其他数据库
    #models.UserInfo.objects.all().using('db2')

    #取时间字段并格式化
    models.UserInfos.objects.dates('ctime','day','DESC') #day:表示获取年月日，desc根据年月日倒序排列
    models.UserInfos.objects.dates('ctime', 'month', 'DESC')#month:表示获取年月-01，desc根据年月-01倒序排列
    models.UserInfos.objects.dates('ctime', 'year', 'DESC')#year:表示获取年-01-01，desc根据年-01-01倒序排列

    import pytz  #pytz.all_timezones显示出所有可填时区
    models.UserInfos.objects.datetimes('ctime', 'hour', 'DESC',tzinfo=pytz.timezone('Asia/Shanghai'))
    #可填字段：year,month,day,hour,minute,second
    #tzinfo:转换时区

    #聚合函数返回字典{n:1}
    models.UserInfos.objects.all().aggregate(n=Count('ut_id'))#表里有多少数据n就等于多少
    models.UserInfos.objects.all().aggregate(n=Count('ut_id',distinct=True))#去重后ut_id有多少，n就有多少

    #批量添加
    #传统添加，100次添加有100次commit
    obj = [
        models.UserInfos(name='xxx1',age=12,ut_id=1),
        models.UserInfos(name='xxx2',age=13,ut_id=2),
    ]
    models.UserInfos.objects.bulk_create(obj,10)#1次最多提交10个数据，100个数据提交10次，最多不超过999

    #存在查询，不存在添加
    obj,created = models.UserInfos.objects.get_or_create(
        name='root',
        age = 12,
        defaults={'ut_id':3,'ctime':'2019-01-01 01:01:01'})
    #如果有name=root and age = 12这条数据，就直接返回对象obj,和created：Ture/False
    #如果没有这条数据，就把defaults的添加进去

    return HttpResponse("aasa")


from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
def test_page(req):
    params = {}
    current_page = req.GET.get('page')
    userlist = models.UserInfos.objects.all()

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
    user_obj = models.UserInfos.objects.all()
    print(type(user_obj))
    page_obj = PageInfo(req.GET.get('page'),10,user_obj,req.path,5)
    userlist = page_obj.get_list()
    params['userlist'] = userlist
    params['page_obj'] = page_obj
    return render(req, 'test_page_self.html', params)

def test_page_self2(req,parm):
    print(parm)
    return HttpResponse('xxxx'+parm)

def test_page_self4(req,*args,**kwargs):
    print(*args,**kwargs)
    return HttpResponse(args)

#标记某一字符串为安全的
from django.utils.safestring import mark_safe
def test_mark(req):
    temp = "<a href='www.baidu.com'>百度</a>"
    new_temp = mark_safe(temp)
    return render(req, 'test_mark.html', {'new_temp':new_temp})
def test_mark(req):
    list_test = [1,2,3,4,5]
    return render(req, 'test_mark.html', {'list_test': list_test})

from django.urls import reverse
def test_mark2(req,a1):
    v = reverse('aaa',args=(a1,))# ->  /orm/test_mark2/222
    return HttpResponse(v)

def test_mark3(req,**kwargs):
    v = reverse('bbb',kwargs=kwargs)# ->  /orm/test_mark3/22/2222
    return HttpResponse(v)