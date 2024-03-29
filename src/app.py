from flask import Flask, jsonify
from config.flask_config import HOST, PORT
from services.run_athena_query import run_athena_query
from queries.hospital_beds_query import hospital_beds_query
from config.aws_config import session, DATABASE_NAME, BUCKET_NAME
from utils.generate_html_page_for_plot import generate_html_page_for_plot
from utils.generate_plotly_bar_html_graph import generate_plotly_bar_html_graph
from queries.us_states_deaths_and_cases_query import us_states_deaths_and_cases_query
from data_processing.proccess_hospital_beds_response import process_hospital_beds_response
from data_processing.process_cases_and_deaths_response import process_cases_and_deaths_response
from utils.generate_scatter_timeline_html_graph import generate_scatter_timeline_html_graph

app = Flask(__name__)

@app.route('/health')
def health():
    message = { 'status': 'OK 👽'}
    
    return jsonify(message)

@app.route('/api/covid/hospital-beds', methods=['GET'])
def get_hospital_beds_availability():
    x_label, y_label = ['Estado', 'Total de camas disponíveis']
    
    result = run_athena_query(hospital_beds_query, session, DATABASE_NAME, BUCKET_NAME, 'hospital-beds-availability-per-state')
    processed_data = process_hospital_beds_response(result, x_label, y_label)
    hospital_beds_graph = generate_plotly_bar_html_graph(processed_data, x_label, y_label, 'Estados americanos e camas disponíveis')

    return generate_html_page_for_plot('🛏️🏥', hospital_beds_graph)

@app.route('/api/covid/cases-and-deaths-timeline', methods=['GET'])
def get_covid_cases_and_deaths_timeline():
    state_label, month_label, deaths_label, cases_label = ["Estado", "Mês", "Mortes", "Casos"] 
    
    result = run_athena_query(us_states_deaths_and_cases_query, session, DATABASE_NAME, BUCKET_NAME, 'us-states-cases-and-deaths-timeline')
    processed_data = process_cases_and_deaths_response(result, state_label, month_label, deaths_label, cases_label)
    cases_and_deaths_graph = generate_scatter_timeline_html_graph(processed_data, state_label, month_label, deaths_label, cases_label)

    return generate_html_page_for_plot('💀🤢', cases_and_deaths_graph)

if __name__ == '__main__': 
    app.run(port=PORT, host=HOST, debug=True)