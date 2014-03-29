py_wap_alipay
=============
##介绍
---
支付宝（无线）WAP端 python版本，即时到账接口

core.py 文件里排序，过滤等函数引用自 [python-alipay](https://github.com/yefei/python-alipay) 这个版本的代码

My Email: <copuzzle@gmail.com>   
  
 
##使用
----
- ####即时到账  
```
	from wap_alipay import submit  
	pay_url = submit.get_pay_ur(tn, subject, body, total_fee)
```
	tn - 'out_trade_no', 网站订单系统中唯一订单匹配号   
	subject - 'subject', 订单名称   
	price - 'price', 商品单价

	返回应该跳转的支付宝链接

