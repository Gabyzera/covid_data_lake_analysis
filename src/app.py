import pandas as pd
import plotly.express as px
from flask import Flask, jsonify
from config.flask_config import HOST, PORT
from services.run_athena_query import run_athena_query
from queries.hospital_beds_query import hospital_beds_query
from config.aws_config import session, DATABASE_NAME, BUCKET_NAME
from utils.generate_plotly_graph import generate_plotly_graph_html
from utils.generate_html_page_for_plot import generate_html_page_for_plot
from data_processing.hospital_beds.proccess_hospital_beds_response import process_hospital_beds_response

app = Flask(__name__)

@app.route('/health')
def health():
    message = { 'status': 'OK 👽'}
    
    return jsonify(message)

@app.route('/api/covid/hospital-beds', methods=['GET'])
def get_hospital_beds_availability():
    result = run_athena_query(hospital_beds_query, session, DATABASE_NAME, BUCKET_NAME)
    processed_data = process_hospital_beds_response(result)
    hospital_beds_graph = generate_plotly_graph_html(processed_data, 'Estado', 'Total de camas disponíveis', 'Estados americanos e camas disponíveis')

    return generate_html_page_for_plot('🛏️🏥', hospital_beds_graph)

@app.route('/api/covid/cases', methods=['GET'])
def get_covid_cases():
    covid_cases = { 'total_cases': 10000 }
    
    return jsonify(covid_cases)

if __name__ == '__main__': 
    app.run(port=PORT, host=HOST, debug=True)