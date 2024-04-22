import pandas as pd
import plotly.express as px

def generate_plotly_bar_html_graph(processed_data: list, x_label: str, y_label: str):
    df = pd.DataFrame(processed_data)
    
    fig = px.bar(df,
                 x=x_label, 
                 y=y_label, 
                 color=x_label, 
                 title='Estados americanos e camas disponíveis')
    graph_html = fig.to_html(full_html=False)
    
    return graph_html