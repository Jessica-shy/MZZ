#生成 200 个激活码（或者优惠券）

import random
ALPHAS = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
code = ''
randomdict = {}
length = len(ALPHAS)
for keys in range(200):
    for i in range(20):#假设生成20位的激活码
        code += random.choice(ALPHAS)
        randomdict[keys+1] = code
    code = ''
print(randomdict) 


 