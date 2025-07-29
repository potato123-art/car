#coding:utf-8
__author__ = "ila"
from django.db import models
from .model import BaseModel
from datetime import datetime
class caigoujinhuodan(BaseModel):#采购进货单
	__doc__ = u'''caigoujinhuodan'''

	__authTables__ = {'zhanghao': 'yuangong', }
	__tablename__ = 'caigoujinhuodan'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	caigoudanhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='采购单号' )
	peijianbianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件编号' )
	peijianmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件名称' )
	shuliang=models.IntegerField ( null=False, unique=False,verbose_name='数量' )
	jiage=models.IntegerField ( null=False, unique=False,verbose_name='价格' )
	jine=models.IntegerField ( null=False, unique=False,verbose_name='金额' )
	tupian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='图片' )
	riqi=models.DateField ( null=True, unique=False,verbose_name='日期' )
	beizhu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='备注' )
	zhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='账号' )
	xingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='姓名' )

	class Meta:
		db_table = 'caigoujinhuodan'
		verbose_name = verbose_name_plural = '采购进货单'


class cheliangxinxi(BaseModel):#车辆信息
	__doc__ = u'''cheliangxinxi'''
	__authTables__ = {}
	__tablename__ = 'cheliangxinxi'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	cheliangbianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车辆编号' )
	cheliangmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车辆名称' )
	chepaihao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车牌号' )
	pinpai=models.CharField ( max_length=255, null=False, unique=False, verbose_name='品牌' )
	xinghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='型号' )
	tupian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='图片' )
	jieshao=models.TextField   ( null=False, unique=False,  verbose_name='介绍' )

	class Meta:
		db_table = 'cheliangxinxi'
		verbose_name = verbose_name_plural = '车辆信息'


class kehu(BaseModel):#客户
	__doc__ = u'''kehu'''
	__loginUser__ = 'kehuzhanghao'
	__authTables__ = {}
	__tablename__ = 'kehu'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	kehuzhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='客户账号' )
	mima=models.CharField ( max_length=255, null=False, unique=False, verbose_name='密码' )
	kehuxingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='客户姓名' )
	shouji=models.CharField ( max_length=255, null=False, unique=False, verbose_name='手机' )
	youxiang=models.CharField ( max_length=255, null=False, unique=False, verbose_name='邮箱' )
	zhaopian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='照片' )

	class Meta:
		db_table = 'kehu'
		verbose_name = verbose_name_plural = '客户'


class peijianleixing(BaseModel):#配件类型
	__doc__ = u'''peijianleixing'''
	__authTables__ = {}
	__tablename__ = 'peijianleixing'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	leixing=models.CharField ( max_length=255, null=False, unique=False, verbose_name='类型' )

	class Meta:
		db_table = 'peijianleixing'
		verbose_name = verbose_name_plural = '配件类型'


class peijianlingyong(BaseModel):#配件领用
	__doc__ = u'''peijianlingyong'''

	__authTables__ = {'weixiuzhanghao': 'weixiuyuan', }
	__tablename__ = 'peijianlingyong'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	lingyongbianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='领用编号' )
	cheliangmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车辆名称' )
	chepaihao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车牌号' )
	pinpai=models.CharField ( max_length=255, null=False, unique=False, verbose_name='品牌' )
	weixiuxiangmu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修项目' )
	peijianmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件名称' )
	shuliang=models.IntegerField ( null=False, unique=False,verbose_name='数量' )
	tupian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='图片' )
	lingyongriqi=models.DateField ( null=True, unique=False,verbose_name='领用日期' )
	beizhu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='备注' )
	weixiuzhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修账号' )
	xingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='姓名' )

	class Meta:
		db_table = 'peijianlingyong'
		verbose_name = verbose_name_plural = '配件领用'


class peijianshenqing(BaseModel):#配件申请
	__doc__ = u'''peijianshenqing'''

	__authTables__ = {'weixiuzhanghao': 'weixiuyuan', }
	__tablename__ = 'peijianshenqing'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	shenqingbianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='申请编号' )
	peijianbianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件编号' )
	peijianmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件名称' )
	shuliang=models.CharField ( max_length=255, null=False, unique=False, verbose_name='数量' )
	xiulidanhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='修理单号' )
	shenqingriqi=models.DateField ( null=True, unique=False,verbose_name='申请日期' )
	weixiuzhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修账号' )
	xingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='姓名' )
	sfsh=models.CharField ( max_length=255, null=False, unique=False, verbose_name='是否审核' )
	shhf=models.TextField   ( null=False, unique=False,  verbose_name='审核回复' )

	class Meta:
		db_table = 'peijianshenqing'
		verbose_name = verbose_name_plural = '配件申请'


class qichepeijiankucun(BaseModel):#汽车配件库存
	__doc__ = u'''qichepeijiankucun'''
	__authTables__ = {}
	__tablename__ = 'qichepeijiankucun'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	peijianbianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件编号' )
	peijianmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件名称' )
	peijianleixing=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件类型' )
	shuliang=models.IntegerField ( null=False, unique=False,verbose_name='数量' )
	jiage=models.IntegerField ( null=False, unique=False,verbose_name='价格' )
	jine=models.CharField ( max_length=255, null=False, unique=False, verbose_name='金额' )
	tupian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='图片' )
	riqi=models.DateField ( null=True, unique=False,verbose_name='日期' )
	beizhu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='备注' )

	class Meta:
		db_table = 'qichepeijiankucun'
		verbose_name = verbose_name_plural = '汽车配件库存'


class qichexiulidan(BaseModel):#汽车修理单
	__doc__ = u'''qichexiulidan'''

	__authTables__ = {'weixiuzhanghao': 'weixiuyuan', }
	__tablename__ = 'qichexiulidan'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	xiulidanhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='修理单号' )
	cheliangmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车辆名称' )
	chepaihao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车牌号' )
	pinpai=models.CharField ( max_length=255, null=False, unique=False, verbose_name='品牌' )
	weixiuxiangmu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修项目' )
	peijianmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='配件名称' )
	xiulifei=models.IntegerField ( null=False, unique=False,verbose_name='修理费' )
	xiulixiaoshi=models.IntegerField ( null=False, unique=False,verbose_name='修理小时' )
	weixiuzonge=models.IntegerField ( null=False, unique=False,verbose_name='维修总额' )
	weixiuzhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修账号' )
	xingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='姓名' )
	songxiuriqi=models.DateField ( null=True, unique=False,verbose_name='送修日期' )

	class Meta:
		db_table = 'qichexiulidan'
		verbose_name = verbose_name_plural = '汽车修理单'


class qichexiulitaizhang(BaseModel):#汽车修理台账
	__doc__ = u'''qichexiulitaizhang'''

	__authTables__ = {'weixiuzhanghao': 'weixiuyuan', }
	__tablename__ = 'qichexiulitaizhang'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	xuhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='序号' )
	cheliangmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车辆名称' )
	chepaihao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车牌号' )
	weixiuxiangmu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修项目' )
	lingjian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='零件' )
	weixiuzonge=models.IntegerField ( null=False, unique=False,verbose_name='维修总额' )
	lingjianfei=models.IntegerField ( null=False, unique=False,verbose_name='零件费' )
	zongji=models.IntegerField ( null=False, unique=False,verbose_name='总计' )
	weixiuzhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修账号' )
	xingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='姓名' )

	class Meta:
		db_table = 'qichexiulitaizhang'
		verbose_name = verbose_name_plural = '汽车修理台账'


class weixiuxiangmu(BaseModel):#维修项目
	__doc__ = u'''weixiuxiangmu'''
	__authTables__ = {}
	__tablename__ = 'weixiuxiangmu'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	xiangmubianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='项目编号' )
	weixiuxiangmu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修项目' )
	jiage=models.IntegerField ( null=False, unique=False,verbose_name='价格' )
	tupian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='图片' )
	riqi=models.DateField ( null=True, unique=False,verbose_name='日期' )
	xiangqing=models.TextField   ( null=False, unique=False,  verbose_name='详情' )

	class Meta:
		db_table = 'weixiuxiangmu'
		verbose_name = verbose_name_plural = '维修项目'


class weixiuyuan(BaseModel):#维修员
	__doc__ = u'''weixiuyuan'''
	__loginUser__ = 'weixiuzhanghao'
	__authTables__ = {}
	__tablename__ = 'weixiuyuan'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	weixiuzhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修账号' )
	mima=models.CharField ( max_length=255, null=False, unique=False, verbose_name='密码' )
	xingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='姓名' )
	xingbie=models.CharField ( max_length=255, null=False, unique=False, verbose_name='性别' )
	shouji=models.CharField ( max_length=255, null=False, unique=False, verbose_name='手机' )
	youxiang=models.CharField ( max_length=255, null=False, unique=False, verbose_name='邮箱' )
	zhaopian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='照片' )

	class Meta:
		db_table = 'weixiuyuan'
		verbose_name = verbose_name_plural = '维修员'


class weixiuyuyue(BaseModel):#维修预约
	__doc__ = u'''weixiuyuyue'''

	__authTables__ = {'kehuzhanghao': 'kehu', }
	__tablename__ = 'weixiuyuyue'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	yuyuebianhao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='预约编号' )
	cheliangmingcheng=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车辆名称' )
	chepaihao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='车牌号' )
	pinpai=models.CharField ( max_length=255, null=False, unique=False, verbose_name='品牌' )
	weixiuxiangmu=models.CharField ( max_length=255, null=False, unique=False, verbose_name='维修项目' )
	jiage=models.IntegerField ( null=False, unique=False,verbose_name='价格' )
	yuyueshijian=models.DateField ( null=True, unique=False,verbose_name='预约时间' )
	kehuzhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='客户账号' )
	kehuxingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='客户姓名' )
	shouji=models.CharField ( max_length=255, null=False, unique=False, verbose_name='手机' )

	class Meta:
		db_table = 'weixiuyuyue'
		verbose_name = verbose_name_plural = '维修预约'


class xiangmuleixing(BaseModel):#项目类型
	__doc__ = u'''xiangmuleixing'''
	__authTables__ = {}
	__tablename__ = 'xiangmuleixing'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	leixing=models.CharField ( max_length=255, null=False, unique=False, verbose_name='类型' )

	class Meta:
		db_table = 'xiangmuleixing'
		verbose_name = verbose_name_plural = '项目类型'


class yuangong(BaseModel):#员工
	__doc__ = u'''yuangong'''
	__loginUser__ = 'zhanghao'
	__authTables__ = {}
	__tablename__ = 'yuangong'
	__authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段 
	__sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面
	__authSeparate__='否'#后台列表权限
	__thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
	__intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
	__browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
	__foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
	__foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
	__isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
	addtime=models.DateTimeField ( null=True, unique=False,verbose_name='创建时间' )
	zhanghao=models.CharField ( max_length=255, null=False, unique=False, verbose_name='账号' )
	mima=models.CharField ( max_length=255, null=False, unique=False, verbose_name='密码' )
	xingming=models.CharField ( max_length=255, null=False, unique=False, verbose_name='姓名' )
	xingbie=models.CharField ( max_length=255, null=False, unique=False, verbose_name='性别' )
	shouji=models.CharField ( max_length=255, null=False, unique=False, verbose_name='手机' )
	youxiang=models.CharField ( max_length=255, null=False, unique=False, verbose_name='邮箱' )
	zhaopian=models.CharField ( max_length=255, null=False, unique=False, verbose_name='照片' )

	class Meta:
		db_table = 'yuangong'
		verbose_name = verbose_name_plural = '员工'



