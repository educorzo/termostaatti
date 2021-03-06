#!/usr/bin/env python
from crontab import CronTab

script = 'sudo /usr/bin/python /home/pi/termostaatti/main/script.py'

class CrontabJob:
    
    def __init__(self):
        self.cron = CronTab(user=True)
    
    def setTemperature(self, temperature):
        job = self.cron.new(command=script +' '+ temperature, comment='Termostaati')
        job.minute.every(1)
        self.cron.write()
    
    def getTemperature(self):
        job = self.cron.find_comment('Termostaati')
        if job :
            for jobs in job:
                print jobs
            return jobs.render()[68:70]
        else:
            return 0

    def deleteCronoJobs(self):
        self.cron.remove_all(comment='Termostaati')
        self.cron.write()
    
    def areCronoJobs(self):
        return self.cron.find_comment('Termostaati')