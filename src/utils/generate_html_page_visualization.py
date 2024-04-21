from dataclasses import dataclass
from config.aws_config import session
from typing import Any, Callable, List
from services.run_athena_query import run_athena_query
from config.aws_config import DATABASE_NAME, BUCKET_NAME
from utils.generate_html_page_for_plot import generate_html_page_for_plot


@dataclass
class VisualizationPayload:
    icon_title: str
    query_string: str
    labels: List[str]
    bucket_folder_name: str
    process_response_function: Callable[[Any, List[str]], Any]
    generate_graph_function: Callable[[Any, List[str]], Any]

def generate_html_page_visualization(payload: VisualizationPayload):
    result = run_athena_query(payload.query_string, session, DATABASE_NAME, BUCKET_NAME, payload.bucket_folder_name)
    
    processed_data = payload.process_response_function(result, *payload.labels)
    graph = payload.generate_graph_function(processed_data, *payload.labels)

    return generate_html_page_for_plot(payload.icon_title, graph)