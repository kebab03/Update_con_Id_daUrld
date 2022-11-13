import requests as rq
url="https://greetingsampl.herokuapp.com/drinks/1"
res=rq.get(url)
print(res.json())
print(type(res.json()))
mydict=res.json()
print(mydict.keys())
for key in mydict.keys():
    print(key)
    print(mydict[key])