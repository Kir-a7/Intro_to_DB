import mysql.connector



def create_database():
    try:    
        db = mysql.connector.connect(

            host ='localhost'
            user = 'root'
            password ='root'
        )
        if db.is_connected():
            mycursor = db.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    
    finally:

        if db.is_connected():
            mycursor.close()
            db.close()
            print("MySQL connection is closed.")

    if __name__ == "__main__":
        create_database