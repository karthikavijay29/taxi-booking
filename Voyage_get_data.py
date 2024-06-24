from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vi@29112004",
    database="moon"
)

@app.route('/book', methods=['GET', 'POST'])
def book_cab():
    if request.method == 'POST':
        name = request.form('name')
        phone = request.form('phone')
        date = request.form('date')
        when = request.form('when')
        pickup_location = request.form('pickup_location')
        drop_location = request.form('drop_location')
        
        cursor = mydb.cursor()
        sql = "INSERT INTO voyage (name, phone, date, when, pickup_location, drop_location) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (name, phone, date, when, pickup_location, drop_location)
        cursor.execute(sql, val)
        mydb.commit()
        
        return "Cab booked successfully!"

    return render_template('Voyage.html')

if __name__ == '__main__':
    app.run(debug=True)
