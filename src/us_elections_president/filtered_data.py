import pandas as pd

def elections_president_2020():
    PRESIDENT_DATA_PATH = ('1976-2020-president.csv')
    data_president_df = pd.read_csv(PRESIDENT_DATA_PATH)
    columns_relevant = ['year', 'state', 'candidate', 'candidatevotes', 'party_simplified']

    data_president_year_2020_df = data_president_df[data_president_df['year'] == 2020]
    
    data_president_columns_filtered_df = data_president_year_2020_df[columns_relevant]
    
    state_party_sum_of_votes_df = data_president_columns_filtered_df.groupby(['state', 'party_simplified'])['candidatevotes'].sum().reset_index()
    
    index_party_bigger_vote_by_state_df = state_party_sum_of_votes_df.groupby(['state'])['candidatevotes'].transform(max) == state_party_sum_of_votes_df['candidatevotes']
    
    most_votes_by_party_df = state_party_sum_of_votes_df[index_party_bigger_vote_by_state_df]
    most_votes_by_party_df = most_votes_by_party_df.drop_duplicates(subset=['state'], keep='first') # Se houver empates, isso manterá apenas a primeira ocorrência
    
    return most_votes_by_party_df