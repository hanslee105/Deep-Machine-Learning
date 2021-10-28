#作業1
import requests
import codecs
#1.-------------requests.get reading a web page
r1=requests.get(
    "http://teaching.bo-yuan.net/test/requests/",
    headers={
        "Cookie":"PHPSESSID=otiv9jtki4rt0amdqmis05ckb6",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
    }
) #answer: "缺少參數「action」。"

#2.-------------requests.post reading a web page
# r1=requests.post(
#     "http://teaching.bo-yuan.net/test/requests/",
#     headers={
#         "Cookie":"PHPSESSID=otiv9jtki4rt0amdqmis05ckb6",
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
#     }
# ) #answer: ""

#3.-------------requests.delete reading a web page
# r1=requests.delete(
#     "http://teaching.bo-yuan.net/test/requests/",
#     headers={
#         "Cookie":"PHPSESSID=otiv9jtki4rt0amdqmis05ckb6",
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
#     }
# ) #answer: ""

#4.-------------requests.put reading a web page
# r1=requests.put(
#     "http://teaching.bo-yuan.net/test/requests/",
#     headers={
#         "Cookie":"PHPSESSID=otiv9jtki4rt0amdqmis05ckb6",
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
#     }
# ) #answer: ""

#5.-------------requests.patch reading a web page
# r1=requests.patch(
#     "http://teaching.bo-yuan.net/test/requests/",
#     headers={
#         "Cookie":"PHPSESSID=otiv9jtki4rt0amdqmis05ckb6",
#         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"
#     }
# ) #answer: ""
print(r1.text)