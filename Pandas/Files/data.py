import pandas as pd

data = {
    "Name" : ["aisha", "zara", "daniya"],
    "Age" : [23, 24, 25],
    "City" : ["Karachi", "Lahore", "Islamabad"],
    "Education": ["BSCS", "BBA", "BSC"]
}

pf = pd.DataFrame(data)
print(pf)

# pd.to_csv("output.csv", index=False)
# pf.to_excel("excle.xlsx")
