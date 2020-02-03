from flask import Flask, render_template, request
from proc_file import read_file, write_file

app = Flask(__name__)

@app.route('/')
def index():
  return '<a href = "/home">Sveika pasaule!</a>'


@app.route('/about')
def about():
  return render_template('about.html', active_page = '/about')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = '169420lol542' )

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/params')
def params():
  return render_template('params.html', args = request.args.to_dict())

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

@app.route('/read_from_file')
def readFromFile():
  content = read_file()
  return content

@app.route('/write_from_file', methods = ['POST'])
def writeFromFile():
  request_type = request.content_type
  print(request_type)
  if (request_type == 'application/json'):
    contentJSON = request.get_json()
    print(contentJSON)
    print(contentJSON['data'])
    write_file(contentJSON['data'])
    return contentJSON
  else:
    return 'Request type not supported'

@app.route('/file', methods = ['POST', 'GET'])
def file():
  if request.method == 'GET':
    return readFromFile()
  elif request.method == 'POST':
    return writeFromFile()

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)