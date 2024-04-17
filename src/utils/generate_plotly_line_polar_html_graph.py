import pandas as pd
import plotly.express as px

from us_elections_president.filtered_data import elections_president_2020

def generate_plotly_line_polar_html_graph(processed_data, location_label, average_fully_vaccinated_per_hundred_label):
    most_votes_by_party_df = elections_president_2020
    averange_vaccinated_per_hundred_df = pd.DataFrame(processed_data)
    combined_elections_president_2020_with_averange_vaccinated_per_hundred_df = pd.merge(averange_vaccinated_per_hundred_df, most_votes_by_party_df, on='state', how='left')

    fig = px.bar_polar(combined_elections_president_2020_with_averange_vaccinated_per_hundred_df, 
                       r=average_fully_vaccinated_per_hundred_label, 
                       theta=location_label, 
                       color=average_fully_vaccinated_per_hundred_label, 
                       color_continuous_scale='Tealgrn',
                       template='plotly_white',
                       title='As 10 Menores e Maiores Médias de Pessoas Vacinadas por 100 Habitantes em Estados Americanos no mês 12/2022')

    fig.update_layout(polar=dict(
                        bgcolor='rgba(255, 255, 255, 0.9)',
                        radialaxis=dict(showticklabels=False)),  
                        polar_angularaxis_rotation=90) 

    graph_html = fig.to_html(full_html=False)
    return graph_html