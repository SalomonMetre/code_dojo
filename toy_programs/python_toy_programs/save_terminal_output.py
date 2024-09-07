import subprocess

# Run a command and capture its output
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

# Write the output to a file
with open('output.txt', 'w') as file:
    file.write(result.stdout)
