#by using add_url_rule 
from flask import Flask
app=Flask(__name__)

def deepthi():
    return 'learning flask'
app.add_url_rule('/deepthi','deepthi',deepthi)

if __name__=='__main__':
    app.run(debug=True)