# username = charlie
# password = charlie
# db_name = mydb

import psycopg2

try :
    conn = psycopg2.connect(
        dbname = "mydb" ,
        user = "charlie" , 
        password = "charlie" ,
        host = "localhost" ,
        port = "5432" ,
    )
    print('Connection Successful ..!')
except :
    print('Connection Failed ..!')

conn.close()