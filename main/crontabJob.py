#!/usr/bin/env python
from crontab import CronTab

script = 'sudo /usr/bin/python /home/pi/termostaatti/main/script.py'

class CrontabJob:
    
    def __init__(self):
        self.cron = CronTab()
    
    def setTemperature(self, temperature):
        job = self.cron.new(command=script +' '+ temperature, comment='Termostaati')
        job.minute.every(1)
        self.cron.write()
    
    def deleteCronoJobs(self):
        self.cron.remove_all()
    
    def areCronoJobs(self):
        return self.cron.find_comment('Termostaati')