from curl_cffi import requests

cookies = {
    'iabbb_user_culture': 'en-us',
    'iabbb_user_location': 'Cordelia_CA_USA',
    'iabbb_user_bbb': '1116',
    'iabbb_user_postalcode': '94534',
    'iabbb_session_id': '30cfa5cb-e655-43af-9e5f-808914982b1e',
    'iabbb_cookies_policy': '%7B%22necessary%22%3Atrue%2C%22functional%22%3Atrue%2C%22performance%22%3Atrue%2C%22marketing%22%3Atrue%7D',
    '__cf_bm': 'H8uv41XFS8fStQrHC7qiLt8QpfxeOI5pTyhctXGyWA8-1757485538-1.0.1.1-5LfEdBttkAdNdUXrnrdWvK9mKXmmJ.xzTxApy2bksLgCFcpHtjQfj5aTxsWuqj4RS5i0cqGxc.srLQhLeAnQKR1xpFvDAHBrwGj._KocIsc',
    '_gcl_au': '1.1.1429673232.1757485539',
    '_evga_f108': '{%22uuid%22:%22f04913f30711dc51%22}',
    '__gads': 'ID=aba8129dc3792fdd:T=1757485539:RT=1757485539:S=ALNI_MYwHnx024pXUxWKro-uHR3vk4Jy2A',
    '__gpi': 'UID=0000119420542893:T=1757485539:RT=1757485539:S=ALNI_MbWhCZatmCjRtpVffFTfzdZvfFwuQ',
    '__eoi': 'ID=84e7d599cc8f9dd9:T=1757485539:RT=1757485539:S=AA-AfjYP0VNiR4lLODSX8uCSvQUx',
    '_sfid_03fc': '{%22anonymousId%22:%22f04913f30711dc51%22%2C%22consents%22:[]}',
    'AMCVS_CB586B8557EA40917F000101%40AdobeOrg': '1',
    '_ga': 'GA1.1.1398292394.1757485541',
    '_fbp': 'fb.1.1757485540985.550974426887528812',
    's_cc': 'true',
    'AMCV_CB586B8557EA40917F000101%40AdobeOrg': '179643557%7CMCIDTS%7C20342%7CMCMID%7C18633051938964806784423461831761568775%7CMCAAMLH-1758090340%7C12%7CMCAAMB-1758090340%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1757492741s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    'iabbb_find_location': 'New%20York_NY_USA',
    '_ga_MJQ72F5ZG5': 'GS2.1.s1757485540$o1$g1$t1757485592$j8$l0$h0',
    'iabbb_accredited_toggle_state': 'seen',
    '_ga_PKZXBXGJHK': 'GS2.1.s1757485592$o1$g1$t1757485628$j24$l0$h0',
    '_ga_MP6NWVNK4P': 'GS2.1.s1757485540$o1$g1$t1757485655$j20$l0$h0',
    's_ips': '551',
    's_tp': '2403',
    'gpv_PageUrl': 'https%3A%2F%2Fwww.bbb.org%2Fus%2Fny%2Fbrooklyn%2Fprofile%2Frestaurants%2Fvidal-cafe-2-inc-0121-87180673',
    '_ga_QWV3Q1HBDG': 'GS2.1.s1757485594$o1$g1$t1757485655$j60$l0$h0',
    'CF_Authorization': 'eyJraWQiOiJkZmJjOGU0NDYwMTk5ZWU3Y2E3MGJjMmRjMGU3MmM2OWM1ZDc3MDg3ZjUyZjU3ZjI3ODMwYzQ2MTEyNTVhMGEzIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoiYXBwIiwiYXVkIjoiY2M4MDRmN2RhN2Q2MTQ0NzFhMmYzNDBjYTkyYzU0ZWVjMWRiOTcwNTg4ZjZlNWI4MWZmYzEzYTA4YWJhNWNkZiIsImV4cCI6MTc1NzU3MjA3OCwiaXNzIjoiaHR0cHM6XC9cL2lhYmJiLmNsb3VkZmxhcmVhY2Nlc3MuY29tIiwiY29tbW9uX25hbWUiOiJhNTBlNTEzYjFjNzM0ZjFhMjJmZDJlN2ZkMjI5ZmI4NC5hY2Nlc3MiLCJpYXQiOjE3NTc0ODU2NzgsInN1YiI6IiJ9.NZA6dcKzaWrK5rG5rrx-9h77VwsM969yBuZJDbYsIjHAzFMaz-CsV7ak4xZFKd3i9RCS-2AR9BGhTTrgMfHyLuuWVYT3Je62xm_alJVF6QYQGSYX5vV9HCf3DZQAKEZ1T6DyOz93lQNEuh9g_NerZQaAAQD9BVnawQBV5rJF0qBL6N2tpLFHkExdcf1ohO9IgwcByhKeoMApDYxWc3FgvSECrR-6qhk_dLKApDSebN2c27QOF7EJLRJOcCJEhGofNlSLJvunslxon8LNxkBVpRiuqd6UHyFe6tRJbuakejCI7XlJSIZh0uyidsaLVNWgVKh3dbpq4C3II-HvkEqrGw',
    's_ppv': 'vidal%2520cafe%25202%2520inc.%2520%257C%2520bbb%2520business%2520profile%2520%257C%2520better%2520business%2520bureau%2C81%2C23%2C1951%2C3%2C5',
    's_nr30': '1757485703601-New',
    's_sq': 'cbbbproduction%3D%2526c.%2526a.%2526activitymap.%2526page%253Dvidal%252520cafe%2525202%252520inc.%252520%25257C%252520bbb%252520business%252520profile%252520%25257C%252520better%252520business%252520bureau%2526link%253DHomeNew%252520YorkBrooklynRestaurantsVidal%252520Cafe%2525202%252520Inc.%252520%252528current%252520page%252529%252520Share%252520BUSINESS%252520PROFILE%252520Restaurants%252520Vidal%252520Cafe%2525202%252520Inc.%252520BBB%252520Accredi%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dvidal%252520cafe%2525202%252520inc.%252520%25257C%252520bbb%252520business%252520profile%252520%25257C%252520better%252520business%252520bureau%2526pidt%253D1%2526oid%253DfunctionJu%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.bbb.org/us/ny/new-york/category/restaurants/accredited',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'iabbb_user_culture=en-us; iabbb_user_location=Cordelia_CA_USA; iabbb_user_bbb=1116; iabbb_user_postalcode=94534; iabbb_session_id=30cfa5cb-e655-43af-9e5f-808914982b1e; iabbb_cookies_policy=%7B%22necessary%22%3Atrue%2C%22functional%22%3Atrue%2C%22performance%22%3Atrue%2C%22marketing%22%3Atrue%7D; __cf_bm=H8uv41XFS8fStQrHC7qiLt8QpfxeOI5pTyhctXGyWA8-1757485538-1.0.1.1-5LfEdBttkAdNdUXrnrdWvK9mKXmmJ.xzTxApy2bksLgCFcpHtjQfj5aTxsWuqj4RS5i0cqGxc.srLQhLeAnQKR1xpFvDAHBrwGj._KocIsc; _gcl_au=1.1.1429673232.1757485539; _evga_f108={%22uuid%22:%22f04913f30711dc51%22}; __gads=ID=aba8129dc3792fdd:T=1757485539:RT=1757485539:S=ALNI_MYwHnx024pXUxWKro-uHR3vk4Jy2A; __gpi=UID=0000119420542893:T=1757485539:RT=1757485539:S=ALNI_MbWhCZatmCjRtpVffFTfzdZvfFwuQ; __eoi=ID=84e7d599cc8f9dd9:T=1757485539:RT=1757485539:S=AA-AfjYP0VNiR4lLODSX8uCSvQUx; _sfid_03fc={%22anonymousId%22:%22f04913f30711dc51%22%2C%22consents%22:[]}; AMCVS_CB586B8557EA40917F000101%40AdobeOrg=1; _ga=GA1.1.1398292394.1757485541; _fbp=fb.1.1757485540985.550974426887528812; s_cc=true; AMCV_CB586B8557EA40917F000101%40AdobeOrg=179643557%7CMCIDTS%7C20342%7CMCMID%7C18633051938964806784423461831761568775%7CMCAAMLH-1758090340%7C12%7CMCAAMB-1758090340%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1757492741s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; iabbb_find_location=New%20York_NY_USA; _ga_MJQ72F5ZG5=GS2.1.s1757485540$o1$g1$t1757485592$j8$l0$h0; iabbb_accredited_toggle_state=seen; _ga_PKZXBXGJHK=GS2.1.s1757485592$o1$g1$t1757485628$j24$l0$h0; _ga_MP6NWVNK4P=GS2.1.s1757485540$o1$g1$t1757485655$j20$l0$h0; s_ips=551; s_tp=2403; gpv_PageUrl=https%3A%2F%2Fwww.bbb.org%2Fus%2Fny%2Fbrooklyn%2Fprofile%2Frestaurants%2Fvidal-cafe-2-inc-0121-87180673; _ga_QWV3Q1HBDG=GS2.1.s1757485594$o1$g1$t1757485655$j60$l0$h0; CF_Authorization=eyJraWQiOiJkZmJjOGU0NDYwMTk5ZWU3Y2E3MGJjMmRjMGU3MmM2OWM1ZDc3MDg3ZjUyZjU3ZjI3ODMwYzQ2MTEyNTVhMGEzIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoiYXBwIiwiYXVkIjoiY2M4MDRmN2RhN2Q2MTQ0NzFhMmYzNDBjYTkyYzU0ZWVjMWRiOTcwNTg4ZjZlNWI4MWZmYzEzYTA4YWJhNWNkZiIsImV4cCI6MTc1NzU3MjA3OCwiaXNzIjoiaHR0cHM6XC9cL2lhYmJiLmNsb3VkZmxhcmVhY2Nlc3MuY29tIiwiY29tbW9uX25hbWUiOiJhNTBlNTEzYjFjNzM0ZjFhMjJmZDJlN2ZkMjI5ZmI4NC5hY2Nlc3MiLCJpYXQiOjE3NTc0ODU2NzgsInN1YiI6IiJ9.NZA6dcKzaWrK5rG5rrx-9h77VwsM969yBuZJDbYsIjHAzFMaz-CsV7ak4xZFKd3i9RCS-2AR9BGhTTrgMfHyLuuWVYT3Je62xm_alJVF6QYQGSYX5vV9HCf3DZQAKEZ1T6DyOz93lQNEuh9g_NerZQaAAQD9BVnawQBV5rJF0qBL6N2tpLFHkExdcf1ohO9IgwcByhKeoMApDYxWc3FgvSECrR-6qhk_dLKApDSebN2c27QOF7EJLRJOcCJEhGofNlSLJvunslxon8LNxkBVpRiuqd6UHyFe6tRJbuakejCI7XlJSIZh0uyidsaLVNWgVKh3dbpq4C3II-HvkEqrGw; s_ppv=vidal%2520cafe%25202%2520inc.%2520%257C%2520bbb%2520business%2520profile%2520%257C%2520better%2520business%2520bureau%2C81%2C23%2C1951%2C3%2C5; s_nr30=1757485703601-New; s_sq=cbbbproduction%3D%2526c.%2526a.%2526activitymap.%2526page%253Dvidal%252520cafe%2525202%252520inc.%252520%25257C%252520bbb%252520business%252520profile%252520%25257C%252520better%252520business%252520bureau%2526link%253DHomeNew%252520YorkBrooklynRestaurantsVidal%252520Cafe%2525202%252520Inc.%252520%252528current%252520page%252529%252520Share%252520BUSINESS%252520PROFILE%252520Restaurants%252520Vidal%252520Cafe%2525202%252520Inc.%252520BBB%252520Accredi%2526region%253DBODY%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dvidal%252520cafe%2525202%252520inc.%252520%25257C%252520bbb%252520business%252520profile%252520%25257C%252520better%252520business%252520bureau%2526pidt%253D1%2526oid%253DfunctionJu%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DDIV',
}
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
token = "token"
proxyModeUrl = "http://{}:@proxy.scrape.do:8080".format(token)
proxies = {
    "http": proxyModeUrl,
    "https": proxyModeUrl,
}
response = requests.get(
    'https://www.bbb.org/us/ny/brooklyn/profile/restaurants/vidal-cafe-2-inc-0121-87180673',
    # cookies=cookies,
    # headers=headers,
    impersonate='chrome120',
    proxies=proxies,
    verify=False,
    timeout=120
)
print(response.status_code)
print('Vidal Cafe 2 Inc' in response.text)

print(response.headers)
