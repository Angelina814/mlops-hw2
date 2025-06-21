# Import standard libraries
import pandas as pd
import numpy as np
import logging


logger = logging.getLogger(__name__)
RANDOM_STATE = 42


def add_combined_features(df):
    logger.debug('Adding combined features: full_name and city_state...')
    
    # Создание признака full_name
    df['full_name'] = df['name_1'].astype(str) + '_' + df['name_2'].astype(str)
    
    # Создание признака city_state
    df['city_state'] = df['one_city'].astype(str) + '_' + df['us_state'].astype(str)
    
    logger.debug('Combined features added. Shape: %s', df.shape)
    return df


def select_base_features(df):
    logger.debug('Selecting base numerical and categorical features...')

    num_columns = ['amount', 'population_city', 'merchant_lat', 'merchant_lon']
    cat_columns = ['merch', 'cat_id', 'gender', 'post_code', 'jobs', 'us_state', 'full_name', 'city_state']

    df_processed = df[num_columns + cat_columns].copy()

    # Преобразование категориальных признаков
    for col in cat_columns:
        df_processed[col] = df_processed[col].fillna('nan').astype(str)

    logger.debug('Base features selected. Shape: %s', df_processed.shape)
    return df_processed, cat_columns

# Main preprocessing function
def run_preproc(input_df):

    # Define column types
    target_col = 'target'

    logger.info('Starting preprocessing...')

    input_df = add_combined_features(input_df)

    output_df, categorical_cols = select_base_features(input_df)

    
    # Return resulting dataset
    return output_df



