#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all cities
 of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Hago la conexión a la BD, obtengo un objeto db"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=argv[1], passwd=argv[2], db=argv[3])
    """Obtengo un cursor para ejecutar las consultas"""
    cur = db.cursor()
    """Ejecuto consulta utilizando el cursor"""
    cur.execute("SELECT cities.name FROM cities JOIN states ON \
                cities.state_id = states.id WHERE states.name LIKE %s\
                ORDER BY cities.id", (argv[4],))
    listcity = []
    for i in cur:
        listcity.append(i[0])
    print(', '.join(listcity))
    cur.close()
    db.close()
