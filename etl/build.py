import subprocess

# Define the list of commands to run
commands = [
    ['rm', 'automotives.db'], 
    ['python', 'etl/db_country_id.py'],
    ['python', 'etl/db_country_stat.py'],
    ['python', 'etl/db_manufacturers.py'],
    ['python', 'etl/db_cars.py'],
    ['python', 'etl/db_chiptuners.py'],
]

# Iterate through the commands and run each one
for command in commands:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f"Output for {command}:")
    print(stdout.decode())
    print(stderr.decode())

print("All ETL scripts run, your current directory should now contain 'automotives.db.' If it does not, check individual script outputs above (empty if successful).")
