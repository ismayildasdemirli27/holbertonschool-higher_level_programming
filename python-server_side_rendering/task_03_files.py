#!/usr/bin/python3
"""
Task 3: Displaying Data from JSON or CSV Files in Flask
"""
import csv
import json
import os
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(file_path):
    """Read and parse JSON file."""
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_csv_file(file_path):
    """Read and parse CSV file."""
    products = []
    if not os.path.exists(file_path):
        return products
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


@app.route('/products')
def products():
    """Handle products route with source and id query parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template(
            'products.html', error="Wrong source", products=[]
        )

    base_dir = os.path.dirname(__file__)
    data = []

    if source == 'json':
        data = read_json_file(os.path.join(base_dir, 'products.json'))
    elif source == 'csv':
        data = read_csv_file(os.path.join(base_dir, 'products.csv'))

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            product_id = None

        filtered_data = [p for p in data if p.get('id') == product_id]
        if not filtered_data:
            return render_template(
                'products.html', error="Product not found", products=[]
            )
        data = filtered_data

    return render_template('products.html', products=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
