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


data = [{**keyInfo(item), **addInfo(item)} for item in items]

df = pandas.DataFrame(data).loc[:, ORDERED_COLUMNS]
