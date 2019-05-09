import sqlite3

def operator_sql(sql):
    con = sqlite3.connect('apirest.db')
    cur = con.cursor()
    cur.execute(sql)
    con.commit()
    cur.close()
    con.close()


def select_all(table):
    con = sqlite3.connect('apirest.db')
    cur = con.cursor()
    cur.execute("select * from {};".format(table))
    recursos = cur.fetchall()
    cur.close()
    con.close()
    recursos_json = []
    for recurso in recursos:
        recurso_json = {}
        recurso_json['id'] = recurso[0]
        recurso_json['nome'] = recurso[1]
        recursos_json.append(recurso_json)
    return recursos_json