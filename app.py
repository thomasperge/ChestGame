from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
import mainRegister as register

app = Flask(__name__)



# ===== Page d'acceuil =====
@app.route("/", methods=['GET', 'POST'])
@app.route("/index.html", methods=['GET', 'POST'])
def main():
    return render_template('index.html')


# ===== Login Page =====
@app.route("/login.html", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print('Username : ', username, ', Password : ' ,password)

        if username == '' or password == '':
            return render_template('error.html', var='No data...')

        # == Appel de la Class ==
        login = register.Register(username, password)

        # == Si la fonction renvoie True ==
        if login.registerUser() == True:
            print('Login dans la database')
            login.returnUser()
            return render_template('index.html')

        else:
            return render_template('error.html', var='No User has this nickname, or the password is wrong ...')
    else:
        return render_template('login.html')



# ===== Sign-Up Page =====
@app.route("/signup.html", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print('Username : ', username, ', Password : ' ,password)

        # == Enregistrement de l'Utilisateur ==
        login = register.Register(username, password)

        if login.recording() == True:
            login.send()
            return render_template('index.html')

        elif login.recording() == 'Pseudoshort':
            return render_template('error.html', var='Username too short !')

        elif login.recording() == 'PasswordShort':
            return render_template('error.html', var='Password too short !')

        else:
            return render_template('error.html', var='User already taken !')
    else:
        return render_template('signup.html')



# === Error - Login ===
@app.route("/error.html", methods=['GET', 'POST'])
def error():
    return render_template('error.html', var='')



# === Earn ===
@app.route("/earn.html", methods=['GET', 'POST'])
def earn():
    return render_template('earn.html')



# === Index2 ===
@app.route("/index2.html", methods=['GET', 'POST'])
def index2():
    return render_template('index2.html')



if __name__ == '__main__':
    app.run(debug=True)