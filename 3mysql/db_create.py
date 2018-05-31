from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import scoped_session, sessionmaker


print('Creating database tables for to do app...')
mysql_db_url="mysql://maxlai:pycontw2018@127.0.0.1/demodb"
engine = create_engine(mysql_db_url, echo=True, pool_recycle=3600)
connection = engine.connect()
trans = connection.begin()
try:
    connection.execute("DROP TABLE IF EXISTS todo_tasks;")
    print ("Finished dropping table (if existed)")
    # Create table
    connection.execute("CREATE TABLE todo_tasks (id INT PRIMARY KEY, title VARCHAR(50), description VARCHAR(200), done TINYINT);")
    print ("Finished creating table")
    # Insert some data into table
    connection.execute("INSERT INTO todo_tasks (id, title, description, done) VALUES (%s, %s, %s, %s);", (1,'Buy groceries', 'Milk, Cheese, Pizza, Fruit, Tylenol',0))
    connection.execute("INSERT INTO todo_tasks (id, title, description, done) VALUES (%s, %s, %s, %s);", (2,'Learn Python', 'Need to find a good Python tutorial on the web',0))
    print ("Finished inserting data")
    trans.commit()
    print('...done!')

except:
    trans.rollback()
    raise
