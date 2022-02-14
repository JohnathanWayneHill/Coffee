import csv
import psycopg2
import os 

os.chdir("/Users/suezhanna/Johnathan/Projects/Coffee")
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
cur = conn.cursor()
with open('consumption.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) # Skip the header row.
    for row in reader:
        for index, col in enumerate(row[1:]): 
            print(col)
            index+=1
            col = col.replace(",", "")
            row[index] = int(col)
        print(row)
        cur.execute(
        "INSERT INTO coffee_consumption VALUES (%s, %s, %s, %s, %s, %s, %s, %s, \
                                                    %s, %s, %s, %s)",
        row
    )
conn.commit()