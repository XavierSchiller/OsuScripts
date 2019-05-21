import requests
from lxml import html
country = "IN"
url = "https://osu.ppy.sh/rankings/osu/performance?country=" + country

class PlayerContent:
    Scores = []
    Acc = []
    PP = []
    PC = []

X = PlayerContent()

page = requests.get(url)

tree = html.fromstring(page.content)

RawScores = tree.xpath('//span[@class="ranking-page-table__user-link-text js-usercard"]/text()')

for var in RawScores:
    X.Scores.append(var.replace('\n','').replace(' ','')) #Remove the clunk.

RawAcc = tree.xpath('//td[@class="ranking-page-table__column ranking-page-table__column--dimmed"]/text()')

for var in RawAcc:
   X.Acc.append(var.replace('\n','').replace(' ','')) #Remove the clunk.

print(X.Acc)
