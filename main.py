from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return '<a href = "/home">Sveika pasaule!</a>'


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = '169momgaylol542' )

@app.route('/home')
def home():
  return render_template('home.html')

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)

