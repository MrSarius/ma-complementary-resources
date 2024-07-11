import subprocess
import time

def ping(host, timeout=1):
    # Command to ping; '-c 1' means send only one packet
    command = ['ping', '-c', '1', host]
    
    try:
        # Execute the ping command with a timeout
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True, timeout=timeout)
        if "0% packet loss" in output:
            print("Pinging google successful")
            # print(output)
    except subprocess.TimeoutExpired:
        print(f"Ping request timed out after {timeout} seconds.")
    except subprocess.CalledProcessError as e:
        print("Failed to ping:")
        print(e.output)

while True:
    ping('216.58.206.67') # Google server
    time.sleep(5)

