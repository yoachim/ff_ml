import urllib.request
import time
# let's scrape a year's worth of data from https://www.footballdb.com
rooturl = 'https://www.footballdb.com/fantasy-football/index.html?pos='


positions = ['WR', 'QB', 'RB', 'TE', 'K', 'DST']

weeks = range(1, 18)
year = 2017

for week in weeks:
    for pos in positions:
        time.sleep(2)
        urllib.request.urlretrieve("%s%s&yr=%i&wk=%i&rules=1" % (rooturl, pos, year, week),
                                   "fbdb_%i_%i_%s.html" % (year, week, pos))
