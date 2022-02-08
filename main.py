import yagmail
import os
import time
from datetime import datetime as dt

sender="testmycode2022@gmail.com"
receiver="helloadish007@gmail.com"

subject=" emailing every 10 seconds "

content="""
Hi,

youll' be receiving emails every 60 seconds

Thanks
Testmycode2022

"""
while True:
  now=dt.now()
  if now.hour == 2 and now.minute == 36:
    yag=yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

    yag.send(to=receiver, subject= subject, contents=content)

    print("Email send successfully!")
    time.sleep(60)