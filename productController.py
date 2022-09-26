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

class Conexao_DB:

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


print(Conexao_DB.test_conn())
print(Conexao_DB.create_table_product())
