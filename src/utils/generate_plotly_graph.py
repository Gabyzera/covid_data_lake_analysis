import pandas as pd
import plotly.express as px

def generate_plotly_graph_html(processed_data: list, x_label: str, y_label: str, title: str):
    df = pd.DataFrame(processed_data)
    graph_html = fig.to_html(full_html=False)
    fig = px.bar(df, x=x_label, y=y_label, title=title)
    
    return graph_html
