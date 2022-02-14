import csv
import psycopg2
import os 



def write_coffee(filename):
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
    cur = conn.cursor()
    with open(filename + '.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            for index, col in enumerate(row[1:]): 
                print(col)
                index+=1
                col = col.replace(",", "")
                row[index] = int(col)
            print(row)
            cur.execute(
            "INSERT INTO coffee_" + filename + 
            " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, \
                                                        %s, %s, %s, %s)",
            row
        )
    conn.commit()
    
def main(): 
    #write_coffee('consumption') 
    write_coffee('production')
    
if __name__ == "__main__": 
    os.chdir("/Users/suezhanna/Johnathan/Projects/Coffee")
    main()