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
                         color='log_scaled_deaths', 
                         color_continuous_scale='Bluered',
                         size='log_scaled_deaths', 
                         hover_data={total_deaths_label: True, 'log_scaled_deaths': False},  
                         animation_frame=month_label, 
                         projection="natural earth", 
                         title="Total de Mortes no mês por COVID-19 por País",
                         labels={'log_scaled_deaths':'Logarítmo de mortes em escala'},
                         size_max=20)  

    fig.update_layout(title_text='Evolução Mensal de Mortes por COVID-19 mundialmente')
    
    graph_html = fig.to_html(full_html=False)
    
    return graph_html