import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="pygame_db",
    user="pp2",
    password="test123",
    port="5432",
)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS snake_scores (
    id SERIAL PRIMARY KEY,
    player_name VARCHAR(50),
    score INT,
    level INT,
    foods_eaten INT,
    played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def get_cur():
    cur = conn.cursor()
    return cur 

def update_score(values):
    insert_q = "INSERT INTO snake_scores (player_name, score, level, foods_eaten) VALUES (%s, %s, %s, %s)"
    insert_v = values
    cur = get_cur()
    cur.execute(insert_q, insert_v)
    conn.commit()

