#!/usr/bin/python3
"""
Task 2: Creating a Dynamic Template with Loops and Conditions in Flask
"""
import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    """Read items from JSON and render items.html template."""
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    items_list = []
    
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            items_list = data.get('items', [])

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
