import sqlite3

dbname = 'lab5.sqlite'

def create_table():
  try:
    sql = 'CREATE TABLE IF NOT EXISTS records (name text UNIQUE, country text, catches int)'
    with sqlite3.connect(dbname) as con:
      con.execute(sql)
    con.close()
  except Exception as e:
    print('error creating database', e)



def create(name, country, catches):
  try:
    sql = 'INSERT INTO records values (?, ?, ?)'
    with sqlite3.connect(dbname) as con:
      result = con.execute(sql, (name, country, catches))
    con.close()
    return result.rowcount
  except Exception as e:
    print('error creating record', e)


def read_all():
  with sqlite3.connect(dbname) as con:
    results = con.execute('SELECT * from records')
    rows = results.fetchall()
  con.close()
  return rows


def read_by_name(name):
  sql = 'SELECT * from records WHERE name = ?'
  with sqlite3.connect(dbname) as con:
    results = con.execute(sql, (name,))
    row = results.fetchone()
  con.close()
  return row


def update_catches(name, catches):
  sql = 'UPDATE records SET catches = ? WHERE name = ?'
  with sqlite3.connect(dbname) as con:
    updated = con.execute(sql, (catches, name))
    rows = updated.rowcount
  con.close()
  return rows


def delete(name):
  sql = 'DELETE from records WHERE name = ?'
  with sqlite3.connect(dbname) as con:
    con.execute(sql, (name,))
  con.close()

def print_all():
  rows = read_all()
  if (len(rows) == 0):
    print('no records :(')
  else:
    for row in rows:
      name, country, catches = row
      print(name, country, catches)

def main():
  create_table()

  
if __name__ == "__main__":
  main()
