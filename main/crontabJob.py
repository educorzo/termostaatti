#!/usr/bin/env python
from crontab import CronTab

cron = CronTab()
job = cron.new(command='script.py')
job.minute.every(1)
