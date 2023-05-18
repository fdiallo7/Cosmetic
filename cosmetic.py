from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    return render_template('home.html')

# Define the booking page route
@app.route('/booking')
def booking():
    return render_template('booking.html')

# Define the information page route
@app.route('/information')
def information():
    # Establish a connection to the MySQL database
    with mysql.connector.connect(
        host="localhost",
        user="flask",
        password="ubuntu",
        database="flask_db"
    ) as con:
        # Create a cursor object to execute SQL queries
        cur = con.cursor()

        # Create a table if it doesn't exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS services (
                id INT PRIMARY KEY,
                service_name VARCHAR(255),
                price DECIMAL(10, 2)
            )
        """)

        # Query the database to get all services
        cur.execute("SELECT * FROM services")
        services = cur.fetchall()

    return render_template('information.html', services=services)

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
