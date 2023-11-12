import psycopg2
connection = psycopg2.connect(user='postgres', password='admin', host='localhost', database='postgres')
curs = connection.cursor()
schema='employees_schema'
create_schema_query=f"CREATE SCHEMA IF NOT EXISTS {schema};"
create_titles_query=f"DROP TABLE IF EXISTS {schema}.titles CASCADE; CREATE TABLE IF NOT EXISTS {schema}.titles(title_id varchar(256) CONSTRAINT pk_titles PRIMARY KEY, title varchar(256));"
create_employee_query=f"DROP TABLE IF EXISTS {schema}.employees CASCADE; CREATE TABLE IF NOT EXISTS {schema}.employees(emp_no integer CONSTRAINT pk_employees PRIMARY KEY, emp_title_id varchar(256), birth_date date, first_name varchar(256), last_name varchar(256), sex char(1), hire_date date, CONSTRAINT fk_employees_titles FOREIGN KEY(emp_title_id) references {schema}.titles(title_id));"
create_departments_query=f"DROP TABLE IF EXISTS {schema}.departments CASCADE; CREATE TABLE IF NOT EXISTS {schema}.departments(dept_no varchar(256) CONSTRAINT pk_departments PRIMARY KEY, dept_name varchar(256));"
create_salaries_query=f"DROP TABLE IF EXISTS {schema}.salaries; CREATE TABLE IF NOT EXISTS {schema}.salaries(emp_no integer CONSTRAINT pk_salaries PRIMARY KEY, salary integer, CONSTRAINT fk_salaries_employees FOREIGN KEY(emp_no) references {schema}.employees(emp_no));"
create_dept_emp_query=f"DROP TABLE IF EXISTS {schema}.dept_emp; CREATE TABLE IF NOT EXISTS {schema}.dept_emp(emp_no integer, dept_no varchar(256), PRIMARY KEY(emp_no,dept_no), CONSTRAINT fk_dept_emp_employees FOREIGN KEY(emp_no) references {schema}.employees(emp_no), CONSTRAINT fk_dept_departments FOREIGN KEY(dept_no) references {schema}.departments(dept_no));"
create_dept_manager_query=f"DROP TABLE IF EXISTS {schema}.dept_manager; CREATE TABLE IF NOT EXISTS {schema}.dept_manager(dept_no varchar(256), emp_no integer, PRIMARY KEY(dept_no,emp_no), CONSTRAINT fk_dept_manager_employees FOREIGN KEY(emp_no) references {schema}.employees(emp_no), CONSTRAINT fk_dept_manager_departments FOREIGN KEY(dept_no) references {schema}.departments(dept_no));"

curs.execute(create_schema_query)
curs.execute(create_titles_query)
curs.execute(create_employee_query)
curs.execute(create_departments_query)
curs.execute(create_salaries_query)
curs.execute(create_dept_emp_query)
curs.execute(create_dept_manager_query)
connection.commit()
curs.close()
connection.close()

