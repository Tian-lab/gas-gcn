import os
import time
import pynvml
import smtplib
from email.mime.text import MIMEText
from email.header import Header
pynvml.nvmlInit()

sender = '18292875642@163.com'
password = 'xiatian730'
addressed_eamil = '2489925838@qq.com'


def mail():
    try:
        msg = MIMEText('GPU空闲！请注意！', 'plain', 'utf-8')
        msg['From'] = Header('xxx', 'utf-8')
        msg['To'] = Header('Vincent', 'utf-8')
        msg['Subject'] = Header('发送GPU空闲通知', 'utf-8')

        server = smtplib.SMTP_SSL("smtp.163.com", 465)
        server.login(sender, password)
        server.sendmail(sender, addressed_eamil, msg.as_string ())
        server.quit()
    except Exception as e:
        print(e)


def print_ts(message):
    print("[%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message))


def run(interval, command=None):
    while True:
        try:
            # sleep for the remaining seconds of interval
            time_remaining = interval-time.time()%interval
            #print_ts("Sleeping until %s (%s seconds)..."%((time.ctime(time.time()+time_remaining)), time_remaining))
            time.sleep(time_remaining)
            #print_ts("Report!")
            #print_ts("-"*100)
            handle = pynvml.nvmlDeviceGetHandleByIndex(0)
            meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
            if meminfo.free >= 10000000000:
                break
        except Exception as e:
            print(e)


if __name__ == "__main__":
    interval = 5
    print_ts("Master! Start watching.")
    command = r"ls"
    run(interval, command=command)
    com = 'python main.py --config ./config/nturgbd-cross-view/train.yaml'
    os.system(com)
