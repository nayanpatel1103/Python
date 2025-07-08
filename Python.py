print("hello World")
# write a code to print "hello world" in Python
print("hello world")
#write a code to take input from user and print it
user_input = input("Please enter something: ")
print("You entered:", user_input)
# write a code to housekeep the temp folder daily   
import os
import shutil                           
def clean_temp_folder(temp_folder):
    if os.path.exists(temp_folder):
        for filename in os.listdir(temp_folder):
            file_path = os.path.join(temp_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
    else:
        print(f'Temp folder {temp_folder} does not exist.') 

        #write a code to clear a system queue in IBM MQ queue manager linux platform
import subprocess

def clear_ibm_mq_queue(queue_manager, queue_name):
    try:
        subprocess.run(['mqcleartmp', '-m', queue_manager, '-q', queue_name], check=True)
        print(f'Successfully cleared queue {queue_name} in queue manager {queue_manager}.')
    except subprocess.CalledProcessError as e:
        print(f'Failed to clear queue {queue_name}. Reason: {e}')   