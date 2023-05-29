from crontab import CronTab

# Create a new cron tab
cron = CronTab(user='root')  # Replace with the desired username

# Add a new cron job
job = cron.new(command='python /path/to/cron_job.py')  # Replace with the actual path to your cron_job.py script
job.setall('0 9 * * *')  # Set the cron schedule

# Write the cron tab
cron.write()
