from flask import Flask, jsonify
from config.flask_config import HOST, PORT
from queries.hospital_beds_query import hospital_beds_query
from queries.global_deaths_query import global_deaths_query
from utils.generate_plotly_3D_graph import generate_plotly_3D_graph
from utils.generate_html_page_for_plot import generate_html_page_for_plot
from utils.generate_plotly_bar_html_graph import generate_plotly_bar_html_graph
from queries.us_states_deaths_and_cases_query import us_states_deaths_and_cases_query
from data_processing.process_global_deaths_response import process_global_deaths_response
from data_processing.proccess_hospital_beds_response import process_hospital_beds_response
from utils.generate_scatter_timeline_html_graph import generate_scatter_timeline_html_graph
from utils.generate_plotly_line_polar_html_graph import generate_plotly_line_polar_html_graph
from data_processing.process_cases_and_deaths_response import process_cases_and_deaths_response
from data_processing.process_dose_pfizer_vaccine_response import process_vaccine_allocation_data
from queries.us_states_vaccinated_per_hundred_query import us_states_vaccinated_per_hundred_query
from utils.generate_html_page_visualization import VisualizationPayload, generate_html_page_visualization
from utils.generate_scatter_global_timeline_html_graph import  generate_scatter_global_timeline_html_graph
from data_processing.process_vaccinated_per_hundred_response import process_vaccinated_per_hundred_response
from queries.us_first_and_second_dose_pfizer_vaccine_query import us_first_and_second_dose_pfizer_vaccine_query

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    message = { 'status': 'OK 👽'}
    
    return jsonify(message)

@app.route('/api/covid/hospital-beds', methods=['GET'])
def get_hospital_beds_availability():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['Estado', 'Total de camas disponíveis'], 
        query_string=hospital_beds_query, 
        bucket_folder_name='hospital-beds-availability-per-state',
        process_response_function=process_hospital_beds_response,
        generate_graph_function=generate_plotly_bar_html_graph, icon_title='🛏️🏥'
    ))

@app.route('/api/covid/us-cases-and-deaths-timeline', methods=['GET'])
def get_covid_us_cases_and_deaths_timeline():
    return generate_html_page_visualization(VisualizationPayload(
        labels=["Estado", "Mês", "Mortes", "Casos"] , 
        query_string=us_states_deaths_and_cases_query, 
        bucket_folder_name='us-states-cases-and-deaths-timeline',
        process_response_function=process_cases_and_deaths_response,
        generate_graph_function=generate_scatter_timeline_html_graph, icon_title='💀🤢'
    ))

@app.route('/api/covid/global-deaths-timeline', methods=['GET'])
def get_covid_global_deaths_timeline():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['País', 'Mês', 'Total de mortes no fim do mês'], 
        query_string=global_deaths_query, 
        bucket_folder_name='global-deaths-timeline',
        process_response_function=process_global_deaths_response,
        generate_graph_function=generate_scatter_global_timeline_html_graph, icon_title='🌎💀'
    ))

@app.route('/api/covid/us-vaccinated-per-hundred', methods=['GET'])
def get_covid_us_vaccinated_per_hundred():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['Estado', 'Média de pessoas totalmente vacinadas por 100 habitantes'], 
        query_string=us_states_vaccinated_per_hundred_query, 
        bucket_folder_name='us-states-vaccinated-per-hundred',
        process_response_function=process_vaccinated_per_hundred_response,
        generate_graph_function=generate_plotly_line_polar_html_graph, icon_title='💉🦠'
    ))

@app.route('/api/covid/us-first-and-second-dose-pfizer', methods=['GET'])
def get_covid_us_first_and_second_dose_pfizer():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['Estado', 'Semana', 'Alocações da primeira dose', 'Alocações da segunda dose'], 
        query_string=us_first_and_second_dose_pfizer_vaccine_query, 
        bucket_folder_name='us-first-and-second-dose-pfizer',
        process_response_function=process_vaccine_allocation_data,
        generate_graph_function=generate_plotly_3D_graph, icon_title='💉💊'
    ))

if __name__ == '__main__': 
    app.run(port=PORT, host=HOST, debug=True)