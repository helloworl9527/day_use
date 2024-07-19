import requests
def Post(license_id,region_id,price_per_month,minimum_stay_month,desc):
    Lid = license_id   #服务
    Rid = region_id    #地区
    Pm = price_per_month  #每月价格
    msm = minimum_stay_month  #至少订阅时间
    dc = desc  #描述


    # 创建请求头字典
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie": "_gid=GA1.2.654887045.1721183570; XSRF-TOKEN=eyJpdiI6ImhcL3V3cjg2VXI3dGRcL1VNUm52VEhTdz09IiwidmFsdWUiOiIwZXdDamJ2NEl3TWNHREdOZDFGMGNuYjhvaitrZzVhN01pNFl0VVIxWE5hTUkzMFFPUkdtZ3Rocm44XC81U0MzcGxyYjFZM3pqY3FjMElRK3JIK1pJd3c9PSIsIm1hYyI6ImJmY2FjNzY4MTllNDE4YTg2ZjlkMTI4NGVlYWRkN2ZmYWU3OGQ5YjQzZDNkZWQ5YTdlOWI4NjY2YzczMWVjYmYifQ%3D%3D; laravel_session=eyJpdiI6IjAxQ2taUGpFVVwvZGY3SDRZdjE3Y0FnPT0iLCJ2YWx1ZSI6IjRJbGEwVjJ3NG1hY25nN2pJaHlZdTBhb2Z3NitRb0w2cGpyNGdXaEI5YVwvTFBqc0I5ZXJnWng3UEhuK04wNjJjRDd5aUFzdEVMQmtrY1E2a0Q3ajBjZz09IiwibWFjIjoiOTVhYzM1MDczZTljOTgyNmI2NTQ0NTc1YjNkYTJlNzEzOWIzMDEyMzYwZGZlNzVjMDE1YTFmN2Q1MmYxOTllMCJ9; _ga_R7KG8B8WSS=GS1.1.1721183570.1.1.1721183617.0.0.0; _ga=GA1.1.1760669033.1721183570",
        "Host": "daixiahu.co",
        "Origin": "https://daixiahu.co",
        "Referer": "https://daixiahu.co/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "X-XSRF-TOKEN": "eyJpdiI6ImhcL3V3cjg2VXI3dGRcL1VNUm52VEhTdz09IiwidmFsdWUiOiIwZXdDamJ2NEl3TWNHREdOZDFGMGNuYjhvaitrZzVhN01pNFl0VVIxWE5hTUkzMFFPUkdtZ3Rocm44XC81U0MzcGxyYjFZM3pqY3FjMElRK3JIK1pJd3c9PSIsIm1hYyI6ImJmY2FjNzY4MTllNDE4YTg2ZjlkMTI4NGVlYWRkN2ZmYWU3OGQ5YjQzZDNkZWQ5YTdlOWI4NjY2YzczMWVjYmYifQ==",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\""
    }

    # 创建JSON数据字典
    data = {
        "bus_request_type": "is_driver",
        "license": "ChatGPT Plus",
        "region": "美区",
        "price_per_month": Pm,
        "minimum_stay_month": msm,
        "is_hide_contact": True,
        "expired_days": 14,
        "desc": dc,
        "contact_email": "",
        "contact_wx": "",
        "leftDrawerOpen": True,
        "regionOptions": ["所有地区","国区","港区","台区","日区","美区","土区","其他区"],
        "licenseOptions": ["所有服务","Netflix","Spotify Premium","ChatGPT Plus","Surge","1Password","Youtube Premium","Youtube TV","Apple Music","Setapp","Office365","TIDAL","Disney+","Hulu","HBO Now","HBO Go","KKBox","端传媒","其他"],
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvZGFpeGlhaHUuY29cL2F1dGhcL2FmdGVyX2xvZ2luIiwiaWF0IjoxNzIxMTgzNjE2LCJleHAiOjM2MTQ1OTkxNzYsIm5iZiI6MTcyMTE4MzYxNiwianRpIjoiejNscVF3UFpQNTNZMkx4dSIsInN1YiI6MTI2MzgsInBydiI6Ijg3ZTBhZjFlZjlmZDE1ODEyZmRlYzk3MTUzYTE0ZTBiMDQ3NTQ2YWEifQ.BdEPLsiKh7t3mNKNBrefjjUhguTn8MwtWhv5RI0vR7k",
        "region_id": Rid,
        "license_id": Lid
    }

    # 发送POST请求
    response = requests.post("https://daixiahu.co/api/bus", headers=headers, json=data)

    # 打印响应
    if response.status_code == 200:
        print("发布成功")
    else:
        print("发布失败")


# Post("3","999","8","1","")