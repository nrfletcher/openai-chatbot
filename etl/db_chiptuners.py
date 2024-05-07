import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('automotives.db')
cursor = conn.cursor()

# Execute the SQL script
with open('sources/chiptuning.sql', 'r') as f:
    cursor.executescript(f.read())

# Add our foreign key association to manufacturer via make_id
cursor.execute("""
    ALTER TABLE chiptuners
    ADD COLUMN make_id INTEGER REFERENCES manufacturers(make_id)
""")

# Set the id to match the make of the car in chiptuner specification
cursor.execute("""
    UPDATE chiptuners
    SET make_id = (
        SELECT manufacturers.make_id
        FROM manufacturers
        WHERE manufacturers.make = chiptuners.Make
    )
""")

# Commit the changes and close the connection
conn.close()