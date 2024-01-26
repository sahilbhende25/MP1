import socket
import subprocess

from flask import Flask, request
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      command = ['python','temp_stress.py']
      subprocess.Popen(command)
      return "Complete"
   else:
      return socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)