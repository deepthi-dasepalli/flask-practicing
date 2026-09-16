# flask using templates
from flask import *
app=Flask(__name__)
@app.route('/')
def deepthi():
    return render_template('flask_html.html')


if __name__=='__main__':
    app.run(debug=True)
