from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'Rand0m$!'

@app.route('/', methods=['GET', 'POST']) 
def index():
    if request.form['increment'] == '':
        if 'count' in session:
            session ['count'] += 1
        else:
            session ['count'] = 0
        return render_template('index.html')
    else:
        if 'increment' in session:
            session ['increment'] += request.form['increment']
        else: 
            session ['increment'] = 1
        return render_template ('index.html')
    

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

if __name__=="__main__":
    app.run(debug=True, port=5001) 
