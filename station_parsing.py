import re
import requests
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import json

def parsePage(page):
    results = []
    page = requests.get("http://www.kric.go.kr/jsp/board/portal/sub05/est/estationList.jsp?pageNo={}".format(page))
    parser = bs(page.text, "html.parser")
    p_results = parser.select('table.bd_tbl.bd_tbl_ul>tbody>tr')
    for p_result in p_results:
        station = p_result.select('td.bd_railway_station>a')[0]
        result = [
            station.text,
            station.attrs['href'][22:31],
            p_result.select('td.bd_railway_line')[0].text.split(','),
            p_result.select('td.bd_railway_add')[0].text
        ]
        results.append(result)
    return results


#kric 데이터로 카카오맵에서 경위도 조회 시 주소 오류로 안되는 경우가 있음.
#그에 따라 주소가 잘못된 역의 주소를 나무위키 기준으로 보정
addr_correction_dict = {
    '한림정역': '경상남도 김해시 한림면 한림로398번길 10',
    '대구역': '대구광역시 북구 태평로 161',
    '진주역': '경상남도 진주시 진주역로 130',
    '봉양역': '충청북도 제천시 봉양읍 주포로8길 58',
    '동백산역': '강원도 태백시 동태백로 1024',
    '북영천역': '경상북도 영천시 장수로 65',
    '전주역': '전라북도 전주시 덕진구 동부대로 680'
}

def addPosition(data):
    result = requests.get("http://dapi.kakao.com/v2/local/search/address.json", params={'query': data[3]}, headers={'Authorization': 'KakaoAK 3fd0f73d676f5f13548ce1450d26914e'})
    result_json = json.loads(result.text)
    if len(result_json['documents']) == 0:
        if data[0] in addr_correction_dict:
            data[3] = addr_correction_dict[data[0]]
            return addPosition(data)
    else:
        data.append(float(result_json['documents'][0]['x']))
        data.append(float(result_json['documents'][0]['y']))
    return data

def main():
    max_page = 22

    results = []
    for page in range(max_page + 1):
        time.sleep(0.6)
        for result in parsePage(page):
            results.append(result)
        print('Page {} parsing complete.'.format(page))
    
    position_results = [addPosition(r) for r in results]

    df = pd.DataFrame(results, columns=['stationName', 'stationCode', 'stationLines', 'stationAddress', 'stationLongitude', 'stationLatitude'])
    with open('./data/station_data.json', 'w', encoding='utf-8') as file:
        df.to_json(file, orient='records', force_ascii=False)

if __name__ == '__main__':
    main()