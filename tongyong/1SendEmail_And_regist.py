import requests
import random
import string
import base64
w = open("订阅链接.txt", "w")
#机场链接
jichang_link = 'https://ni8.me/'
for i in range(1,9):
    url_regist= jichang_link+'api/v1/passport/auth/register'

    qq_num = random.randint(1, 999999999999)
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    qq_email = "%d@qq.com" % qq_num

    data = {
        "email": qq_email,
        "password": ran_str,
    }

    r2 = requests.post(url=url_regist,data=data)

    print(qq_email,ran_str)
    print(r2)

    url_login = jichang_link+"api/v1/passport/auth/login"

    resp = requests.post(url=url_login,data=data)

    resp_token = resp.json()['data']['token']
    sub_lianjie = jichang_link+"api/v1/client/subscribe?token=" + resp_token
    print(sub_lianjie)
    w.write(sub_lianjie)
    # 换行
    w.write('\n')
w.close()

o = open("订阅链接.txt", encoding='utf-8')
l = open("节点信息.txt","wb+") #wb+打开会删光之前的内容

#解密，然后把订阅链接放一起
while True:
    url = o.readline()
    if url:
        #访问订阅链接，以'utf-8'拿到订阅链接的base64编码
        r = requests.get(url).content.decode('utf-8')
        #解码，把base64编码变成节点链接
        jiedian_link = base64.b64decode(r)
        #把拿到的节点链接写到一个文件里
        l.write(jiedian_link)
    else:
        break
o.close()
l.close()

#加密
m = open("节点信息.txt","rb+")
n = open("fin","wb+")
str1 = m.read()
str64 = base64.b64encode(str1)
n.write(str64)

m.close()
n.close()
