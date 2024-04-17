import pandas as pd
import plotly.express as px

def generate_plotly_line_polar_html_graph(processed_data, location_label, average_fully_vaccinated_per_hundred_label):
    df = pd.DataFrame(processed_data)

    fig = px.bar_polar(df, 
                       r=average_fully_vaccinated_per_hundred_label, 
                       theta=location_label, 
                       color=location_label, 
                       template='plotly_white',
                       title='Média de Pessoas Vacinadas por 100 Habitantes no Estado Americano no mês 12/2022')

    fig.update_layout(polar=dict(
                        bgcolor='rgba(255, 255, 255, 0.9)',
                        radialaxis=dict(showticklabels=False)),  
                        polar_angularaxis_rotation=90) 

    graph_html = fig.to_html(full_html=False)
    return graph_html
