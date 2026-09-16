from flask import *
app=Flask(__name__)
@app.route('/')
def deepthi():
    return 'learning flask'


if __name__=='__main__':
    app.run(debug=True)
