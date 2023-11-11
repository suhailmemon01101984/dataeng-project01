import psycopg2
connection = psycopg2.connect(user='postgres', password='admin', host='localhost', database='postgres')
curs = connection.cursor()
schema='employees_schema'
create_schema_query=f"CREATE SCHEMA IF NOT EXISTS {schema};"
curs.execute(create_schema_query)
connection.commit()
curs.close()
connection.close()