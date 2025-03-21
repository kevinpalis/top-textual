import subprocess

def get_process_data():
    result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
    lines = result.stdout.strip().split("\n")
    return [line.split(None, 10) for line in lines]