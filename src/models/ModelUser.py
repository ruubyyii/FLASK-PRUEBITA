from .entities.User import User

class ModelUser():

    @classmethod
    def login(cls, db, email):

        try:
            cur = db.connection.cursor()
            cur.execute('SELECT * FROM user WHERE email = %s', (email,))
            datos = cur.fetchone()

            if datos:

                id = datos[0]
                username  = datos[1]
                email = datos[2]
                password = datos[3]

                user = User(id, username, email, password)

                return user
            else:

                return None
        
        except Exception as e:

            raise Exception(e)


    @classmethod
    def register(cls, db, user):

        try:
            hashed_password = User.generate_hash(user.password)
            cur = db.connection.cursor()
            cur.execute('INSERT INTO users VALUES (NULL, %s, %s, %s)', (user.username, user.email, hashed_password))
            db.connection.commit()

        except Exception as e:

            raise Exception(e)


    @classmethod
    def get_by_id(cls, db, id):

        try:
            cur = db.connection.cursor()
            cur.execute('SELECT id, username, email FROM user WHERE id = %s', (id))
            datos = cursor.fetchone()

            if datos:

                id = datos[0]
                username = datos[1]
                email = datos[2]

                logged_user = User(id, username, email, None)

                return logged_user

            else:
                return None

        except Exception as e:

            raise Exception(e)