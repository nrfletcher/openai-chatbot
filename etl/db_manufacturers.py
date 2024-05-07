import csv
import sqlite3

conn = sqlite3.connect('automotives.db')
cursor = conn.cursor()

# Create the 'manufacturers' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS manufacturers (
        make_id INTEGER PRIMARY KEY,
        make TEXT,
        country TEXT,
        year INTEGER
    )
""")

# Open the CSV file and insert the data into the 'manufacturers' table
with open('sources/manufacturers.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        make, country, year = row

        # This ensures that our country table foreign key matches easily
        if country == 'USA':
            country = 'United States'
        if country == 'UK':
            country = 'United Kingdom'

        cursor.execute("INSERT INTO manufacturers (make, country, year) VALUES (?, ?, ?)", 
                       (make, country, year))
        
# Add our foreign key association to country via country_id
cursor.execute("""
    ALTER TABLE manufacturers
    ADD COLUMN country_id INTEGER REFERENCES country(country_id)
""")

# Set the id to match whatever id country has associated with country of manufacturer
cursor.execute("""
    UPDATE manufacturers
    SET country_id = (
        SELECT country.country_id
        FROM country
        WHERE country.name = manufacturers.country
    )
""")

conn.commit()
conn.close()