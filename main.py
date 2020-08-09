import time, platform
from datetime import datetime as dt, timedelta as td

os_name = platform.system()

if os_name == 'Linux':
    hosts_path  = '/etc/hosts'
elif os_name == 'Windows':
    hosts_path  = r"c:\Windows\System32\Drivers\etc\hosts"
elif os_name == 'Darwin':
    hosts_path  = '/private/etc/hosts'

redirect        = "127.0.0.1"
websites_list   = ['facebook.com', 'www.facebook.com', 'twitter.com', 'www.twitter.com', 'youtube.com', 'www.youtube.com', 'egy.best', 'mail.google.com', 'www.google.com', 'google.com']


print("Please Enter The Working Hours")

try:
    hours           = int(input())
except:
    print("Enter Integer Number Please")
    exit()

start_time      = dt.now()
end_time        = start_time + td(hours=hours)

while True:
    if start_time <= dt.now() < end_time:
        print('Working Time...')
        
        with open(hosts_path, 'r+') as f:
            content         = f.read()

            for website in websites_list:
                if website in content:
                    pass
                else:
                    f.write("\n{} {}".format(redirect, website))
    else:
        with open(hosts_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    f.write(line)
            f.truncate()
        break
    time.sleep(5)

print("Break Time...")