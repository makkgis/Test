from crontab import CronTab
import os, sys

# create a new daily cron object
daily = CronTab()
# we then set the path for the absolute path for the 
# package files
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
# this command runs our daily script
cmd = '/usr/bin/python %s/world_shape.py' % dname
# we don't want multiple commands, remove just in case. There is no impact 
# if the job doesn't already exist
cron_job = daily.find_command(cmd)
daily.remove_all(cmd) 
#daily.minute.every(1)
# we can also set the default user e.g. (user='root'), in this case, we pull current
job = daily.new(command=cmd, comment='This command runs the daily process')
# set the job recurrence, in this case every 24 hours
# every day at 12pm
job.minute.on(42)
job.hour.on(18)


# write the job into cron
daily.write()
# log the file output
print daily.render()


 
