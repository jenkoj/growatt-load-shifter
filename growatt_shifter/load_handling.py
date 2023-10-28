import subprocess

def handle_load(script_file_name):
    """
    to turn on use load_on_script path
    to turn off use load_off_script path
    """
    # Execute the Node.js script using subprocess
    process = subprocess.Popen(['node', script_file_name], 
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    # Wait for the process to finish and capture the output
    stdout, stderr = process.communicate()

    # Decode the output from bytes to string
    stdout = stdout.decode('utf-8')
    stderr = stderr.decode('utf-8')

    # Print the output
    print('Standard Output:')
    print(stdout)

    print('Standard Error:')
    print(stderr)

    # Check the return code
    return_code = process.returncode
    print('Return Code:', return_code)
    