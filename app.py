from flask import Flask, render_template, request, redirect, url_for
from models import Seasonal, Inventory, Allergens, Suggestions, Cart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/seasonal', methods=['GET', 'POST'])
def add_seasonal():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        avail_start = request.form['avail_start']
        avail_end = request.form['avail_end']
        seasonal = Seasonal()
        seasonal.add(name, description, avail_start, avail_end)
        return redirect(url_for('index'))
    return render_template('seasonal.html')

@app.route('/inventory', methods=['GET', 'POST'])
def add_inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        inventory = Inventory()
        inventory.add(name, quantity)
        return redirect(url_for('index'))
    return render_template('inventory.html')

@app.route('/allergens', methods=['GET', 'POST'])
def add_allergens():
    if request.method == 'POST':
        name = request.form['name']
        allergen = Allergens()
        allergen.add(name)
        return redirect(url_for('index'))
    return render_template('allergens.html')

@app.route('/suggestions', methods=['GET', 'POST'])
def add_suggestions():
    if request.method == 'POST':
        flav_name = request.form['flav_name']
        cust_name = request.form['cust_name']
        suggestion = request.form['suggestion']
        allergy_concerns = request.form['allergy_concerns']
        suggestion_obj = Suggestions()
        suggestion_obj.add(flav_name, cust_name, suggestion, allergy_concerns)
        return redirect(url_for('index'))
    return render_template('suggestions.html')

@app.route('/cart', methods=['GET', 'POST'])
def add_cart():
    if request.method == 'POST':
        prod_id = request.form['prod_id']
        prod_name = request.form['prod_name']
        cart = Cart()
        cart.add(prod_id, prod_name)
        return redirect(url_for('index'))
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
