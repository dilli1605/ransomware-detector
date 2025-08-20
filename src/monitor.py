import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Logging setup
logger = logging.getLogger("monitor")

class RansomwareHandler(FileSystemEventHandler):
    def __init__(self, alert_callback):
        self.alert_callback = alert_callback

    def on_modified(self, event):
        if not event.is_directory:
            logger.info(f"[MODIFIED] {event.src_path}")
            # Fake ransomware check
            if event.src_path.endswith(".locked") or event.src_path.endswith(".encrypted"):
                logger.warning(f"⚠ Suspicious encryption detected: {event.src_path}")
                self.alert_callback(event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"[CREATED] {event.src_path}")
            if event.src_path.endswith(".locked") or event.src_path.endswith(".encrypted"):
                logger.warning(f"⚠ Suspicious file creation detected: {event.src_path}")
                self.alert_callback(event.src_path)

def start_monitor(path, alert_callback):
    event_handler = RansomwareHandler(alert_callback)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logger.info(f"✅ Monitoring started on: {path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
