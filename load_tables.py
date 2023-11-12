import psycopg2
# Connection parameters
param_dic = {
    "host"      : "localhost",
    "database"  : "postgres",
    "user"      : "postgres",
    "password"  : "admin"
}

def connect(params_dic):
    conn=None
    conn=psycopg2.connect(**params_dic)
    return conn

def copy_from_file(conn,schema,table):
    filename=f"./data/{table}.csv"
    tablename=f"{schema}.{table}"
    truncate_table_query=f"TRUNCATE TABLE {tablename} CASCADE"
    f=open(filename,'r')
    copy_sql = f"COPY {tablename} FROM stdin DELIMITER \',\' CSV header;"
    cursor=conn.cursor()
    cursor.execute(truncate_table_query)
    cursor.copy_expert(copy_sql,f)
    conn.commit()
    cursor.close()

conn = connect(param_dic)
copy_from_file(conn, 'employees_schema', 'titles')
copy_from_file(conn, 'employees_schema', 'employees')
copy_from_file(conn, 'employees_schema', 'departments')
copy_from_file(conn, 'employees_schema', 'dept_manager')
copy_from_file(conn, 'employees_schema', 'dept_emp')
copy_from_file(conn, 'employees_schema', 'salaries')
conn.close() # close the connection