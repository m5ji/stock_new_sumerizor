#!pip install transformers
#!pip install torch==1.6.0+cu101 torchvision==0.7.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html

import torch
import json 
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import pandas as pd
from tqdm.notebook import tqdm
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

def getStockNewsTitleRating(article):
    # If there's a GPU available...
    if torch.cuda.is_available():
        device = torch.device("cuda")
        print('There are %d GPU(s) available.' % torch.cuda.device_count())
        print('We will use the GPU:', torch.cuda.get_device_name(0))
    else:
        print('No GPU available, using the CPU instead.')
        device = torch.device("cpu")

    def get_text_sentiment(tokenizer, model, text):
        # This is the method that returns the prediction
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs)
        loss = outputs.loss
        logits = outputs.logits
        print(np.argsort(logits.detach().numpy(), axis=1)[0][::-1])
        return np.argmax(logits.detach().numpy(), axis=1)[0]

    rate = get_text_sentiment(tokenizer, model, article['title'])
    return {
        'rate': int(rate),
        'title': article['title'],
        'url': article['url']
    }

#>>> 5

#loop through a list:
# f = open('/content/drive/MyDrive/Copy of stock_news_general_new_US_2',)
# data = json.load(f)
#
# for i in data['items']['result']:
#     article = i['article']
#     rate = get_text_sentiment(tokenizer,model,article)
#     rate_list.append(rate)
#     print(rate,article)
