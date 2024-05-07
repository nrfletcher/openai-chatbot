import subprocess

# Define the list of commands to run
commands = [
    ['python', 'etl/build.py']
]

# Iterate through the commands and run each one
for command in commands:
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f"Output for {command}:")
    print(stdout.decode())
    print(stderr.decode())

print("Build script finished execution")
