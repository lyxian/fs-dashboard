from urllib.parse import unquote
import pandas
import json 
import re

from vars import BIZ_CATEGORY, ORDERED_COLUMNS

filename = 'data/2022-01-07:23H.json'

with open(filename, 'r') as file:
    items = json.load(file)

def getCategory(nums):
    return ', '.join([BIZ_CATEGORY[num] for num in nums])

def keyInfo(data: dict) -> dict:
    keyInfo = [
        'itemTitle',
        'isHot',
        'itemSoldCnt',
        'itemTotalStock',
        'itemDiscountPrice',
        'itemPrice',
        'itemRatingScore',
        'itemReviews'
        # 'lowestPriceIn',
    ]
    return {k:v for k,v in data.items() if k in keyInfo}

def addInfo(data: dict) -> dict:
    itemDiscount = eval(f'100-100*{data["itemDiscountPrice"].replace(",","")}/{data["itemPrice"].replace(",","")}')
    trackInfo = unquote(data['trackInfo'])
    return {
        'bizCategory': getCategory(data['bizCategory']),
        'soldRatio': f'{100*data["itemSoldCnt"]/data["itemTotalStock"]:0.2f} %',
        'itemDiscount': f'{itemDiscount:.2f} %',
        'minPrice30d': re.search(r'fs_min_price_l30d:(.*?);', trackInfo).group(1) if 'fs_min_price_l30d' in trackInfo else 0
    }

def filterItemsByCategory(category: str, items: dict) -> dict:
    items = [{**keyInfo(item), **addInfo(item)} for item in items]
    if category == 'All':
        return pandas.DataFrame(items).loc[:, ORDERED_COLUMNS]
    else:
        return pandas.DataFrame([item for item in items if item['bizCategory'] == category]).loc[:, ORDERED_COLUMNS]

def formatFilename(filename: str) -> str:
    return f'@ {", ".join(re.search(r"data/(.*):(.*?).json", filename).groups())}'

def sortItemsByColumn(category: str, column: str, items: dict, orderBy: str) -> dict:
    items = [{**keyInfo(item), **addInfo(item)} for item in items]
    if category != 'All':
        items = [item for item in items if item['bizCategory'] == category]
    return pandas.DataFrame(sorted(items, key=lambda x: eval(x[column].rstrip(' %')) if column != 'itemTitle' else x[column], reverse=(orderBy!='Ascending'))).loc[:, ORDERED_COLUMNS]

# ======
def getItems():
    with open('data/2022-01-07:23H.json', 'r') as file:
        items = json.load(file)
    return [{**keyInfo(item), **addInfo(item)} for item in items]