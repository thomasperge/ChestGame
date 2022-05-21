# Module Imports
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='azerty',
    database="chestgame"
)

cursor = db.cursor()

# ============ Class Register ============
class Register():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    


    def registerUser(self):
        """ Permet de voir si le pseudo envoyer en __init__ est dans la DB ou non, si pseudo est dans la DB: renvoye False, si
        pseudo disponible (pas dans la DB): renvoye True, ou renvoye False si: mauvais mdp
        """
        username = self.username
        # == Query ==
        sql = ("""SELECT * FROM chestgame.registeruser WHERE userPseudo = %s""")
        info = (username, )
        cursor.execute(sql, info)

        # == Boucle: permet de voir si il y un pseudo ==
        for x in cursor:
            # == Get Hash Password ==
            passwordHash = x[2]
            passwordInput = self.password
            # == Verifie si le Hash est correcte aux mdp entrée ==
            if check_password_hash(passwordHash, passwordInput):
                # Connect
                return True
            else:
                # Mauvais mdp
                return False
        else:
            # == Pseudo disponible ==
            return False



    def recording(self):
        """Creation du compte si l'utilisateur n'en a pas, on regarde si l'entrée du nouveaux username existe ou pas
        dans la DB
        """
        # == Appel fonction registerUser, si True c'est que il y a déjà un pseudo prit ==
        if self.registerUser():
            return False
        else:
            username = self.username
            passwordInput = self.password

            if username == '' or passwordInput == '':
                return False
            elif len(username) <= 4:
                return 'Pseudoshort'
            elif len(passwordInput) <= 7:
                return 'PasswordShort'

            passwordHash = generate_password_hash(passwordInput)

            sql = ("""SELECT * FROM chestgame.registeruser WHERE userPseudo = %s""")
            info = (username,)
            cursor.execute(sql, info)

            # == On fait une boucle, pour savoir si le pseudo est deja prit ==
            for x in cursor:
                # == Pseudo déjà pris ==
                return False
            else:
                # == creation pseudo dans la DB ==
                sql = ("""INSERT INTO registeruser (userPseudo, passwordUser)
                        VALUES (%s, %s)""")
                info = (username, passwordHash,)
                cursor.execute(sql, info)
                print('Account crée !')
                return True
     


    def returnUser(self):
        if self.registerUser() == True:
            print('ReturnUser = tout est oké pour: ', self.username, self.password)

# ============ End Class Register ============



    def send(self):
        db.commit()


if __name__ == '__main__':
    r = Register('thomas2', 'thomaspassword1')
    r.recording()
    # db.commit()
