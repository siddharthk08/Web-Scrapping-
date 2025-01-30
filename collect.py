from bs4 import BeautifulSoup
import os
import pandas as pd
d={'title':[1,2],'price':[3,4],'link':[1,2]}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc=f.read()
        soup=BeautifulSoup(html_doc,'html.parser')
        #print(soup.prettify())
        t=soup.find("h2")
        title=t.get_text()

        l=t.find("a")
        link="www.amazon.in"+l['href']

        p=soup.find("span",attrs={"class":'a-price-whole'})
        price=p.get_text()
        print(title,price)
        d['title'].append(title)
        d['price'].append(price)    
        d['link'].append(link)
    except Exception as e:
        print(e)
df=pd.DataFrame(data=d)
df.to_csv("data.csv")