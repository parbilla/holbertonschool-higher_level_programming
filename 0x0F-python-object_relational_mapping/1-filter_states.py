#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Hago la conexión a la BD, obtengo un objeto db"""
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    """Obtengo un cursor para ejecutar las consultas"""
    cur = db.cursor()
    """Ejecuto consulta utilizando el cursor"""
    cur.execute("SELECT * FROM states ORDER BY id WHERE name LIKE 'N%'")
    for i in cur:
        print(cur.fetchone())
    cur.close()
    db.close()
