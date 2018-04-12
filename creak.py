#http://www.tfent.cn/sign/show?id=1
import httplib
import gzip
import StringIO
import time
data={
    'Host': 'www.tfent.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.tfent.cn/sign/show?id=1',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '6',
    'Cookie': 'UM_distinctid=15d45add7fdc5-0b82538890d3ac8-49556d-fa000-15d45add7ff264; CNZZDATA1255363484=1597157921-1500109055-http%253A%252F%252Fwww.tfent.cn%252F%7C1500265863; aliyungf_tc=AQAAAAmLwWXv5g0Ap/okeKY1ZGv91nMz; PHPSESSID=2sa2jbfss0nq3p2poku59pd4l6; think_language=zh-CN',
    'Connection': 'keep-alive'
}
t=0
while 1:
    t=t+1
    url = "http://www.tfent.cn/sign/getbuycode"
    conn = httplib.HTTPConnection("www.tfent.cn")
    conn.request(method="POST",url=url,body="area=2",headers=data)
    response = conn.getresponse()
    res= response.read()
    if "refresh" in res:
        res="refresh"
    else:
        if "502" in res:
            res="502"
        else:
            if "请先登录" in res:
                res="denglu"
            else :
                res = gzip.GzipFile(fileobj=StringIO.StringIO(res), mode="r").read()
    print(res.decode('unicode-escape').encode('utf-8'))
    print (t)
