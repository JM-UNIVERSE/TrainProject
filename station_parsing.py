import re
import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

def parsePage(page):
    results = []
    page = requests.get("http://www.kric.go.kr/jsp/board/portal/sub05/est/estationList.jsp?pageNo={}".format(page))
    parser = bs(page.text, "html.parser")
    p_results = parser.select('table.bd_tbl.bd_tbl_ul>tbody>tr')
    for p_result in p_results:
        station = p_result.select('td.bd_railway_station>a')[0]
        result = (
            station.text,
            station.attrs['href'][22:31],
            p_result.select('td.bd_railway_line')[0].text.split(','),
            p_result.select('td.bd_railway_add')[0].text
        )
        results.append(result)
    return results
max_page = 22

results = []
for page in range(max_page + 1):
    time.sleep(0.6)
    for result in parsePage(page):
        results.append(result)
    print('Page {} parsing complete.'.format(page))

df = pd.DataFrame(results, columns=['stationName', 'stationCode', 'stationLines', 'stationAddress'])
with open('./data/station_data.json', 'w', encoding='utf-8') as file:
    df.to_json(file, orient='records', force_ascii=False)