from bs4 import BeautifulSoup
import nltk
import urllib3.request
import requests as request

response= request.get('http://www.cervantesvirtual.com/obra-visor/la-influencia-de-las-emociones-en-el-sonido-de-la-voz/html')

soup= BeautifulSoup(response.text,'html.parser')
text=soup.get_text(strip=True)
#print(text)
from nltk.tokenize import word_tokenize
tokens= word_tokenize(text,"spanish")
tokens=[word.lower() for word in tokens if word.isalpha()]
#print(tokens)

freq =nltk.FreqDist(tokens)
for key,val in freq.items():
    print(str(key) + ":" + str(val) )

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
freq.plot(50,cumulative=False)
#plt.savefig("image.png")
