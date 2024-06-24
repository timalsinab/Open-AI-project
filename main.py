from flask import Flask, request, jsonify
import requests
import os
import pandas as pd
import sqlalchemy as db

app = Flask(__name__)

API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
if not API_KEY:
    raise ValueError("No API key set for OpenWeatherMap API. Please set the OPENWEATHERMAP_API_KEY environment variable.")

# Create an engine object for SQLite database
engine = db.create_engine('sqlite:///weather_data.db')

@app.route('/weather', methods=['POST'])
def get_weather():
    data = request.get_json()
    city = data.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': 'City not found'}), 404

    weather_data = response.json()
    result = {
        'city': weather_data['name'],
        'temperature': weather_data['main']['temp'],
        'description': weather_data['weather'][0]['description']
    }

    # Convert dictionary to DataFrame
    df = pd.DataFrame([result])

    # Save DataFrame to SQL database
    df.to_sql('weather', con=engine, if_exists='replace', index=False)

    return jsonify(result)

@app.route('/weather_data', methods=['GET'])
def get_weather_data():
    with engine.connect() as connection:
        query_result = connection.execute(db.text("SELECT * FROM weather;")).fetchall()
        df = pd.DataFrame(query_result, columns=['city', 'temperature', 'description'])
        return df.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
