# Tabelog Scraper

Given tabelog jp webpage list
ex. https://tabelog.com/tokyo/rstLst/7/?Srt=D&SrtT=rt&LstSmoking=0&svd=20240909&svt=1900&svps=2&LstCosT=5&RdoCosTp=2

Prints a formatted output with the name of the restaurant, url, address, genre, number of seats/ private room.

### Requirements
```
$ pip install -r requirements.txt
```

### Sample Output:
```
Tabelog URL: https://tabelog.com/tokyo/rstLst/7/?Srt=D&SrtT=rt&LstSmoking=0&svd=20240909&svt=1900&svps=2&LstCosT=5&RdoCosTp=2

神名備
https://tabelog.com/tokyo/A1311/A131105/13006070/
4-21-3 Sendagi, Bunkyo-ku, Tokyo
ramen
13 seats (9 seats at the counter, 4 seats (4 people x 1))
Private Room: Nothing
...
```