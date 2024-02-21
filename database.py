import psycopg

conn = psycopg.connect(
    dbname="soy_beans",
    user="vaecherdt"
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        file_name TEXT NOT NULL,
        timestamp TEXT,
        exif TEXT,
        defect TEXT,
        notes TEXT
    );
""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS grains (
        id SERIAL PRIMARY KEY,
        image_id INTEGER REFERENCES images(id),
        region TEXT,
        cooperative TEXT,
        harvest_information TEXT,
        timestamp TIMESTAMP
    );
""")
conn.commit()

cur.execute("""
    CREATE TABLE IF NOT EXISTS climate (
        id SERIAL PRIMARY KEY,
        grains_id INTEGER REFERENCES grains(id),
        temperature FLOAT,
        humidity FLOAT,
        weather_conditions TEXT,
        timestamp TIMESTAMP
    );
""")
conn.commit()


def save_image_data(image_data):
    for data in image_data:
        cur.execute("""
            INSERT INTO images (file_name, timestamp, exif, defect)
            VALUES (%s, %s, %s, %s)
        """, (data["file_name"], data["defect"], data["timestamp"], data["exif"]))
    conn.commit()
