from datasets import load_dataset
import pandas as pd

"""
structure and how i see it: 

we load all the datasets and put the variable names as a category

include only fields that we need for embedding 

and then save it as a csv with pandas
"""

math = load_dataset("gsm8k", "main") 
# print(ds["train"][0])
# print(math["train"][0]['question'])

q_list = []

for i in range(200):
    row = math["train"][i]
    q_list.append({"category" : "MATH", "text": row["question"]})

df = pd.DataFrame(q_list)

df.to_csv("file.csv")



