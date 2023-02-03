import pandas as pd
# from phpserialize import serialize
from phpserialize import unserialize
from phpserialize import phpobject


d = []
dd ='a:61:{s:7:"NEFT ID";s:28:"NFT-234100260GN00193XXXXXXX ";s:12:"Payment Date";s:10:"2022-12-07";s:38:"Bank Settlement Value  Rs      SUM I P";d:891.07;s:38:"Input GST   TCS Credits  Rs    GST TCS";d:39.18;s:29:"Income Tax Credits  Rs    TDS";d:2.79;s:0:"";s:13:"Not Available";s:8:"Order ID";s:20:"OD426659565414107100";s:13:"Order item ID";s:18:"426659565414107100";s:15:"Sale Amount  Rs";d:1099;s:22:"Total Offer Amount  Rs";d:0;s:12:"My share  Rs";d:0;s:27:"Customer Add-ons Amount  Rs";d:0;s:33:"Marketplace Fee  Rs     SUM  T AG";d:-165.96;s:9:"Taxes  Rs";d:-29.87;s:19:"Protection Fund  Rs";d:0;s:10:"Refund  Rs";d:0;s:4:"Tier";s:4:"gold";s:15:"Commission Rate";d:2;s:14:"Commission  Rs";d:-21.98;s:14:"Fixed Fee   Rs";d:-50;s:18:"Collection Fee  Rs";d:-21.98;s:21:"Pick And Pack Fee  Rs";d:-14;s:18:"Shipping Fee  Rs 0";d:-58;s:24:"Reverse Shipping Fee  Rs";d:0;s:32:"No Cost Emi Fee Reimbursement Rs";d:0;s:20:"Installation Fee  Rs";d:0;s:18:"Tech Visit Fee  Rs";d:0;s:34:"Uninstallation   Packaging Fee  Rs";d:0;s:36:"Customer Add-ons Amount Recovery  Rs";d:0;s:17:"Franchise Fee  Rs";d:0;s:24:"Shopsy Marketing Fee  Rs";d:0;s:28:"Product Cancellation Fee  Rs";d:0;s:7:"TCS  Rs";d:-9.31;s:7:"TDS  Rs";d:-2.79;s:18:"GST on MP Fees  Rs";d:-29.87;s:16:"Dead Weight  kgs";s:4:"0.14";s:21:"Length Breadth Height";s:15:"11.67*8.58*5.19";s:22:"Volumetric Weight  kgs";s:4:"0.10";s:24:"Chargeable Weight Source";s:22:"System measured weight";s:22:"Chargeable Weight Type";s:4:"Dead";s:27:"Chargeable Wt  Slab  In Kgs";s:7:"0.0-0.5";s:13:"Shipping Zone";s:8:"National";s:10:"Order Date";s:10:"2022-11-29";s:13:"Dispatch Date";s:10:"2022-11-29";s:10:"Order Type";s:8:"postpaid";s:15:"Fulfilment Type";s:19:"flipkart_fulfilment";s:10:"Seller SKU";s:33:"itel_it2171_Ace2Cam_Elegant Black";s:8:"Quantity";d:1;s:20:"Product Sub Category";s:6:"mobile";s:22:"Additional Information";s:2:"NA";s:11:"Return Type";s:2:"NA";s:12:"Shopsy Order";s:2:"No";s:18:"Item Return Status";s:2:"NA";s:10:"Invoice ID";s:16:"FAJI3L2300052335";s:12:"Invoice Date";s:10:"2022-11-29";s:11:"Sale Amount";d:1099;s:18:"Total Offer Amount";d:0;s:8:"My Share";d:0;s:2:"ID";s:1:"0";s:33:"Marketplace Fee  Rs     SUM  T AK";d:-165.96;s:16:"Shipping Fee  Rs";d:-58;}'
d.append(dd)
df = pd.DataFrame(d, columns=['data'])
# print(df)
# df.to_csv(r'C:\Users\evanik\OneDrive\Desktop\Deepak_Raut\extra\php_data.csv', index=False)

# df = pd.read_csv(r'C:\Users\evanik\OneDrive\Desktop\Deepak_Raut\extra\php_data.csv')
# df = df[['data']]
# print(df.head(3))


def php_serialized_to_dict(serialized):

    dict_bytes = unserialize(bytes(serialized, 'utf-8'), object_hook=phpobject)

    dict_regular = {
        key.decode(): val.decode() if isinstance(val, bytes) else val
        for key, val in dict_bytes.items()
    }

    return dict_regular


data = php_serialized_to_dict(df.data[0])
# print(data)

df['data_unserialized'] = df.apply(lambda x: php_serialized_to_dict(x.data), axis=1)
# print(df.head())

df_unserialized = pd.json_normalize(df['data_unserialized'])
# print(df_unserialized.head())
# print(df_unserialized)
ddd = pd.DataFrame(df_unserialized)
print(ddd)
# ddd.to_csv('unserialized1.csv', index=False)
