from flask import Flask, render_template

#------------------------------------1. init app ---------------------
app = Flask(__name__)


#------------------------------------2. Routers ------------------------
@app.route('/')
def index():
    return render_template('index.html')



@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/Home')
def Home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('full_website.html')


#-----------------------------------------3.start server ---------------------------------
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
