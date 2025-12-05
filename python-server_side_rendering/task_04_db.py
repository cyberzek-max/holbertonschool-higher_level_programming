from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except:
        items_list = []
    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    p_id = request.args.get('id')
    products_list = []
    error_msg = None

    if source == 'json':
        try:
            with open('products.json', 'r') as f:
                products_list = json.load(f)
        except Exception as e:
            error_msg = str(e)
    elif source == 'csv':
        try:
            with open('products.csv', 'r') as f:
                reader = csv.DictReader(f)
                products_list = []
                for row in reader:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                    products_list.append(row)
        except Exception as e:
            error_msg = str(e)
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Products')
            products_list = [dict(row) for row in cursor.fetchall()]
            conn.close()
        except Exception as e:
            error_msg = str(e)
    else:
        error_msg = "Wrong source"

    if not error_msg and p_id:
        try:
            p_id = int(p_id)
            products_list = [p for p in products_list if p['id'] == p_id]
            if not products_list:
                error_msg = "Product not found"
        except ValueError:
             error_msg = "Product not found"

    return render_template('product_display.html', products=products_list, error=error_msg)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
