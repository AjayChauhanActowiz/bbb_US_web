from curl_cffi import requests
# import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import time


cookies = {
    # 'iabbb_user_culture': 'en-us',
    # 'iabbb_user_location': 'Cordelia_CA_USA',
    # 'iabbb_user_bbb': '1116',
    # 'iabbb_user_postalcode': '94534',
    # 'iabbb_session_id': '30cfa5cb-e655-43af-9e5f-808914982b1e',
    # 'iabbb_cookies_policy': '%7B%22necessary%22%3Atrue%2C%22functional%22%3Atrue%2C%22performance%22%3Atrue%2C%22marketing%22%3Atrue%7D',
    # '_gcl_au': '1.1.1429673232.1757485539',
    # '_evga_f108': '{%22uuid%22:%22f04913f30711dc51%22}',
    # '_sfid_03fc': '{%22anonymousId%22:%22f04913f30711dc51%22%2C%22consents%22:[]}',
    # 'AMCVS_CB586B8557EA40917F000101%40AdobeOrg': '1',
    # '_ga': 'GA1.1.1398292394.1757485541',
    # '_fbp': 'fb.1.1757485540985.550974426887528812',
    # 's_cc': 'true',
    # 'AMCV_CB586B8557EA40917F000101%40AdobeOrg': '179643557%7CMCIDTS%7C20342%7CMCMID%7C18633051938964806784423461831761568775%7CMCAAMLH-1758090340%7C12%7CMCAAMB-1758090340%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1757492741s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
    # 'iabbb_find_location': 'New%20York_NY_USA',
    # '_ga_MJQ72F5ZG5': 'GS2.1.s1757485540$o1$g1$t1757485592$j8$l0$h0',
    # 'iabbb_accredited_toggle_state': 'seen',
    # '__cf_bm': 'QXh5Ul7DHwZtInWXSGuFPLFutKo1G2kgQYsErqPI324-1757486744-1.0.1.1-nb22A3dmI_zd_1GT6ZtAR3LjB3rFIeoyTBgOQx1ioaqrYj8Zp3F_EjYx_exobQCFdjKeKFrDnGnZNCldNR87GC4i9qg32QK6BGyJf2aM6GQ',
    # '__gads': 'ID=aba8129dc3792fdd:T=1757485539:RT=1757486746:S=ALNI_MYwHnx024pXUxWKro-uHR3vk4Jy2A',
    # '__gpi': 'UID=0000119420542893:T=1757485539:RT=1757486746:S=ALNI_MbWhCZatmCjRtpVffFTfzdZvfFwuQ',
    # '__eoi': 'ID=84e7d599cc8f9dd9:T=1757485539:RT=1757486746:S=AA-AfjYP0VNiR4lLODSX8uCSvQUx',
    'iabbb_accredited_search': 'true',
    # 's_sq': '%5B%5BB%5D%5D',
    # 'CF_Authorization': 'eyJraWQiOiJkZmJjOGU0NDYwMTk5ZWU3Y2E3MGJjMmRjMGU3MmM2OWM1ZDc3MDg3ZjUyZjU3ZjI3ODMwYzQ2MTEyNTVhMGEzIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoiYXBwIiwiYXVkIjoiMmNhYzEyYTJmOWY0OTI2YjdmYmY3OTJmNTA5MjA1NjA5YWMwMmIwZmQ0MWQ1ZTcyZjY0YzY5NWY3MDg2ODkzYyIsImV4cCI6MTc1NzU3MzM0NywiaXNzIjoiaHR0cHM6XC9cL2lhYmJiLmNsb3VkZmxhcmVhY2Nlc3MuY29tIiwiY29tbW9uX25hbWUiOiJhNTBlNTEzYjFjNzM0ZjFhMjJmZDJlN2ZkMjI5ZmI4NC5hY2Nlc3MiLCJpYXQiOjE3NTc0ODY5NDcsInN1YiI6IiJ9.GoaOHlZkw3TI3tb4gVzYZHzDDfHntUe_KIY8CO4xeaKKqJwKYcNUQc2hNlbGMI5fWNwD_fWBNE-bjQ5hoCObQ14hK7sVN-1nKCkr-Gajd2KWmxJ7B0Nh600Gy3Wy0TuVtIQpDGprOdM4oT_jSREgDhloRf4KfI1TCWeDaFV6JHOna697fDuSkvzLiQq9ESHRdLJUTnr2CCznpjAXhlxlbvTaabgj7VJ99uq8v3hC7sngKo7Ml9m1_gLRgDM5GMT2q1rvOymNNIPFzJ5IPFhC7e4HiQQ-LPOsv7XTgQqmMZZqKzhz__Mwk77Uj9SRPkIrEsZ8ZFMs6BpGY9SeBkr8yA',
    # '_ga_PKZXBXGJHK': 'GS2.1.s1757485592$o1$g1$t1757486949$j12$l0$h0',
    # 's_nr30': '1757486950370-New',
    # 's_ips': '232',
    # 's_tp': '4936',
    's_ppv': 'search%2520results%2520%257C%2520search%2C5%2C5%2C232%2C1%2C21',
    'gpv_PageUrl': 'https%3A%2F%2Fwww.bbb.org%2Fsearch%3Ffind_country%3DUSA%26find_entity%3D50544-000%26find_latlng%3D40.762801%252C-73.977818%26find_loc%3DNew%2520York%252C%2520NY%26find_text%3DRestaurants%26find_type%3DCategory%26page%3D1%26touched%3D1',
    # '_ga_MP6NWVNK4P': 'GS2.1.s1757485540$o1$g1$t1757486950$j10$l0$h0',
    # '_ga_QWV3Q1HBDG': 'GS2.1.s1757485594$o1$g1$t1757486950$j10$l0$h0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,gu;q=0.8',
    'baggage': 'sentry-environment=production,sentry-public_key=dc450e854f474eda9a1173e782ca24e6,sentry-trace_id=1f3cde1087b14abbafbf09b7b8f27f2d,sentry-org_id=960626,sentry-sampled=false,sentry-sample_rand=0.447932681902138,sentry-sample_rate=0.2',
    'priority': 'u=1, i',
    'referer': 'https://www.bbb.org/search?find_country=USA&find_entity=50544-000&find_latlng=40.762801%2C-73.977818&find_loc=New%20York%2C%20NY&find_text=Restaurants&find_type=Category&page=1&touched=1',
    'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '1f3cde1087b14abbafbf09b7b8f27f2d-a77a3c95f67e1299-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
    # 'cookie': 'iabbb_user_culture=en-us; iabbb_user_location=Cordelia_CA_USA; iabbb_user_bbb=1116; iabbb_user_postalcode=94534; iabbb_session_id=30cfa5cb-e655-43af-9e5f-808914982b1e; iabbb_cookies_policy=%7B%22necessary%22%3Atrue%2C%22functional%22%3Atrue%2C%22performance%22%3Atrue%2C%22marketing%22%3Atrue%7D; _gcl_au=1.1.1429673232.1757485539; _evga_f108={%22uuid%22:%22f04913f30711dc51%22}; _sfid_03fc={%22anonymousId%22:%22f04913f30711dc51%22%2C%22consents%22:[]}; AMCVS_CB586B8557EA40917F000101%40AdobeOrg=1; _ga=GA1.1.1398292394.1757485541; _fbp=fb.1.1757485540985.550974426887528812; s_cc=true; AMCV_CB586B8557EA40917F000101%40AdobeOrg=179643557%7CMCIDTS%7C20342%7CMCMID%7C18633051938964806784423461831761568775%7CMCAAMLH-1758090340%7C12%7CMCAAMB-1758090340%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1757492741s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; iabbb_find_location=New%20York_NY_USA; _ga_MJQ72F5ZG5=GS2.1.s1757485540$o1$g1$t1757485592$j8$l0$h0; iabbb_accredited_toggle_state=seen; __cf_bm=QXh5Ul7DHwZtInWXSGuFPLFutKo1G2kgQYsErqPI324-1757486744-1.0.1.1-nb22A3dmI_zd_1GT6ZtAR3LjB3rFIeoyTBgOQx1ioaqrYj8Zp3F_EjYx_exobQCFdjKeKFrDnGnZNCldNR87GC4i9qg32QK6BGyJf2aM6GQ; __gads=ID=aba8129dc3792fdd:T=1757485539:RT=1757486746:S=ALNI_MYwHnx024pXUxWKro-uHR3vk4Jy2A; __gpi=UID=0000119420542893:T=1757485539:RT=1757486746:S=ALNI_MbWhCZatmCjRtpVffFTfzdZvfFwuQ; __eoi=ID=84e7d599cc8f9dd9:T=1757485539:RT=1757486746:S=AA-AfjYP0VNiR4lLODSX8uCSvQUx; iabbb_accredited_search=true; s_sq=%5B%5BB%5D%5D; CF_Authorization=eyJraWQiOiJkZmJjOGU0NDYwMTk5ZWU3Y2E3MGJjMmRjMGU3MmM2OWM1ZDc3MDg3ZjUyZjU3ZjI3ODMwYzQ2MTEyNTVhMGEzIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJ0eXBlIjoiYXBwIiwiYXVkIjoiMmNhYzEyYTJmOWY0OTI2YjdmYmY3OTJmNTA5MjA1NjA5YWMwMmIwZmQ0MWQ1ZTcyZjY0YzY5NWY3MDg2ODkzYyIsImV4cCI6MTc1NzU3MzM0NywiaXNzIjoiaHR0cHM6XC9cL2lhYmJiLmNsb3VkZmxhcmVhY2Nlc3MuY29tIiwiY29tbW9uX25hbWUiOiJhNTBlNTEzYjFjNzM0ZjFhMjJmZDJlN2ZkMjI5ZmI4NC5hY2Nlc3MiLCJpYXQiOjE3NTc0ODY5NDcsInN1YiI6IiJ9.GoaOHlZkw3TI3tb4gVzYZHzDDfHntUe_KIY8CO4xeaKKqJwKYcNUQc2hNlbGMI5fWNwD_fWBNE-bjQ5hoCObQ14hK7sVN-1nKCkr-Gajd2KWmxJ7B0Nh600Gy3Wy0TuVtIQpDGprOdM4oT_jSREgDhloRf4KfI1TCWeDaFV6JHOna697fDuSkvzLiQq9ESHRdLJUTnr2CCznpjAXhlxlbvTaabgj7VJ99uq8v3hC7sngKo7Ml9m1_gLRgDM5GMT2q1rvOymNNIPFzJ5IPFhC7e4HiQQ-LPOsv7XTgQqmMZZqKzhz__Mwk77Uj9SRPkIrEsZ8ZFMs6BpGY9SeBkr8yA; _ga_PKZXBXGJHK=GS2.1.s1757485592$o1$g1$t1757486949$j12$l0$h0; s_nr30=1757486950370-New; s_ips=232; s_tp=4936; s_ppv=search%2520results%2520%257C%2520search%2C5%2C5%2C232%2C1%2C21; gpv_PageUrl=https%3A%2F%2Fwww.bbb.org%2Fsearch%3Ffind_country%3DUSA%26find_entity%3D50544-000%26find_latlng%3D40.762801%252C-73.977818%26find_loc%3DNew%2520York%252C%2520NY%26find_text%3DRestaurants%26find_type%3DCategory%26page%3D1%26touched%3D1; _ga_MP6NWVNK4P=GS2.1.s1757485540$o1$g1$t1757486950$j10$l0$h0; _ga_QWV3Q1HBDG=GS2.1.s1757485594$o1$g1$t1757486950$j10$l0$h0',
}

params = {
    'find_country': 'USA',
    'find_entity': '50544-000',
    'find_latlng': '40.762801,-73.977818',
    'find_loc': 'New York, NY',
    'find_text': 'Restaurants',
    'find_type': 'Category',
    'page': '1',
    'touched': '1',
}

# import urllib3
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# token = "token"
# proxyModeUrl = "http://{}:@proxy.scrape.do:8080".format(token)
# proxies = {
#     "http": proxyModeUrl,
#     "https": proxyModeUrl,
# }
# scraper_api_token = 'token'
# proxies = {
#     "http": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001",
#     "https": f"http://scraperapi:{scraper_api_token}@proxy-server.scraperapi.com:8001"
# }
def response_check(start_iteration, num_requests):
    """Perform multiple requests inside one thread to reduce overhead."""
    batch_results = []
    for i in range(num_requests):
        iteration = start_iteration + i
        st = time.time()
        try:
            response = requests.get(
                'https://www.bbb.org/api/search',
                params=params,
                # headers=headers,
                cookies=cookies,
                impersonate='chrome120',
                # proxies=proxies,
                # verify=False,
                timeout=180
            )
            if fr'restaurants/taam-tov-restaurant-inc-0121-170777' in response.text:
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'good',
                    'time_taken': time.time()-st
                }
                batch_results.append(return_dict)
                print(return_dict)
            else:
                return_dict = {
                    'iteration': iteration,
                    'status': response.status_code,
                    'response': 'bad',
                    'time_taken': time.time() - st
                }
                batch_results.append(return_dict)
                print(return_dict)
        except Exception as e:
            return_dict = {
                'iteration': iteration,
                'status': None,
                'response': f'error: {e}',
                'time_taken': time.time() - st
            }
            batch_results.append(return_dict)
            print(return_dict)
    return batch_results

results = []
thread_count = 20
total_requests = 3000
requests_per_thread = 10  # Each worker handles 10 requests

with ThreadPoolExecutor(max_workers=thread_count) as executor:
    futures = []
    for start in range(1, total_requests + 1, requests_per_thread):
        futures.append(executor.submit(response_check, start, requests_per_thread))

    for future in as_completed(futures):
        batch = future.result()
        for result in batch:
            # print(result)
            results.append(result)

# Save results to Excel
file_name = 'bbb_US_pl_feasibility_test'
df = pd.DataFrame(results)
df.to_excel(f'{file_name}.xlsx', index=False)
print(f"Results saved to {file_name}.xlsx")



