from flask import Flask, request
app = Flask(__name__)

num = 0

@app.route('/',methods = ['POST', 'GET'])
def login():
   global num
   if request.method == 'POST':
      inputData = request.json
      num = inputData.get('num')
      return str(num)
   else:
      return str(num)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)