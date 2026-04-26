import subprocess
import time
import threading

class Watchdog:
    def __init__(self, host="1.1.1.1", interval=10):
        self.host = host
        self.interval = interval
        self.running = False
        self.callback = None

    def start(self, callback):
        self.running = True
        self.callback = callback
        threading.Thread(target=self._watch, daemon=True).start()

    def stop(self):
        self.running = False

    def _watch(self):
        while self.running:
            if not self._ping():
                if self.callback:
                    self.callback()
            time.sleep(self.interval)

    def _ping(self):
        try:
            result = subprocess.run(["ping", "-n", "1", "-w", "2000", self.host], capture_output=True, text=True)
            return result.returncode == 0
        except:
            return False
