import pandas as pd
from phpserialize import unserialize
from phpserialize import phpobject


d = []
dd ='a:2:{i:0;s:12:"Sample array";i:1;a:2:{i:0;s:5:"Apple";i:1;s:6:"Orange";}}'
d.append(dd)

# creating  dataframe of 'dd' (the PHP array string)...
df = pd.DataFrame(d, columns=['data'])

# function to unserialize the string...
def php_serialized_to_dict(serialized):

    dict_bytes = unserialize(bytes(serialized, 'utf-8'), object_hook=phpobject)

    dict_regular = {
        key.decode(): val.decode() if isinstance(val, bytes) else val
        for key, val in dict_bytes.items()
    }

    return dict_regular

# calling function...
data = php_serialized_to_dict(df.data[0])

df['data_unserialized'] = df.apply(lambda x: php_serialized_to_dict(x.data), axis=1)

df_unserialized = pd.json_normalize(df['data_unserialized'])
creating dataframe of unserialized...
ddd = pd.DataFrame(df_unserialized)
print(ddd)
# save as CSV file 
ddd.to_csv('unserialized1.csv', index=False)
