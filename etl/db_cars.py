import csv
import sqlite3

conn = sqlite3.connect('automotives.db')
cursor = conn.cursor()

# Create the 'cars' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cars (
        car_id INTEGER,
        make TEXT,
        model TEXT,
        year INTEGER,
        color TEXT,
        mileage INTEGER,
        price INTEGER,
        location TEXT
    )
""")

# Open the CSV file and insert the data into the 'manufacturers' table
with open('sources/cars.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)
    for row in csv_reader:
        car_id, make, model, year, color, mileage, price, location = row
        cursor.execute("INSERT INTO cars (car_id, make, model, year, color, mileage, price, location) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (car_id, make, model, year, color, mileage, price, location))

# Add our foreign key association to manufacturer via make_id
cursor.execute("""
    ALTER TABLE cars
    ADD COLUMN make_id INTEGER REFERENCES manufacturers(make_id)
""")

# Set make_id of car to match id associated with manufacturer
cursor.execute("""
    UPDATE cars
    SET make_id = (
        SELECT manufacturers.make_id
        FROM manufacturers
        WHERE manufacturers.make = cars.make
    )
""")

conn.commit()
conn.close()