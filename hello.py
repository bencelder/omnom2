from flask import Flask, url_for, render_template, session, redirect, escape, request
app = Flask(__name__)


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return "You are not logged in"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="POST">
            <p><input type=text name=username value="Enter username">
            <p><input type=submit value=Login>
        </form>
        '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


app.secret_key = '%R\x17\x8e\xcblG\xbb(9\xf9\xe6\x87\xbc\xb5\x8b\xca\xa8mK\xb3\xcf\xffV'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return "User %s" % username

@app.route('/projects/')
def projects():
    return "The project page"

@app.route('/about')
def about():
    return "The about page"
