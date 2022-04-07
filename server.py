from typing import Counter
from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'Rand0m$!'

@app.route('/') 
def index():
    if 'count' in session:
        session ['count'] += 1
    else:
        session ['count'] = 0
    return render_template('index.html')

@app.route('/count2')
def count2():
    if 'count' in session:
        session ['count'] += 1
    else:
        session ['count'] += 0
    return redirect ('/')

@app.route('/destroy_session')
def destroySession():
    session.clear()
    return redirect('/')
    
# @app.route('/users', methods=['POST'])
# def create_user():
#     print(request.form)
#     session ['username'] = request.form['name']
#     session ['useremail'] = request.form['email']
#     return redirect("/show")	

if __name__=="__main__":
    app.run(debug=True, port=5001) 
