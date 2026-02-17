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
    "MATH": {"dataset": "gsm8k", "subset": "main", "field": "question"},
    "CODING": {"dataset": "sahil2801/CodeAlpaca-20k", "subset": None, "field": "instruction"},
    "LEGAL": {"dataset": "lex_glue", "subset": "case_hold", "field": "context"},
    "WRITING": {"dataset": "aeslc", "subset": None, "field": "email_body"},
    "KNOWLEDGE": {"dataset": "trivia_qa", "subset": "unfiltered", "field": "question"},
    "DATA_ANALYSIS": {"dataset": "Clinton/Text-to-sql-v1", "subset": None, "field": "instruction"},
    "TRANSLATION": {"dataset": "opus_books", "subset": "en-es", "field": "translation"},
    "SUMMARIZATION": {"dataset": "cnn_dailymail", "subset": "3.0.0", "field": "article"},
}

q_list = []

for category, config in datasets_config.items():
    ds = load_dataset(config["dataset"], config.get("subset"))
    for i in range(200):
        row = ds["train"][i]
        q_list.append({"category": category, "text": row[config["field"]]})


df = pd.DataFrame(q_list)

df.to_csv("file.csv")


# ds = load_dataset("sahil2801/CodeAlpaca-20k")

# print(ds["train"][0])
