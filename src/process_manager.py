
import psutil
import os
import signal

def get_processes_touching(path):
    """
    Returns a list of processes that have open file handles in the given path.
    """
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            for file in proc.open_files():
                if file.path.startswith(path):
                    suspicious.append(proc)
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            continue
    return suspicious


def kill_process_tree(pid):
    """
    Kill a process and all its children.
    """
    try:
        parent = psutil.Process(pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()
    except psutil.NoSuchProcess:
        pass
