#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, safe from MySQL
injections"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Hago la conexión a la BD, obtengo un objeto db"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """Obtengo un cursor para ejecutar las consultas"""
    cur = db.cursor()
    """Ejecuto consulta utilizando el cursor"""
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id",
                (argv[4],))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
