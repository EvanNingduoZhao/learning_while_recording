import pandas as pd
import numpy as np
import featuretools as ft
import warnings

warnings.filterwarnings('ignore')

clients = pd.read_csv('/Users/apple/PycharmProjects/qtm385/pandas_learning/clients.csv', parse_dates=['joined'])
loans = pd.read_csv('/Users/apple/PycharmProjects/qtm385/pandas_learning/loans.csv',
                    parse_dates=['loan_start', 'loan_end'])
payments = pd.read_csv('/Users/apple/PycharmProjects/qtm385/pandas_learning/payments.csv', parse_dates=['payment_date'])

clients['join_month'] = clients['joined'].dt.month
clients['log_income'] = np.log(clients['income'])

# print(clients.head())

# print(loans)
stats = loans.groupby('client_id').loan_amount.agg(['mean', 'min', 'max'])

clients.merge(stats, left_on='client_id', right_index=True, how='left').head(10)
print(clients)
