import json
import driver
import time

with open('test.txt', 'r') as f:
    data = json.read(f)

for item in data:
    # print(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
    # 发送POST请求
    driver.Post(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
    time.sleep(15)
    print("等待15秒")
