import pandas as pd

pf = pd.read_csv("file.csv")
print(pf.head(3))
# print(pf.tail(2))
# print(pf)

pf = pd.read_json("hello.json")
# print(pf)


pf = pd.read_csv('text.txt', sep='\t')
# print(pf.head(3))

pf = pd.read_excel("Excle.xlsx")
# print(pf)
