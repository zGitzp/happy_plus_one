import requests
from bs4 import BeautifulSoup
 
##Server酱更改为PUSHPLUS，此段代码注释了###Server酱推送模块，PUSH_KEY替换自己的
#def send_message_fangtang(_item,_message):
#        PUSH_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  #
#        api = 'https://sctapi.ftqq.com/' + PUSH_KEY + '.send'
#        _d = {
#                "title": _item,
#                "desp": _message
#                }
#       req = requests.post(api,data = _d)
#       #print(req.text)
 
#PushPlus推送模块
def pushplus(_item, _message):
    token = sys.argv[1]    #隐藏token码，参考楼下代码
    api = 'http://www.pushplus.plus/send'
    _d = {
        "token": token,
        "title": _item,
        "content": _message
    }
    req = requests.post(api, data=_d)
    #print(req.text)
 
#爬取代码
url='https://steamstats.cn/xi'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.41'}
 
r=requests.get(url,headers=headers)
r.raise_for_status()
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, "html.parser")
tbody=soup.find('tbody')
#print(tbody)
if tbody is not None:
    tr=tbody.find_all('tr')
    i=1
    desp="&#10084;今日喜加一&#10084;"+'\n'
    for tr in tr:
        td=tr.find_all('td')
        name=td[1].string.strip().replace('\n', '').replace('\r', '')
        gametype=td[2].string.replace(" ","").replace('\n', '').replace('\r', '')
        start=td[3].string.replace(" ","").replace('\n', '').replace('\r', '')
        end=td[4].string.replace(" ","").replace('\n', '').replace('\r', '')
        time=td[5].string.replace(" ","").replace('\n', '').replace('\r', '')
        oringin=td[6].find('span').string.replace(" ","").replace('\n', '').replace('\r', '')
        sp=str(td[6]).split('"')
        http=sp[3]
     
        desp=desp+"序号："+str(i)+'\r'+"游戏名称："+name+'\r'+"类型："+gametype+'\r'+"开始时间："+start+'\r'+"结束时间："+end+'\r'+"是否永久："+time+'\r'+"平台："+oringin+'\r'+"链接："+http+'\r'
else:
        desp=desp+"今日没有游戏可领!"
#send_message_fangtang("今日喜加一",desp)
pushplus("今日喜加一",desp)
print(desp）  
