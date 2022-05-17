from distutils.log import debug
from pickle import TRUE
from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return render_templates('index.html',name=name) 
    app.send_ststic_
    index.html
    return "<h1>Hello World</h1>"

if __name__=='__main__':
    app.run(port=5050,debug=TRUE)
