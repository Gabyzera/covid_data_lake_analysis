import pandas as pd
import plotly.express as px

def generate_plotly_graph_area(processed_data, location_label, total_vaccinations_label, people_fully_vaccinated_label):
    df = pd.DataFrame(processed_data)
    
    fig = px.area(df, 
                  x=location_label, 
                  y=[people_fully_vaccinated_label, total_vaccinations_label], 
                  labels={location_label: 'Estado', 
                        'variable': 'Métrica',
                        people_fully_vaccinated_label:'Total de doses administradas', 
                        total_vaccinations_label:'Pessoas totalmente vacinadas' },
                  title='Total de vacinas providenciadas ao Estado e Pessoas Totalmente Vacinadas em maio de 2023')
    
    fig.update_layout(yaxis_title='Número de Vacinações')
    graph_html = fig.to_html(full_html=False)

    return graph_html