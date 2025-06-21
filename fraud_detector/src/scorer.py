import pandas as pd
import logging
from catboost import CatBoostClassifier

# Настройка логгера
logger = logging.getLogger(__name__)

logger.info('Importing pretrained model...')

# Import model
model = CatBoostClassifier()
model.load_model('./model/my_catboost.cbm')


logger.info('Pretrained model imported successfully...')

# Make prediction
def make_pred(dt, source_info = 'kafka'):
    model_th = 0.95
    # Make submission dataframe
    submission = pd.DataFrame({
        'score':  model.predict_proba(dt)[:, 1],
        'fraud_flag': (model.predict_proba(dt)[:, 1] > model_th) * 1
    })
    
    logger.info(f'Prediction complete for data from {source_info}')

    # Return proba for positive class
    return submission

