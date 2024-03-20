import time
from boto3 import Session

def run_athena_query(query: str, session: Session, database_name: str, bucket_name: str, result_path: str):
    athena_client = session.client('athena')
    response = athena_client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database_name
        },
        ResultConfiguration={
            'OutputLocation': f's3://{bucket_name}/{result_path}',
        }
    )
    query_execution_id = response['QueryExecutionId']
    
    while True:
        response = athena_client.get_query_execution(QueryExecutionId=query_execution_id)
        state = response['QueryExecution']['Status']['State']
        
        if state == 'SUCCEEDED':
            print("Finished athena query execution")
            break
        
        elif state in ['FAILED', 'CANCELLED']:
            return None
        
        time.sleep(5) 
    
    result = athena_client.get_query_results(QueryExecutionId=query_execution_id)
    return result