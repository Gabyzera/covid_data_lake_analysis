import plotly.express as px
import pandas as pd

def generate_scatter_timeline_html_graph(processed_data, state_label: str, month_label: str, deaths_label: str, cases_label: str):
    df = pd.DataFrame(processed_data)

    fig = px.scatter(df, x=cases_label, y=deaths_label,
                    animation_frame=month_label, animation_group=state_label,
                    
                    color=state_label, hover_name=state_label,
                    size=cases_label, log_x=True, size_max=55,
                    range_y=[0, max(df[deaths_label])])

    fig.update_layout(title_text='Evolução Mensal de Casos e Mortes por COVID-19 por Estado Americano')
    
    graph_html = fig.to_html(full_html=False)
    
    return graph_html