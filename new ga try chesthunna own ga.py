from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return 'hello student'

@app.route('/vahi')
def vahi():
     return "hello vahi"

@app.route('/deepu')
def deepu():
     return "hello deepu"
def user(name):
     if name=="vahi":
          return redirect (url_for('vahi'))
     
     if name=="deepu":
          return redirect (url_for('deepu'))
if __name__== '__main__':
     app.run(debug=True)