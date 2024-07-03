import subprocess
import sys

def run_as_admin():
    if sys.platform.startswith('win'):
        try:
            powershell_script = '''
            Start-Process -FilePath '{python_exec}' -ArgumentList 'cmdspam.py' -Verb runAs
            '''.format(python_exec=sys.executable)

            subprocess.check_call(["powershell.exe", "-Command", powershell_script])
            sys.exit()
        except subprocess.CalledProcessError as e:
            print(f"Failed to elevate: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Failed to elevate: {e}")
            sys.exit(1)
run_as_admin()

