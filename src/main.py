# main.py
import os
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dashboard import run_dashboard, add_alert


SUSPICIOUS_EXTENSIONS = [".locked", ".crypt", ".enc"]

class RansomwareHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            self.check_file(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            self.check_file(event.src_path)

    def check_file(self, filepath):
        _, ext = os.path.splitext(filepath)
        if ext.lower() in SUSPICIOUS_EXTENSIONS:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"Suspicious file detected: {filepath}"
            print(f"[ALERT] {message} at {timestamp}")  # Terminal alert
            add_alert(message, timestamp)  # Dashboard alert

def monitor_folder(folder_path):
    event_handler = RansomwareHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    print(f"[INFO] Monitoring started on: {folder_path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_monitor = r"C:\Users\DILLIRAJ\Downloads\ransomware-detector\test_folder"

    # Start the dashboard
    run_dashboard()
    print("[INFO] Dashboard running at http://127.0.0.1:5000/")

    # Start monitoring folder
    monitor_folder(folder_to_monitor)
