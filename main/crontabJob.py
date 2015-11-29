#!/usr/bin/env python
from crontab import CronTab

#cron = CronTab()
#job = cron.new(command='sudo /usr/bin/python /home/pi/termostaatti/main/script.py 10')
#job.minute.every(1)
#cron.write()
script = 'sudo /usr/bin/python /home/pi/termostaatti/main/script.py'

class CrontabJob:
    
    def __init__(self):
        self.cron = CronTab()

    def setTemperature(self, temperature):
        job = self.cron.new(command=script + temperature)
        job.minute.every(1)
        self.cron.write()

    def deleteCronoJobs(self):
        self.cron.remove_all()