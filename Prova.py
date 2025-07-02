def build_large_string():
    result = ""
    for i in range(10000):
        result += str(i) + ","
    return result


token = "default"

def update_token():
    token = get_new_token()  # This will not affect the global token variable
    print("Token updated:", token)

def get_new_token():
    return "new_token_value"

import subprocess

def run_backup(path):
    command = f"tar -czf backup.tar.gz {path}"
    subprocess.call(command, shell=True)


def parse_number(val):
    if val is not None:
        try:
            return int(val)
        except ValueError:
            return None
    else:
        return None


def risky_operation():
    try:
        result = do_something_critical()
        return result
    except:
        return None

def do_something_critical():
    # Simulating a critical operation that might fail
    raise Exception("Critical failure occurred!")