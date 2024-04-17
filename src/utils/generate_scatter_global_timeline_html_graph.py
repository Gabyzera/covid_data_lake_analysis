import numpy as np
import pandas as pd
import plotly.express as px

def generate_scatter_global_timeline_html_graph(processed_data, country_label, month_label, total_deaths_label):
    df = pd.DataFrame(processed_data)
    df['log_scaled_deaths'] = np.log10(df[total_deaths_label] + 1) * 5
    
    fig = px.scatter_geo(df,
                         locations=country_label,
                         locationmode='country names',
                         template='seaborn',
                         color=total_deaths_label,  # Represents each country by color
                         color_continuous_scale='Tealgrn',
                         size='log_scaled_deaths',  # Uses log-scaled deaths for size
                         hover_data={total_deaths_label: True, 'log_scaled_deaths': False},  # Information displayed when hovering over points
                         animation_frame=month_label,  # Creates an animation based on month
                         projection="natural earth",  # Type of map projection
                         title="Total de Mortes no mês por COVID-19 por País",
                         size_max=20)  # Adjust size_max if needed

    fig.update_layout(title_text='Evolução Mensal de Mortes por COVID-19 mundialmente')
    
    graph_html = fig.to_html(full_html=False)
    
    return graph_html