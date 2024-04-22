from flask import Flask, jsonify
from config.flask_config import HOST, PORT
from queries.hospital_beds_query import hospital_beds_query
from queries.global_deaths_query import global_deaths_query
from utils.generate_plotly_graph_area import generate_plotly_graph_area
from utils.generate_plotly_bar_html_graph import generate_plotly_bar_html_graph
from queries.us_states_deaths_and_cases_query import us_states_deaths_and_cases_query
from data_processing.process_global_deaths_response import process_global_deaths_response
from data_processing.proccess_hospital_beds_response import process_hospital_beds_response
from utils.generate_scatter_timeline_html_graph import generate_scatter_timeline_html_graph
from utils.generate_plotly_line_polar_html_graph import generate_plotly_line_polar_html_graph
from data_processing.process_cases_and_deaths_response import process_cases_and_deaths_response
from queries.us_states_vaccinated_per_hundred_query import us_states_vaccinated_per_hundred_query
from utils.generate_html_page_visualization import VisualizationPayload, generate_html_page_visualization
from utils.generate_scatter_global_timeline_html_graph import  generate_scatter_global_timeline_html_graph
from data_processing.process_vaccinated_per_hundred_response import process_vaccinated_per_hundred_response
from queries.us_total_vaccinations_and_people_fully_vaccinated_query import us_total_vaccinations_and_people_fully_vaccinated_query
from data_processing.process_total_vaccinations_and_people_fully_vaccinated_response import process_total_vaccinations_and_people_fully_vaccinated_response
from config.aws_config import BUCKET_FOLDER_CASES_AND_DEATHS, BUCKET_FOLDER_GLOBAL_DEATHS, BUCKET_FOLDER_HOSPITAL_BEDS, BUCKET_FOLDER_VACCINATED_PER_HUNDRED, \
    BUCKET_FOLDER_VACCINES_AND_VACCINATED

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
        bucket_folder_name=BUCKET_FOLDER_HOSPITAL_BEDS,
        process_response_function=process_hospital_beds_response,
        generate_graph_function=generate_plotly_bar_html_graph, icon_title='🛏️🏥'
    ))

@app.route('/api/covid/us-cases-and-deaths-timeline', methods=['GET'])
def get_covid_us_cases_and_deaths_timeline():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['Estado', 'Mês', 'Mortes', 'Casos'] , 
        query_string=us_states_deaths_and_cases_query, 
        bucket_folder_name=BUCKET_FOLDER_CASES_AND_DEATHS,
        process_response_function=process_cases_and_deaths_response,
        generate_graph_function=generate_scatter_timeline_html_graph, icon_title='💀🤢'
    ))

@app.route('/api/covid/global-deaths-timeline', methods=['GET'])
def get_covid_global_deaths_timeline():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['País', 'Mês', 'Total de mortes no fim do mês'], 
        query_string=global_deaths_query, 
        bucket_folder_name=BUCKET_FOLDER_GLOBAL_DEATHS,
        process_response_function=process_global_deaths_response,
        generate_graph_function=generate_scatter_global_timeline_html_graph, icon_title='🌎💀'
    ))

@app.route('/api/covid/us-vaccinated-per-hundred', methods=['GET'])
def get_covid_us_vaccinated_per_hundred():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['Estado', 'Média de pessoas totalmente vacinadas por 100 habitantes'], 
        query_string=us_states_vaccinated_per_hundred_query, 
        bucket_folder_name=BUCKET_FOLDER_VACCINATED_PER_HUNDRED,
        process_response_function=process_vaccinated_per_hundred_response,
        generate_graph_function=generate_plotly_line_polar_html_graph, icon_title='💉🦠'
    ))

@app.route('/api/covid/us-total-vaccinations-people-fully-vaccinated', methods=['GET'])
def get_covid_us_total_vaccinations_people_fully_vaccinated():
    return generate_html_page_visualization(VisualizationPayload(
        labels=['Estado', 'Total de doses administradas', 'Pessoas totalmente vacinadas'], 
        query_string=us_total_vaccinations_and_people_fully_vaccinated_query, 
        bucket_folder_name=BUCKET_FOLDER_VACCINES_AND_VACCINATED,
        process_response_function=process_total_vaccinations_and_people_fully_vaccinated_response,
        generate_graph_function=generate_plotly_graph_area, icon_title='👥💉'
    ))

if __name__ == '__main__': 
    app.run(port=PORT, host=HOST, debug=True)