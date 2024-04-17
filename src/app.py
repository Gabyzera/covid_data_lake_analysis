from flask import Flask, jsonify
from config.flask_config import HOST, PORT
from services.run_athena_query import run_athena_query
from queries.hospital_beds_query import hospital_beds_query
from queries.global_deaths_query import global_deaths_query
from config.aws_config import session, DATABASE_NAME, BUCKET_NAME
from utils.generate_html_page_for_plot import generate_html_page_for_plot
from utils.generate_plotly_bar_html_graph import generate_plotly_bar_html_graph
from queries.us_states_deaths_and_cases_query import us_states_deaths_and_cases_query
from data_processing.process_global_deaths_response import process_global_deaths_response
from data_processing.proccess_hospital_beds_response import process_hospital_beds_response
from utils.generate_scatter_timeline_html_graph import generate_scatter_timeline_html_graph
from utils.generate_plotly_line_polar_html_graph import generate_plotly_line_polar_html_graph
from data_processing.process_cases_and_deaths_response import process_cases_and_deaths_response
from queries.us_states_vaccinated_per_hundred_query import us_states_vaccinated_per_hundred_query
from utils.generate_scatter_global_timeline_html_graph import  generate_scatter_global_timeline_html_graph
from data_processing.process_vaccinated_per_hundred_response import process_vaccinated_per_hundred_response

app = Flask(__name__)

@app.route('/')
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

@app.route('/api/covid/us-cases-and-deaths-timeline', methods=['GET'])
def get_covid_us_cases_and_deaths_timeline():
    state_label, month_label, deaths_label, cases_label = ["Estado", "Mês", "Mortes", "Casos"] 
    
    result = run_athena_query(us_states_deaths_and_cases_query, session, DATABASE_NAME, BUCKET_NAME, 'us-states-cases-and-deaths-timeline')
    processed_data = process_cases_and_deaths_response(result, state_label, month_label, deaths_label, cases_label)
    cases_and_deaths_graph = generate_scatter_timeline_html_graph(processed_data, state_label, month_label, deaths_label, cases_label)

    return generate_html_page_for_plot('💀🤢', cases_and_deaths_graph)

@app.route('/api/covid/global-deaths-timeline', methods=['GET'])
def get_covid_global_deaths_timeline():
    country_label, month_label, total_deaths_label = ['País', 'Mês', 'Total de mortes no fim do mês']
    
    result = run_athena_query(global_deaths_query, session, DATABASE_NAME, BUCKET_NAME, 'global-deaths-timeline')
    
    processed_data = process_global_deaths_response(result, country_label, month_label, total_deaths_label)
    global_deaths_graph = generate_scatter_global_timeline_html_graph(processed_data, country_label, month_label, total_deaths_label)
    
    return generate_html_page_for_plot('🌎💀', global_deaths_graph)

@app.route('/api/covid/us-vaccinated-per-hundred', methods=['GET'])
def get_covid_us_vaccinated_per_hundred():
    location_label, average_fully_vaccinated_per_hundred_label = ['Estado', 'Média de pessoas totalmente vacinadas por 100 habitantes']
    
    result = run_athena_query(us_states_vaccinated_per_hundred_query, session, DATABASE_NAME, BUCKET_NAME, 'us-states-vaccinated-per-hundred')
    
    processed_data = process_vaccinated_per_hundred_response(result, location_label, average_fully_vaccinated_per_hundred_label)
    vaccinated_per_hundred_graph = generate_plotly_line_polar_html_graph(processed_data, location_label, average_fully_vaccinated_per_hundred_label)
    
    return generate_html_page_for_plot('💉🦠', vaccinated_per_hundred_graph)

if __name__ == '__main__': 
    app.run(port=PORT, host=HOST, debug=True)