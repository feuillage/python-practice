# -*- coding: utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

import random, string

def random_string(num, length=10):
    file = open('code.txt', 'wb')
    for i in range(num):
	    chars = string.ascii_letters + string.digits
	    s = [random.choice(chars) for i in range(length)]
	    code = ''.join(s) + '\n'
	    file.write(code.encode('utf-8'))
    file.close
	
if __name__ == '__main__':
    random_string(200)