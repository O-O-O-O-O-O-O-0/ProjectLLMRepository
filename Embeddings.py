import requests
import pandas as pd
import torch
from datasets import load_dataset
from sentence_transformers.util import semantic_search

model_id = "sentence-transformers/all-MiniLM-L6-v2"
hf_token = "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"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}

def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()
with open('Output.txt') as f:
    texts = f.read().splitlines()

output = query(texts)
embeddings = pd.DataFrame(output)
embeddings.to_csv("vectorEmbeddings.csv", index=False)
faqs_embeddings = load_dataset('ProjectL/vectorEmbeddings')
'''faqs_embeddings = load_dataset('/Users/sriharithirumaligai/Downloads/project1-main/vectorEmbeddingsTwo.csv')'''
dataset_embeddings = torch.from_numpy(faqs_embeddings["train"].to_pandas().to_numpy()).to(torch.float)

question = ["picture day"]
output = query(question)

query_embeddings = torch.FloatTensor(output)

hits = semantic_search(query_embeddings, dataset_embeddings, top_k=5)
print(hits)
print([texts[hits[0][i]['corpus_id']] for i in range(len(hits[0]))])