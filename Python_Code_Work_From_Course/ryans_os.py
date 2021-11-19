import os

CURRENT_SSH = os.getenv("SSH_CONNECTION")

output = f"The IP Address of the user that is accessing this machine is {CURRENT_SSH}"

print(output)

