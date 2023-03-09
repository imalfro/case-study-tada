import json
import pandas as pd

fields=["id","createdAt","updatedAt","confirmedAt","name","phone","gender","birthday","active","city","occupation"]
df = pd.read_csv('./files/member_registration.csv', header=None)
df.columns = fields
result = df.to_json(orient="records",lines=True)

with open("./files/member_registration.json", "w") as outfile:
    outfile.write(result)