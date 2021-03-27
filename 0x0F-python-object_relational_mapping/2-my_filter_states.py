#!/usr/bin/python3
"""Script that  takes in an argument and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Hago la conexión a la BD, obtengo un objeto db"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """Obtengo un cursor para ejecutar las consultas"""
    cur = db.cursor()
    """Ejecuto consulta utilizando el cursor"""
    cur.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY id"
                .format(argv[4]))
    rows = cur.fetchall()
    for i in rows:
        if i[1] == argv[4]:
            print(i)
    cur.close()
    db.close()
