from flask import (Flask, Blueprint, render_template, request)
from productController import Conn_DB

views = Blueprint(__name__, 'views')

@views.route('/')
def home():
    return render_template('base.html')

@views.route('/createproduct', methods = ['POST', 'GET'])
def create_product():
    if request.method == 'GET':
        return render_template('createProduct.html')

    if request.method == 'POST':
        name = request.form['product_name']
        price = request.form['product_price']
        category = request.form['product_category']
        Conn_DB.insert_product(name, price, category)
        return 'product '+ name + ' added' + ' <a class="nav-link" href="/"> Clique aqui para Voltar</a>'

    else: return 'Deu ruim'