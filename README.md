# Discord Chatbot
## AutoBot is a Discord bot that utilizes and internal car database!

### This project is a Discord chat bot which combines the ability to use a GPT-based response format and also utilizes additional information from internal sources persisted into a SQLite3 database.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/iovmhhzY2PA/0.jpg)](https://youtu.be/iovmhhzY2PA)

## Sections
This project consists of two sections:
1. The Discord bot instructions located in the root of this repo.
2. The ETL instructions located inside of the 'etl' folder.

<br>
In order to build and run this project, you must complete the steps in both the instructions below as well as the steps regarding SQLite3 installation which can be found in the ETL section of the writeup.
<br>
<br>
If SQLite3 is successfully installed globally, you can build this project by following the instructions below.

## Instructions
To run this project do the following:
1. Ensure that all Python libraries in 'requirements.txt' are installed.
```python
pip install -r requirements.txt
```
2. Create a '.env' file in the root directory and add your tokens for "DISCORD_TOKEN" and "GPT_TOKEN"
```bash
touch .env
```
3. Run the build command to create the database necessary for using the '!cars' and '!manufacturers' commands.
```python
python build.py
```
4. Start the Discord bot 
```python
python main.py
```
5. At this point, the bot should now be active and running in the Discord server. Here are all the valid commands to try.
```bash
!help 
# Responds with help message
!hello 
# Basic hello command
!funfact 
# Gives a fun car fact
!cars {your question} 
# Ask a question about the automotives.db cars table
!manufacturers {your question} 
# Ask a question about the automotives.db manufacturers table
```

### Bot Specifications
1. Utilizes the automotives.db SQLite3 database
2. Recognizes '!help' command; reply with instructions
3. Provides 3 unique commands; '!cars' and '!manufacturers' which interact with the database, and '!funfact' which does not.
4. The external datasource is the automotives.db from the ETL project.

# Extract, Transfer, Load (ETL folder)
- Focus: Automotive Industry

## Instructions
- This project utilizes SQLite by downloading the bundle distribution and directly accessing it via the executables provided.
- This executable can be found at https://www.sqlite.org/download.html, this project was built using Precompiled Binaries for Windows.
- The .gitignore specifies these executables, and while SQLite3 can be added to PATH, it should be noted that this project was built with all files in .gitignore present at the root of the project.
- If using SQLite3.exe directly in root of project, follow instructions exactly. If using sqlite3 via a global install with PATH, use 'sqlite3' instead of './sqlite3.exe'.
### Database Init
- To build the database, simply run the setup script in the root directory.
```bash
python build.py
```
- If successful, there should now be an 'automotives.db' file in the root directory. Now, we can interact using SQLite3.exe or sqlite3 if on PATH.
```sql
./sqlite3.exe automotives.db # Selects database
```
- Once in the shell:
```sql
.databases; # Should show 'automotives' and automotives.db should be present
.tables; # Should show 'cars', 'manufacturers', 'chiptuners', 'country_ids', and 'country_stats'
select * from cars; # Should show all fields in cars
pragma table_info(cars); # Should show cars table schema
```
- We can use the interactive shell to build tables, but Python scripts are used for everything in this project. Only use sqlite3.exe directly for viewing purposes.
### SQL Queries
- Here are some SQL queries we can now do on our database with relational connections.
```sql
# Shows us all car models with a non-modified HP greater than 300
select model from chiptuners where "bhp standard" > 300;

# Shows us countries with a GDP per capita over 1
select country, gdp from country_stat where gdp > 1;

# Shows us how many of each car make exist in cars table
select count(make), make from cars group by make;

# Get all car manufacturers which are based in countries ranked top 10 for overall happiness 
select m.make, m.country from manufacturers m join country c on m.country_id = c.country_id join country_stat cs on c.country_id = cs.country_id where cs.rank <= 10 group by m.make;

# See how many major car manufacturers each country has (ascending order)
select count(country), country from manufacturers group by country order by count(country);

# Shows us statistics for all countries with a major car manufacturer
select * from country_stat where country_id > 0;
```

## Database Schema & Creation
- With SQLite3, database creation is simple - using the connect function will either connect to an existing database, or if that database does not exist, simply creates it instead and continues on.
### Tables
- Manufacturers (Car manufacturers) (foreign key association to country via country_id, foreign key associations to chiptuners and cars via make_id)
- Chiptuners (Instances of car modification specifications) (foreign key association with manufacturers via make_id)
- Cars (Specific trims and years of car models) (foreign key association with manufacturers via make_id)
- Country (Country name, abbreviation, etc.) (foreign key connections to manufacturers and country_stat via country_id)
- Country Statistic (global rankings and individual measurements such as GDP) (foreign key connection to country via country_id)

## Data Sources
- Free Tuning SQL Sample Database 
https://www.teoalida.com/cardatabase/tuning/
- Manufacturers Gist 
https://gist.github.com/OdeToCode/582e9c044eee5882d54a6e5997c0be52#file-manufacturers-csv
- Countries API 
https://restcountries.com/#rest-countries
- Car Data CSV (only used first 500 for size consideration) 
https://www.kaggle.com/datasets/arnavsmayan/vehicle-manufacturing-dataset
- World Happiness Report CSV 
https://www.kaggle.com/datasets/unsdsn/world-happiness
