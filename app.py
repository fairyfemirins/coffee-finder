#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
import sqlite3
import json

app = Flask(__name__)

# Initialize SQLite database
conn = sqlite3.connect('coffee_shops.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS coffee_shops (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        latitude REAL,
        longitude REAL,
        wifi_rating INTEGER,
        outlet_rating INTEGER,
        coffee_rating INTEGER,
        vibe_rating INTEGER,
        address TEXT,
        city TEXT
    )
''')

# Insert mock data
cursor.execute('''
    INSERT OR IGNORE INTO coffee_shops 
    (name, latitude, longitude, wifi_rating, outlet_rating, coffee_rating, vibe_rating, address, city)
    VALUES
    ('The Daily Grind', 37.7749, -122.4194, 5, 4, 5, 4, '123 Market St', 'San Francisco'),
    ('Brew Haven', 37.7841, -122.4036, 4, 5, 5, 5, '456 Mission St', 'San Francisco'),
    ('Nomad Beans', 40.7128, -74.0060, 5, 3, 4, 4, '789 Broadway', 'New York'),
    ('Café Remote', 51.5074, -0.1278, 4, 4, 5, 5, '10 Downing St', 'London')
''')
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    city = request.args.get('city', '')
    wifi = request.args.get('wifi', 0, type=int)
    outlets = request.args.get('outlets', 0, type=int)
    coffee = request.args.get('coffee', 0, type=int)
    vibe = request.args.get('vibe', 0, type=int)
    
    query = "SELECT * FROM coffee_shops WHERE 1=1"
    params = []
    
    if city:
        query += " AND city LIKE ?"
        params.append(f"%{city}%")
    if wifi:
        query += " AND wifi_rating >= ?"
        params.append(wifi)
    if outlets:
        query += " AND outlet_rating >= ?"
        params.append(outlets)
    if coffee:
        query += " AND coffee_rating >= ?"
        params.append(coffee)
    if vibe:
        query += " AND vibe_rating >= ?"
        params.append(vibe)
    
    cursor.execute(query, params)
    results = cursor.fetchall()
    
    shops = []
    for row in results:
        shops.append({
            'id': row[0],
            'name': row[1],
            'latitude': row[2],
            'longitude': row[3],
            'wifi_rating': row[4],
            'outlet_rating': row[5],
            'coffee_rating': row[6],
            'vibe_rating': row[7],
            'address': row[8],
            'city': row[9]
        })
    
    return jsonify(shops)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015, debug=True)