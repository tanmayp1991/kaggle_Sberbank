import pandas as pd
from os import listdir
import numpy as np

class Dataset:

    def __init__(self, path):
        # Remove trailing slash
        path = path[:-1] if path[-1] == '/' else path
        self.path=path

        for fname in listdir(path):
            if fname=='test.csv':
                test_df=pd.read_csv(path+'/test.csv')
            elif fname=='train.csv':
                train_df=pd.read_csv(path+'/train.csv')
            else:
                continue

        self.Y_train=train_df.loc[:,['price_doc']]
        self.X_train = train_df.drop(['price_doc'], axis=1)

        self.X_test = test_df