#!/usr/bin/env python
from crontab import CronTab

cron = CronTab()
job = cron.new(command='sudo /usr/bin/python /home/pi/termostaatti/main/script.py 10')
job.minute.every(1)
cron.write()