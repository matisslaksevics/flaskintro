from flask import Flask, render_template, request

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

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)