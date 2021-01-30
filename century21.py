import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/", 
headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

c = r.content
soup = BeautifulSoup(c,"html.parser")
all = soup.find_all("div",{"class":"propertyRow"}) #all contains details of each property
#print(all[0].find("h4",{"class":"propPrice"}).text)
all[0].find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","") #makes previous output look good

for item in all:
    print(item.find("h4",{"class","propPrice"}).text.replace("\n","").replace(" ",""))
    print(item.find_all("span",{"class","propAddressCollapse"})[0].text)
    print(item.find_all("span",{"class","propAddressCollapse"})[1].text) #address is in two lines
    try:
        print(item.find("span",{"class","infoBed"}).find("b").text)  #.text cannot be applied to None values;so passes
    except:
        print(None)
    
    try:
         print(item.find("span",{"class","infoSqFt"}).find("b").text)
    except:
        print(None)
    
    try:
         print(item.find("span",{"class","infoValueFullBath"}).find("b").text)
    except:
        print(None)

    try:
         print(item.find("span",{"class","infoValueHalfBath"}).find("b").text)
    except:
        print(None)

    #loop for finding loop size which all props dont have
    for column_group in item.find_all("div",{"class":"columnGroup"}):
        #print(column_group)
        for feature_group,feature_name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all("span",{"class":"featureName"})):
            #print(feature_group.text,feature_name.text)
            if "Lot Size" in feature_group.text:
                print(feature_name.text)
    
    
    print(" ")


