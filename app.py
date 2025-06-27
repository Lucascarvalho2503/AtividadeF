# app.py

from flask import Flask, render_template, request, redirect, url_for

# Inicializa a aplicação Flask
app = Flask(__name__)

# --- BANCO DE DADOS EM MEMÓRIA (PARA SIMPLICIDADE) ---
# Em um projeto real, você usaria um banco de dados como SQLite, PostgreSQL, etc.
# Usaremos listas e dicionários para simular um banco de dados.

# Dados dos Fornecedores
suppliers_db = [
    {'id': 1, 'name': 'Fornecedor A'},
    {'id': 2, 'name': 'Fornecedor B'}
]
supplier_id_counter = 2  # Contador para o próximo ID de fornecedor

# Dados dos Produtos
products_db = [
    {'id': 1, 'name': 'Produto 1', 'price': 10.50, 'supplier_id': 1},
    {'id': 2, 'name': 'Produto 2', 'price': 25.00, 'supplier_id': 2},
    {'id': 3, 'name': 'Produto 3', 'price': 5.75, 'supplier_id': 1}
]
product_id_counter = 3  # Contador para o próximo ID de produto

# --- ROTA PRINCIPAL ---
@app.route('/')
def index():
    return redirect(url_for('list_products'))

# ========== CRUD DE FORNECEDORES ==========

# READ (Listar todos os fornecedores)
@app.route('/suppliers')
def list_suppliers():
    return render_template('suppliers.html', suppliers=suppliers_db)

# CREATE (Adicionar novo fornecedor)
@app.route('/suppliers/add', methods=['GET', 'POST'])
def add_supplier():
    if request.method == 'POST':
        global supplier_id_counter
        supplier_id_counter += 1
        new_supplier = {
            'id': supplier_id_counter,
            'name': request.form['name']
        }
        suppliers_db.append(new_supplier)
        return redirect(url_for('list_suppliers'))
    return render_template('add_supplier.html')

# UPDATE (Editar um fornecedor existente)
@app.route('/suppliers/edit/<int:id>', methods=['GET', 'POST'])
def edit_supplier(id):
    supplier = next((s for s in suppliers_db if s['id'] == id), None)
    if not supplier:
        return "Fornecedor não encontrado!", 404

    if request.method == 'POST':
        supplier['name'] = request.form['name']
        return redirect(url_for('list_suppliers'))
    
    return render_template('edit_supplier.html', supplier=supplier)

# DELETE (Deletar um fornecedor)
@app.route('/suppliers/delete/<int:id>', methods=['POST'])
def delete_supplier(id):
    global suppliers_db
    # Aviso: Isso também deveria deletar ou desassociar produtos relacionados
    suppliers_db = [s for s in suppliers_db if s['id'] != id]
    return redirect(url_for('list_suppliers'))


# ========== CRUD DE PRODUTOS ==========

# READ (Listar todos os produtos)
@app.route('/products')
def list_products():
    # Adiciona o nome do fornecedor a cada produto para exibição
    for product in products_db:
        supplier = next((s for s in suppliers_db if s['id'] == product['supplier_id']), None)
        product['supplier_name'] = supplier['name'] if supplier else 'N/A'
    return render_template('products.html', products=products_db)

# CREATE (Adicionar novo produto)
@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        global product_id_counter
        product_id_counter += 1
        new_product = {
            'id': product_id_counter,
            'name': request.form['name'],
            'price': float(request.form['price']),
            'supplier_id': int(request.form['supplier_id'])
        }
        products_db.append(new_product)
        return redirect(url_for('list_products'))
    # Passa a lista de fornecedores para o template para o menu dropdown
    return render_template('add_product.html', suppliers=suppliers_db)

# UPDATE (Editar um produto existente)
@app.route('/products/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    product = next((p for p in products_db if p['id'] == id), None)
    if not product:
        return "Produto não encontrado!", 404

    if request.method == 'POST':
        product['name'] = request.form['name']
        product['price'] = float(request.form['price'])
        product['supplier_id'] = int(request.form['supplier_id'])
        return redirect(url_for('list_products'))
    
    return render_template('edit_product.html', product=product, suppliers=suppliers_db)

# DELETE (Deletar um produto)
@app.route('/products/delete/<int:id>', methods=['POST'])
def delete_product(id):
    global products_db
    products_db = [p for p in products_db if p['id'] != id]
    return redirect(url_for('list_products'))


# --- Executa a aplicação ---
if __name__ == '__main__':
    # O modo debug reinicia o servidor automaticamente a cada alteração no código.
    app.run(debug=True)