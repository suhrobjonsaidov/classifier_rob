from datasets import load_dataset
import pandas as pd

"""
structure and how i see it: 

we load all the datasets and put the variable names as a category

include only fields that we need for embedding 

and then save it as a csv with pandas
"""

# data loading from hggf
datasets_config = {
    "WRITING": {"dataset": "aeslc", "field": "email_body"},
    "MATH": {"dataset": "gsm8k", "field": "question"},
    "KNOWLEDGE": {"dataset": "trivia_qa", "field": "question"},
    "DATA_ANALYSIS": {"dataset": "datadrivenscience/datasets-for-analysis", "field": "Description"},
    "TRANSLATION": {"dataset": "opus_books", "field": "translation"},
    "CODING": {"dataset": "codeparrot/apps", "field": "question"},
    "LEGAL": {"dataset": "lex_glue", "field": "context"},
    "SUMMARIZATION": {"dataset": "cnn_dailymail", "field": "article"}
}

q_list = []

for category, config in datasets_config.items():
    for i in range(200):
        row = config["dataset"]["train"][i]
        q_list.append({"category": category, "text": row[config["field"]]})


df = pd.DataFrame(q_list)

df.to_csv("file.csv")



