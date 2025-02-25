import pandas as pd

df = pd.read_json("hello.json")
print(df.info())