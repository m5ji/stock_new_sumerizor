import torch
import json 
from matplotlib import pyplot as plt
import pandas as pd
from tqdm.notebook import tqdm
import numpy as np


from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)
  
  
labels = ['negative', 'neutral', 'positive']
#label mapping form ['negative', 'neutral', 'positive'] to ['negative','week negative', 'neutral', 'week positive, 'positive']
label_mapping = {0:0,
                 1:2,
                 2:4}
                 
tokenizer = AutoTokenizer.from_pretrained("finiteautomata/bertweet-base-sentiment-analysis")
model = AutoModelForSequenceClassification.from_pretrained("finiteautomata/bertweet-base-sentiment-analysis")

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
        
        text = preprocess(text)
        inputs = tokenizer(text, return_tensors='pt')
        
        outputs = model(**inputs)

        scores = output[0][0].detach().numpy()
        scores = softmax(scores)

        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        
        l = ranking[i]
        l = label_mapping[l]

        print(l)
        return l

    rate = get_text_sentiment(tokenizer, model, article['title'])
    return {
        'rate': rate,
        'title': article['title']
    }

  