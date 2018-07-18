import numpy as np
import pandas as pd
from os import path

src_path = path.dirname(path.realpath(__file__))


def compute_missing_values(df):
  _size = len(df)
  nulls = df.isnull().sum()
  nulls = nulls[nulls != 0].sort_values(ascending=False)
  nulls_percent = 100 * nulls / _size
  return pd.DataFrame({'NaN Count': nulls, 'NaN %': nulls_percent}) 


def outliers_iqr(ys, k=1.5):
  quartile_1, quartile_3 = np.percentile(ys, [25, 75])
  iqr = quartile_3 - quartile_1
  lower_bound = quartile_1 - (iqr * k)
  upper_bound = quartile_3 + (iqr * k)
  return np.where((ys > upper_bound) | (ys < lower_bound))


def idx_of_missing_values(df, threshold=90):
  to_remove = []
  for idx, row in df.iterrows():
    if row['NaN %'] > threshold:
      to_remove.append(idx)
  return to_remove  


def save_prediction(data, name):
    file_path = '%s/submissions/submission-%s.csv' % (src_path, name)
    data[['SK_ID_CURR', 'TARGET']].to_csv(file_path, index=False)
    return 'kaggle competitions submit -c home-credit-default-risk -f %s -m "%s"' % (file_path, name)

####

appartment_avg_cols = ['APARTMENTS_AVG', 'BASEMENTAREA_AVG', 'COMMONAREA_AVG', 'ELEVATORS_AVG',
                       'ENTRANCES_AVG', 'FLOORSMAX_AVG', 'FLOORSMIN_AVG', 'LANDAREA_AVG', 'LIVINGAPARTMENTS_AVG',
                       'LIVINGAREA_AVG']

appartment_mode_cols = ['APARTMENTS_MODE', 'BASEMENTAREA_MODE', 'COMMONAREA_MODE',
                        'ELEVATORS_MODE', 'ENTRANCES_MODE', 'FLOORSMAX_MODE', 'FLOORSMIN_MODE', 'LANDAREA_MODE',
                        'LIVINGAPARTMENTS_MODE', 'LIVINGAREA_MODE']

appartment_medi_cols = ['APARTMENTS_MEDI', 'BASEMENTAREA_MEDI', 'COMMONAREA_MEDI', 'ELEVATORS_MEDI',
                        'ENTRANCES_MEDI', 'FLOORSMAX_MEDI', 'FLOORSMIN_MEDI',
                        'LANDAREA_MEDI', 'LIVINGAPARTMENTS_MEDI', 'LIVINGAREA_MEDI']

docs_flags = ['FLAG_DOCUMENT_2', 'FLAG_DOCUMENT_3', 'FLAG_DOCUMENT_4', 'FLAG_DOCUMENT_5',
              'FLAG_DOCUMENT_6', 'FLAG_DOCUMENT_7', 'FLAG_DOCUMENT_8', 'FLAG_DOCUMENT_9',
              'FLAG_DOCUMENT_10', 'FLAG_DOCUMENT_11', 'FLAG_DOCUMENT_12', 'FLAG_DOCUMENT_13',
              'FLAG_DOCUMENT_14', 'FLAG_DOCUMENT_15', 'FLAG_DOCUMENT_16', 'FLAG_DOCUMENT_17',
              'FLAG_DOCUMENT_18', 'FLAG_DOCUMENT_19', 'FLAG_DOCUMENT_20', 'FLAG_DOCUMENT_21']

personal_info_flags = ['FLAG_MOBIL', 'FLAG_EMP_PHONE', 'FLAG_WORK_PHONE', 'FLAG_CONT_MOBILE',
                      'FLAG_PHONE', 'FLAG_EMAIL', 'REG_REGION_NOT_LIVE_REGION',
                      'REG_REGION_NOT_WORK_REGION', 'LIVE_REGION_NOT_WORK_REGION', 'REG_CITY_NOT_LIVE_CITY',
                      'REG_CITY_NOT_WORK_CITY', 'LIVE_CITY_NOT_WORK_CITY',
                      'FLAG_OWN_CAR', 'FLAG_OWN_REALTY']

num_enq = ['AMT_REQ_CREDIT_BUREAU_HOUR', 'AMT_REQ_CREDIT_BUREAU_DAY', 'AMT_REQ_CREDIT_BUREAU_WEEK',
           'AMT_REQ_CREDIT_BUREAU_MON', 'AMT_REQ_CREDIT_BUREAU_QRT', 'AMT_REQ_CREDIT_BUREAU_YEAR']

social_dpd = ['OBS_30_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE',
              'OBS_60_CNT_SOCIAL_CIRCLE', 'DEF_60_CNT_SOCIAL_CIRCLE']

days_duration = [ 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'DAYS_LAST_PHONE_CHANGE']

financial_info = ['AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY', 'AMT_GOODS_PRICE',
                  'EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3']

others = ['NAME_CONTRACT_TYPE', 'CODE_GENDER', 'CNT_CHILDREN', 'NAME_TYPE_SUITE', 'NAME_INCOME_TYPE', 'NAME_EDUCATION_TYPE', 'NAME_FAMILY_STATUS',
          'NAME_HOUSING_TYPE', 'REGION_POPULATION_RELATIVE', 'OWN_CAR_AGE', 'OCCUPATION_TYPE', 'CNT_FAM_MEMBERS',
          'REGION_RATING_CLIENT', 'REGION_RATING_CLIENT_W_CITY', 'WEEKDAY_APPR_PROCESS_START',
          'HOUR_APPR_PROCESS_START', 'ORGANIZATION_TYPE', 'WALLSMATERIAL_MODE','EMERGENCYSTATE_MODE', 'TOTALAREA_MODE']

# others  financial_info  days_duration  social_dpd  num_enq  personal_info_flags  docs_flags
# appartment_medi_cols  appartment_mode_cols  appartment_avg_cols  