import json
import driver
import time
from apscheduler.schedulers.background import BackgroundScheduler


def day_use():
    with open('test.txt', 'r') as f:
        data = json.read(f)

    for item in data:
        # print(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
        # 发送POST请求
        driver.Post(item['license_id'], item['region_id'], item['price_per_month'], item['minimum_stay_month'], item['desc'])
        time.sleep(15)
        print("等待15秒")



import time

def job():
    print("现在是10:00,该执行任务了")
    day_use()

# 创建一个调度器
scheduler = BackgroundScheduler()

# 使用cron触发器在每天的21:43执行job函数
scheduler.add_job(job, 'cron', hour=10, minute=00)

# 启动调度器
scheduler.start()

# 无限循环，每次循环都暂停一段时间，以防止CPU占用过高
while True:
    time.sleep(1)
