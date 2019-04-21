import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
 df = pd.read_csv("E:\\7817_1.csv")
 df.head()
 
 stopwords = set(STOPWORDS) #convert list or tuple into set

def Mywordcloud (data, title = None):
    wordcloud = WordCloud(
    background_color = 'white',
    stopwords =stopwords,
    max_words =200,
    max_font_size = 40,
    scale =3,
    random_state =1
    ).generate(str(data)) # generate applies WordCload with the data 
    
    fig = plt.figure(1, figsize =(20,20))
    plt.axis('off')
    if title:
        fig.suptitle(title,fontsize=20)
        fig.subplots_adjust(top=2.3)
    plt.imshow(wordcloud)
    plt.show()

mywordcloud =Mywordcloud(df['reviews.text'].dropna())
