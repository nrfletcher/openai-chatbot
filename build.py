import subprocess

# Define the list of commands to run
commands = [
    ['python', 'db_country_id.py'],
    ['python', 'db_country_stat.py'],
    ['python', 'db_manufacturers.py'],
    ['python', 'db_cars.py'],
    ['python', 'db_chiptuners.py'],
]

# Iterate through the commands and run each one
for command in commands:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f"Output for {command}:")
    print(stdout.decode())
    print(stderr.decode())

print("Successfully built project")
