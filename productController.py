import json
from flask import Flask
from flaskext.mysql import MySQL

# variaveis de ambiente
from env_var import env_var_mysql

# set app
app = Flask(__name__)
mysql = MySQL()

# configura conexão com o db
app.config['MYSQL_DATABASE_HOST'] = env_var_mysql['server']
app.config['MYSQL_DATABASE_PORT'] = env_var_mysql['porta']
app.config['MYSQL_DATABASE_USER'] = env_var_mysql['username']
app.config['MYSQL_DATABASE_PASSWORD'] = env_var_mysql['password']
app.config['MYSQL_DATABASE_DB'] = env_var_mysql['database']
mysql.init_app(app)

class Conn_DB:

    #testa db
    def test_conn():
        conn = mysql.connect()
        cursor = conn.cursor()              
        consulta_nome_db = '''SELECT DATABASE() as 'DB_NAME' '''
        cursor.execute(consulta_nome_db)
        colunas = [coluna[0] for coluna in cursor.description]
        resultados = []
        for linha in cursor.fetchall():
            resultados.append(dict(zip(colunas, linha)))
        json_str = json.dumps(resultados, indent=4, sort_keys=False)
        json_obj = json.loads(json_str)
        return json_obj

    def create_table_product():
        create = f'''CREATE TABLE IF NOT EXISTS product  (id integer, name varchar(50), price decimal, category varchar(50));'''
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(create)
        validar = 'SHOW TABLES;'
        resposta = cursor.execute(validar)
        return  resposta

    def make_select(query):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(query)
        results = []
        columns = [column[0] for column in cursor.description]
        for line in cursor.fetchall():
            results.append(dict(zip(columns, line)))
        return results

    def select_product_name(name):
        select = f'''SELECT * FROM product WHERE name = '{name}'; '''
        return Conn_DB.make_select(select)

    def insert_product(name, price, category):
        insert = f'''INSERT INTO product (name, price, category) values ('{name}', {price}, '{category}');'''
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(insert)
        conn.commit()
        return Conn_DB.select_product_name(name)

#teste
# print(Conn_DB.test_conn())
# print(Conn_DB.create_table_product())
# print(Conn_DB.insert_product('Cotonete', 30.0, 'Hiegiene'))