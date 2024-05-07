import csv
import sqlite3

conn = sqlite3.connect('automotives.db')
cursor = conn.cursor()

# Create the 'manufacturers' table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS country_stat (
        country_stat_id INTEGER PRIMARY KEY,
        rank INTEGER,
        country TEXT,
        happiness REAL,
        gdp REAL,
        social REAL,
        life_expectancy REAL,
        freedom REAL,
        generosity REAL,
        perception REAL
    )
""")

# Open the CSV file and insert the data into the 'manufacturers' table
with open('sources/worldhappiness.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        rank, country, happiness, gdp, social, life_expectancy, freedom, generosity, perception = row
        cursor.execute("INSERT INTO country_stat (rank, country, happiness, gdp, social, life_expectancy, freedom, generosity, perception) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (rank, country, happiness, gdp, social, life_expectancy, freedom, generosity, perception))

cursor.execute("""
    ALTER TABLE country_stat
    ADD COLUMN country_id INTEGER REFERENCES country(country_id)
""")

cursor.execute("""
    UPDATE country_stat
    SET country_id = (
        SELECT country.country_id
        FROM country
        WHERE country.name = country_stat.country
    )
""")

conn.commit()
conn.close()