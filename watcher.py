import time,hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
seen={}
class LogHandler(FileSystemEventHandler):
    def __init__(self,cb): self.cb=cb
    def on_modified(self,event):
        if event.is_directory:return
        try:
            with open(event.src_path,'r',errors='ignore') as f: lines=f.readlines()[-20:]
            for line in lines:
                if 'ERROR' in line.upper() or 'WARNING' in line.upper():
                    h=hashlib.md5(line.encode()).hexdigest()
                    if h not in seen:
                        seen[h]=1; self.cb(event.src_path,line)
        except Exception: pass
def watch(path,cb):
    o=Observer(); o.schedule(LogHandler(cb),path=path,recursive=True); o.start()
    while True: time.sleep(5)
