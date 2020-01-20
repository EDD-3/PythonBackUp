import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')

staten_island = inventory[ inventory.location == 'Staten Island']
product_request = staten_island.product_description
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)
inventory['total_value'] = inventory.price * inventory.quantity

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)
inventory['full_description'] = inventory.apply(combine_lambda,axis=1)
print(inventory.head(10))

#inventory.rename(columns={'in_stock': 'Is Available?'},inplace=True) change the name of an existing column

#tools = inventory[inventory.product_type.isin(['garden tools', 'pest control', 'planter'])] get all rows that contain the specify values in the list passed as argument of the .isin()