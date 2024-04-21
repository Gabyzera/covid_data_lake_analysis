import os 
import sys
import pandas as pd
import plotly.express as px

script_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(script_dir, '..'))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from us_elections_president.filtered_data import elections_president_2020

def generate_plotly_line_polar_html_graph(processed_data, location_label, average_fully_vaccinated_per_hundred_label):
    most_votes_by_party_df = elections_president_2020()
    averange_vaccinated_per_hundred_df = pd.DataFrame(processed_data)
    combined_elections_president_2020_with_averange_vaccinated_per_hundred_df = pd.merge(averange_vaccinated_per_hundred_df, most_votes_by_party_df, on='Estado', how='left')
    combined_elections_president_2020_with_averange_vaccinated_per_hundred_df['party_simplified'] = combined_elections_president_2020_with_averange_vaccinated_per_hundred_df['party_simplified'].fillna('NO DATA')
    combined_elections_president_2020_with_averange_vaccinated_per_hundred_df['should_render_party_simplified_and_votes'] = combined_elections_president_2020_with_averange_vaccinated_per_hundred_df['party_simplified'] != 'NO DATA'
    combined_elections_president_2020_with_averange_vaccinated_per_hundred_df['hover_candidatevotes'] = combined_elections_president_2020_with_averange_vaccinated_per_hundred_df.apply(
        lambda row: row['candidatevotes'] if row['should_render_party_simplified_and_votes'] else 'SEM INFORMAÇÕES',
        axis=1
    )
    
    PARTY_COLORS = {
        'REPUBLICAN': '#FF3333',
        'DEMOCRAT': '#0033FF',
        'LIBERTARIAN': '#FFFF33',
        'NO DATA': '#CCCCCC'
    }
    fig = px.bar_polar(combined_elections_president_2020_with_averange_vaccinated_per_hundred_df, 
                       r=average_fully_vaccinated_per_hundred_label, 
                       theta=location_label, 
                       color='party_simplified', 
                       color_discrete_map=PARTY_COLORS,
                       hover_data=['party_simplified', 'hover_candidatevotes'],
                       template='plotly_white',
                       labels={
                        'average_fully_vaccinated_per_hundred': 'Média de pessoas totalmente vacinadas por 100 habitantes',
                        'party_simplified': 'Partido mais votado',
                        'hover_candidatevotes': 'Total de votos'
                        },
                        title='As 10 Menores e Maiores Médias de Pessoas Totalmente Vacinadas por 100 Habitantes em Estados Americanos no mês 12/2022') 
 
    fig.add_annotation(
        x=0, y=1.08, 
        xref="paper", yref="paper",
        showarrow=False,
        text='Coloridas pelo Partido Eleitoral que soma o maior número nas Eleições Presidenciais de 2020',
        font=dict(size=16, color="black"),
        align="center"
    )
    
    fig.update_layout(polar=dict(
                        bgcolor='rgba(255, 255, 255, 0.9)',
                        radialaxis=dict(showticklabels=False)), 
                        polar_angularaxis_rotation=90)
    
    graph_html = fig.to_html(full_html=False)
    return graph_html 
