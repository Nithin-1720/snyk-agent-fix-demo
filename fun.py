import subprocess
from flask import request

def ping():
    host = request.args.get("host")
    subprocess.call("ping " + host, shell=True)
