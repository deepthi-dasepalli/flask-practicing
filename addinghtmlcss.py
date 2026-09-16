from flask import *
app=Flask(__name__)
@app.route('/')
def  deepthi():
    return render_template('html_2exmp.html')
if __name__=='__main__':
    app.run(debug=True)