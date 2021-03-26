#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Hago la conexión a la BD, obtengo un objeto db"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """Obtengo un cursor para ejecutar las consultas"""
    cur = db.cursor()
    """Ejecuto consulta utilizando el cursor"""
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN\
                states ON cities.state_id = states.id ORDER BY cities.id")
    for i in cur:
        print(cur.fetchone())
    cur.close()
    db.close()
