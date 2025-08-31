import psycopg2, requests, json, os, random

# DailyChallenge: Web API to DB

dir_path = os.path.dirname(os.path.realpath(__file__))

connection = psycopg2.connect(
    database = 'countries',
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = '5432'
)
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS countries')
cursor.execute('''CREATE TABLE countries(
               country_id SERIAL PRIMARY KEY,
               country_name VARCHAR (200) NOT NULL,
               capital VARCHAR (200),
               flag_png VARCHAR(200),
               region VARCHAR (200),
               population INTEGER NOT NULL)''')

connection.commit()
print('Connection Successful. Table Created.')

api_url = 'https://restcountries.com/v3.1/all?fields=name,capital,flags,subregion,population'
response = requests.get(api_url)

# LOAD DATA INTO JSON FILE
if response.status_code == 200:
    data = response.json()

    with open(f'{dir_path}/contries.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print("Data Successfully Loaded into JSON file")

else:
    print(f'{response.status_code}')
    print("Failed to fetch data from API.")


# LOAD 10 random countries 
selected_countries = random.sample(data, 10)

for country in selected_countries:
    country_name = country['name']['common']
    capital = country['capital'][0]
    flag_png = country['flags']['png']
    region = country['subregion']
    population = country['population']
    
    query = "INSERT INTO countries(country_name, capital, flag_png, region, population) VALUES (%s, %s, %s, %s, %s)"

    cursor.execute(query, (country_name, capital, flag_png, region, population))

    connection.commit()

print("Table Successfully Populated.")

cursor.close()
connection.close()