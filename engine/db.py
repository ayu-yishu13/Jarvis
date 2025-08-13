import sqlite3

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

#query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'edge', 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'code', 'https://leetcode.com/')"
#cursor.execute(query)
#con.commit()

#delete_query = "DELETE FROM web_command WHERE id = ?"
#cursor.execute(delete_query, (7,))  # 1 is the id you want to delete
#con.commit()

# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')