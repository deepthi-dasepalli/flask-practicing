from flask import Flask
app=Flask(__name__)

@app.route('/hello/<name>')
def deepthi(name):

    return 'learning flask ' +name

if __name__=='__main__'  :
  
  app.run(debug=True)