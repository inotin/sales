import numpy as np
import pandas as pd
import random
from sklearn.metrics import mean_squared_error
from collections import defaultdict

def anonimize(dfOriginal, force = 10):
    """
    This function returns a dataframe with randomized numerical values and replaced non-numerical values.
    Input:  pandas dataframe

    Ouptut: pandas dataframe

    Example:
    dfT = pd.DataFrame({'a':[1,2,3,4],'b':['a','b','c','d'],'c':[random.random() for i in range(4)]})
    dfT

        a	b	c
    0	1	a	0.131762
    1	2	b	0.434353
    2	3	c	0.487006
    3	4	d	0.328282

    anonimize(dfT)

    	a	b			c
    0	1	b_item_1	-0.005217
    1	1	b_item_2	0.003818
    2	2	b_item_3	-0.045839
    3	4	b_item_4	-0.004548


    """
    df = dfOriginal.copy()
    flCoef = force*force*random.uniform(-force/100, force/100)
    for c in df.columns:
        if np.dtype(df[c])=='float':
            df[c]=df[c].map(lambda x: x+x*flCoef)
        elif np.dtype(df[c])=='int':
            df[c]=df[c].map(lambda x: int(x+x*random.uniform(-force/10, force/10)))
        elif 'date' not in str(df.dtypes[c]):
            dct = defaultdict()
            for i,name in enumerate(df[c].unique()):
                dct[name]=f'{c}_item_{i+1}'
            df[c]=df[c].apply(lambda x: dct[x])
    return df

def regressionReport(y_true, y_pred, cv = 10):
    print('True mean value \t:', np.mean(y_true))
    print('Predicted mean value \t:', np.mean(y_true))
    print('RMSE \t\t\t:', mean_squared_error(y_true, y_pred, squared=False))
    sigm = np.sqrt(mean_squared_error(y_true, y_pred)*len(y_true)/(len(y_true)-1))
    print('3sigma \t\t\t:', 3 * sigm)
    print('Variation coefficient \t:', sigm/np.mean(y_pred))
    print('VC (3s) \t\t:', 3*sigm/np.mean(y_pred))
