import requests
from bs4 import BeautifulSoup as bs
import time
import pandas

def parsePage(page):
    results = []
    page = requests.get("http://www.kric.go.kr/jsp/board/portal/sub05/est/estationList.jsp?pageNo={}".format(page))
    parser = bs(page.text, "html.parser")
    p_results = parser.select('td.bd_railway_station>a')
    for p_result in p_results:
        result = (
            p_result.text,
            p_result.attrs['href'][22:31]
        )
        results.append(result)

max_page = 22

results = []
for page in range(max_page + 1):
    time.sleep(0.6)
    results.append(parsePage(page))
    print('Page {} parsing complete.'.format(page))

for result in results:
    