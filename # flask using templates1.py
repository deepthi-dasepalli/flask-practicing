# flask using templates
from flask import *
app=Flask(__name__)
@app.route('/user/<name>')
def deepthi(name):
    return render_template('using_delimeters.html',name=name)


if __name__=='__main__':
    app.run(debug=True)