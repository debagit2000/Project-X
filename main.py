import yaml,socket
from monitor.watcher import watch
from ai.analyzer import analyze
from notifications.email_sender import send_email
with open("config.yaml") as f: config=yaml.safe_load(f)
server=socket.gethostname()
def process(logfile,error):
    report=analyze(error)
    send_email(f"[ALERT] {server}",report,config['email'])
    print(report)
for p in config['log_paths']: watch(p,process)
