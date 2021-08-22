from app import mysql
from models.user import User
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash

class User_repository():
    def __init__(self):
        self.mysql = mysql
        self.user = User

    @staticmethod
    def get_all(self):
        conn = self.mysql.connect()
        users = []
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            rv = cursor.fetchall()
            for i in range(len(rv)):
                user = self.user(rv[i])
                users.append(user)
            return "OK",users,200
        except MySQL.Error as e:
            return e,None,500
        except TypeError as e:
            return e,None,400
        except Exception as e:
            return e,None,400
        finally:
            conn.close()
            cursor.close()
    
    @staticmethod
    def get_by_id(self, id):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        user = None
        try:
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            rv = cursor.fetchone()
            user = self.user(rv[0])
            return "OK",user,200
        except MySQL.Error as e:
            return e,None,500
        except TypeError as e:
            return e,None,400
        except Exception as e:
            return e,None,400
        finally:
            conn.close()
            cursor.close()

    @staticmethod
    def create(self,user):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO users (id, username, password,jwt_token, last_login, name_id, password_hash, team, api_token, project, username_is_assigned, authentication_mechanism) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user.id, user.username, user.password, user.jwt_token, user.last_login, user.name_id, user.password_hash, user.team, user.api_token, user.project, user.username_is_assigned, user.authentication_mechanism))
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            rv = cursor.fetchone()
            user = self.user(rv[0])
            conn.commit()
            return "Created",user,201
        except MySQL.Error as e:
            return e,None,500
        except TypeError as e:
            return e,None,400
        except Exception as e:
            return e,None,400
        finally:
            conn.close()
            cursor.close()

    @staticmethod
    def update(self,id,username, password):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        user = None
        try:
            cursor.execute('''UPDATE users SET name = %s, password = %s WHERE id = %s''', (username, generate_password_hash(password), id))
            cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
            rv = cursor.fetchone()
            user = User(rv[0])
            conn.commit()
            return "Updated",user,201
        except MySQL.Error as e:
            return e,None,500
        except TypeError as e:
            return e,None,400
        except Exception as e:
            return e,None,400
        finally:
            conn.close()
            cursor.close()
        
    
    @staticmethod
    def delete(self,id):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id = %s", (id,))
            conn.commit()
            return "SUCCESS",True,200
        except MySQL.Error as e:
            return e,None,500
        except TypeError as e:
            return e,None,400
        except Exception as e:
            return e,None,400
        finally:
            conn.close()
            cursor.close()
    
    @staticmethod
    def get_all_ids(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        ids = []
        cursor.execute("SELECT id FROM users")
        rv = cursor.fetchall()
        for i in range(len(rv)):
            ids.append(rv[i][0])
        conn.close()
        cursor.close()
        return ids