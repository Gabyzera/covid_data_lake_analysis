import pandas as pd
import plotly.express as px

def generate_plotly_3D_graph(processed_data, jurisdiction_label, week_of_allocations_label, first_dose_allocations_label, second_dose_allocations_label):
    pfizer_df = pd.DataFrame(processed_data)
    pfizer_df[week_of_allocations_label] = pd.to_datetime(pfizer_df[week_of_allocations_label]).dt.date

    fig = px.scatter_3d(pfizer_df,
                        x=first_dose_allocations_label,
                        y=week_of_allocations_label,
                        z=second_dose_allocations_label,
                        size=first_dose_allocations_label, 
                        color=jurisdiction_label,    
                        hover_name=jurisdiction_label,    
                        title='Distribuição de Primeiras e Segundas Doses da Vacina Pfizer')

    # Melhorar a formatação da data no eixo Y para exibir apenas o mês e o ano
    fig.update_layout(xaxis=dict(tickformat="%m-%Y"))
    graph_html = fig.to_html(full_html=False)
    
    return graph_html
