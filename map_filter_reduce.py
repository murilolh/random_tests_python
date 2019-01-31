#!/usr/bin/env python
# -*- coding: utf-8 -*-

###################################################################
# Get the dailyPrices, sum and average from a requested JSON from flipkey.com
###################################################################

import requests
import json
import re

# Function to test if x['dailyPrice'] is valid
def test_error(x):
    try:
        x['dailyPrice']
    except TypeError:
        return False
    else:
        return True

test = requests.get('https://www.flipkey.com/content/srp/srp_fk/index_json/book/destin/222604340//zoom.11?page=1')

results = json.loads(test.text) # Loads the JSON from the request above

results = list(filter(lambda x: test_error(x), results['results'])) # Filter to remove invalid data from the array

daylyPricesStr = list(map(lambda x: x['dailyPrice'], results)) # Map to get only the dailyPrices from the results array

dailyPrices = list(map(lambda x: int(re.sub(r'([^0-9]+)', '', x)), daylyPricesStr)) # Map to get the prices as an Integer, removing the $ sign

sum = reduce((lambda x, y: x + y), dailyPrices) # Reduce to get the sum of the prices

avg = sum / len(dailyPrices) # Getting the avg of the prices

print str(len(dailyPrices)) + ' price(s) analysed'
for price in dailyPrices:
    print price
print 'SUM: ' + str(sum)
print 'AVG: ' + str(avg)
