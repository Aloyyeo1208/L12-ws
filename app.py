from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)

# Simple in-memory user store for demonstration
users = {"user": "pass123"}

@app.route('/')
def home():
    return render_template_string(open('login.html').read())

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('transfer'))
    else:
        return "Invalid credentials, please try again."

@app.route('/transfer')
def transfer():
    return render_template_string(open('transfer.html').read())

if __name__ == '__main__':
    app.run(debug=True)