import pandas as pd
import os

def elections_president_2020():
    current_dir = os.path.dirname(__file__) 
    PRESIDENT_DATA_PATH = os.path.join(current_dir, '1976-2020-president.csv')
    data_president_df = pd.read_csv(PRESIDENT_DATA_PATH)

    data_president_df = data_president_df.rename(columns={'state': 'Estado'})
    data_president_year_2020_df = data_president_df[data_president_df['year'] == 2020]
    columns_relevant = ['Estado', 'candidatevotes', 'party_simplified']
    data_president_columns_filtered_df = data_president_year_2020_df[columns_relevant]
        
    state_party_sum_of_votes_df = data_president_columns_filtered_df.groupby(['Estado', 'party_simplified'])['candidatevotes'].sum().reset_index()
        
    index_party_bigger_vote_by_state_df = state_party_sum_of_votes_df.groupby(['Estado'])['candidatevotes'].transform(max) == state_party_sum_of_votes_df['candidatevotes']
        
    most_votes_by_party_df = state_party_sum_of_votes_df[index_party_bigger_vote_by_state_df]
    most_votes_by_party_df = most_votes_by_party_df.drop_duplicates(subset=['Estado'], keep='first') # Se houver empates, isso manterá apenas a primeira ocorrência
    
    return most_votes_by_party_df