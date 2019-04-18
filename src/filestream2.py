import json
import os
from __init__ import api
import requests
from tqdm import tqdm
from colorama import Fore, init


iconOK = (Fore.GREEN + '[!]')
iconNone = (Fore.YELLOW + '[!]')
init(autoreset=True)


# ===================== ************* ===============================
# ----------- using this for testing purpose -----------------------
# ===================== ************* ===============================
# info = {'attackers': '178.128.78.235\n167.99.81.228',
#           'victims': 'SOCUsers',
#           'context': 'dns bidr.trellian.com'}


def print_banner():
    banner = """
          _______
         /      /, 	;___________________;
        /      //  	; Soc-L1-Automation ;
       /______//	;-------------------;
      (______(/	            danieleperera
      """
    return banner


def get_api():
    # os platform indipendent
    APIpath = os.path.join(api, "api.json")
    with open(APIpath, "r") as f:
        contents = f.read()
        # print(contents)
        data = json.loads(contents)
        # print(data)
        return data


def progressbar_ip(ip_addresses):
    for i in tqdm(ip_addresses):
        pass

# ===================== ************* =================================
# ------- Get IP addresses information form api -----------------------
# ===================== ************* =================================


def iphub_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    data = get_api()
    api = (data['API info']['iphub']['api'])
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking IPhub for ' + colorQuery)
    if type == "domain":
        print(Fore.RED + '[x] IPhub does not check domains')  # The data to post
    elif type == "ip":
        query_ip = data['API info']['iphub']['query_ip']
        url = query_ip+query
        headers = {
                    'X-Key': api}
        response = requests.get(url, headers=headers)

        if val:
            return response.json()
        else:
            pass


def getipintel_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    data = get_api()
    email = data['API info']['getipintel']['email']
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking GetIPintel for ' + colorQuery)
    if type == "domain":
        print(Fore.RED + '[x] GetIPintel does not check domains')  # The data to post
    elif type == "ip":
        query_ip = data['API info']['getipintel']['query_ip']
        url = query_ip.format(query, email)
        response = requests.get(url)

        if val:
            return response.json()
        else:
            pass

"""
def fofa_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    data = get_api()
    email = data['API info']['fofa']['email']
    api_key = data['API info']['fofa']['api']
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking fofa for ' + colorQuery)
    b64query = base64.b64encode(query)
    print(b64query)
    if type == "domain" or type == "ip":
        query_all = data['API info']['fofa']['query_all']
        params = {
            'email': email,
            'key': api_key,
            'qbase64': b64query
        }

        response = requests.get(query_all, params=params)

        if val:
            return response.json()
        else:
            pass

"""


def threatcrowd_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    data = get_api()

    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking threatcrowd for ' + colorQuery)

    if type == "domain":
        pass
    elif type == "ip":
        query_all = data['API info']['threatcrowd']['query_ip']
        params = {
            'ip': query,
        }

        response = requests.get(query_all, params=params)

    if val:
        return response.json()
    else:
        pass


def abuseipdb_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    """
    Documentation for ip_abuseipdb.
    It gets one ip addresse at a time as a string,
    uses request to do a get request to abuseip_db,
    gets json as text.

    param
        ip: str -- This is a string variable.

    example::

    ```
     ip = '124.164.251.179'
    ```

    return
    dict -- Returns json as a dict.

    """
    data = get_api()
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking Abuseipdb for ' + colorQuery)
    if type == "domain":
        print(Fore.RED + '[x] AbuseIPdb does not check domains')  # The data to post
    elif type == "ip":
        # --- abuseipdb data ----
        api = (data['API info']['abuseipdb']['api'])
        url = (data['API info']['abuseipdb']['url'])
        request_url = url.replace("API", api)
        final_url = request_url.replace("IP", query)
        # --- Add Timeout for request ---
    else:
        pass
    try:
        info_json = requests.get(final_url, timeout=10)
        response = json.loads(info_json.text)
        if val:
            return response  # this returns only huge dict
        else:
            return  # this prints some data
    except requests.exceptions.Timeout:
        print(Fore.RED + 'Timeout error occurred for AbuseIPdb')
        return


def urlscan_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    """
    Documentation for ip_urlscan.
    It gets one ip addresse at a time as a string,
    uses request to do a get request to ip_urlscan,
    gets json as text.

    param
        ip: str -- This is a string variable.

    example::

    ```
     ip = '124.164.251.179'
    ```

    return
    dict -- Returns json as a dict.

    """
    data = get_api()
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking URLscan for ' + colorQuery)
    if type == "domain":
        query_domain = data['API info']['urlscan.io']['query_domain']
        requests_url = query_domain+query
        info_json = requests.get(requests_url)
        response = json.loads(info_json.text)        
    elif type == "ip":
        # --- urlscan.io ok----
        query_ip = data['API info']['urlscan.io']['query_ip']
        requests_url = query_ip+query
        info_json = requests.get(requests_url)
        response = json.loads(info_json.text)
    if val:
        return response
    else:
        return


def urlhause_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    """
    Documentation for ip_urlhaus.
    It gets one ip addresse at a time as a string,
    uses request to do a get request to ip_urlhaus,
    gets json as text.

    param
        ip: str -- This is a string variable.

    example::

    ```
     ip = '124.164.251.179'
    ```

    return
    dict -- Returns json as a dict.

    """
    data = get_api()
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking urlhause for ' + colorQuery)
    if type == "domain" or type == "ip":
        # --- urlhaus data ok ----
        querry_host_url = (data['API info']['urlhaus']['querry_host_url'])
        params = {"host": query}
        r = requests.post(querry_host_url, params)
        r.raise_for_status()
    elif type == "url":
        data = {"host": query}
    else:
        pass
    if val:
        return r.json()
    else:
        return


def virustotal_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    """
    Documentation for ip_urlhaus.
    It gets one ip addresse at a time as a string,
    uses request to do a get request to ip_urlhaus,
    gets json as text.

    param
        ip: str -- This is a string variable.

    example::

    ```
     ip = '124.164.251.179'
    ```

    return
    dict -- Returns json as a dict.

    """
    # --- API info ---
    data = get_api()
    api = (data['API info']['virustotal']['api'])
    # print 
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking virustotal for ' + colorQuery)
    if sha_sum is None:
        if type == "domain":
            data = {"domain": query}  # The data to post
        elif type == "ip":
            query_ip = (data['API info']['virustotal']['query_ip'])
            params = {'apikey': api, 'ip': query}
            response_ip = requests.get(query_ip, params=params)
        else:
            return

        if val:
            return response_ip.json(),response_ip.json()
        else:
            return
    else:
        print(sha_sum)
        # --- virustotal data ---
        data = get_api()
        #colorIP = (Fore.RED + ip)
        api = (data['API info']['virustotal']['api'])
        #print(iconOK + ' Checking virustotal for ' + colorIP)
        ip_address_url = (data['API info']['virustotal']['ip_address_url'])
        file_address_url = (data['API info']['virustotal']['file_url'])

        # https://developers.virustotal.com/v2.0/reference#comments-get

        params_ip = {'apikey': api, 'ip': ip}
        params_file = {'apikey': api, 'resource': sha_sum}
        response_ip = requests.get(ip_address_url, params=params_ip)
        response_file = requests.get(file_address_url, params=params_file)

        if val:
            return response_ip.json(), response_file.json()
        else:
            return
    """
        for x in context:
        params = {'apikey': api, 'resource': x}
        response = requests.get(scan_url, params=params)
        print(response.json())
    """


def domain_virustotal(domain: str, boolvalue: bool, sha_sum: list = None) -> dict:
    """
    Documentation for ip_urlhaus.
    It gets one ip addresse at a time as a string,
    uses request to do a get request to ip_urlhaus,
    gets json as text.

    param
        ip: str -- This is a string variable.

    example::

    ```
     ip = '124.164.251.179'
    ```

    return
    dict -- Returns json as a dict.

    """
    if sha_sum is None:
        # --- virustotal data ---
        data = get_api()
        #colorIP = (Fore.RED + ip)
        api = (data['API info']['virustotal']['api'])
        #print(iconOK + ' Checking virustotal for ' + colorIP)
        domain_address_url = (data['API info']['virustotal']['domain_address_url'])

        # https://developers.virustotal.com/v2.0/reference#comments-get

        params = {'apikey': api, 'domain': domain}
        response_domain = requests.get(domain_address_url, params=params)
        if boolvalue:
            return response_domain.json(), response_domain.json()
        else:
            return querry_status_virustotal_domain(response_domain.json(), domain)
    else:
        print(sha_sum)
        # --- virustotal data ---
        data = get_api()
        #colorIP = (Fore.RED + ip)
        api = (data['API info']['virustotal']['api'])
        #print(iconOK + ' Checking virustotal for ' + colorIP)
        ip_address_url = (data['API info']['virustotal']['ip_address_url'])
        domain_address_url = (data['API info']['virustotal']['domain_address_url'])

        # https://developers.virustotal.com/v2.0/reference#comments-get

        params_domain = {'apikey': api, 'domain': domain}
        params_file = {'apikey': api, 'resource': sha_sum}
        response_domain = requests.get(ip_address_url, params=params_domain)
        response_file = requests.get(domain_address_url, params=params_file)

        if boolvalue:
            return domain_address_url.json(), response_file.json()
        else:
            return querry_status_virustotal_domain(domain_address_url.json(), domain), querry_status_virustotal_file(response_file.json())
    """
        for x in context:
        params = {'apikey': api, 'resource': x}
        response = requests.get(scan_url, params=params)
        print(response.json())
    """


def shodan_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    # --- API info ---
    data = get_api()
    api_key = data['API info']['shodan']['api']
    # print 
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking Shodan for ' + colorQuery)    
    if type == "domain":
        data = {"domain": query}  # The data to post
    elif type == "ip":
        url = 'https://api.shodan.io/shodan/host/{}?key={}'.format(query, api_key)
        response = requests.get(url)
    else:
        return

    #print(response.json())

    host = response.json()
    simple_dic = {}
    try:
        for index, item in enumerate(host['data']):
            hd = (item['data'])
            simple_dic[f'Detected_{index+1}_open_port: '] = item['port']
            simple_dic[f'Detected_info_{index+1}'] = "{} {}".format(hd.splitlines()[0], hd.splitlines()[1])
        #simple_dic = {k: str.encode(v, 'utf-8', 'replace') for k,v in simple_dic.items()}
    except IndexError:
        print("Index Error")
    finally:
        if val:
            return response.json()
        else:
            return


def apility_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    # --- API info ---
    data = get_api()
    api_key = data['API info']['apility']['api']
    # print 
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking apility for ' + colorQuery)     
    if type == "domain":
        data = {"domain": query}  # The data to post
    elif type == "ip":
        get_url_ip = data['API info']['apility']['url_ip_request']
        headers = {'Accept': 'application/json', 'X-Auth-Token': api_key}
        url = get_url_ip+query
        r = requests.get(url, headers=headers)
        data_paser = r.json()
    if val:
        return r.json()
    else:
        if data_paser['fullip']['history']['score_1year'] is False:
            return None
        else:
            return data_paser['fullip']['history']['activity']


def hybrid_query(query: str, type: str, val: bool, sha_sum: list = None) -> dict:
    # --- API info ---
    data = get_api()
    api_key = data['API info']['hybrid']['api']
    # printing name
    colorQuery = (Fore.RED + query)
    print(iconNone, end='')
    print(' Checking hybrid for ' + colorQuery)  

    if type == "domain":
        data = {"domain": query}  # The data to post
    elif type == "ip":
        url = "https://www.hybrid-analysis.com/api/v2/search/terms"  # The api url
        headers = {"api-key": api_key, "user-agent": "Falcon Sandbox", "accept": "application/json"}  # The request headers
        data = {"host": query}
        resp = requests.post(url, headers=headers, data=data)
        response = json.loads(resp.text)
    else:
        pass
    if val:
        return response
    else:
        if response["count"] == 0:  # If no result was recieved
            error = "\nCould not recieve value\n"
            print(error)
            return None
        else:
            c = response["count"]
            simple_dic = {}
            if c >= 3:
                print("[+] Hybrid analysis has got {} matches\n".format(c))
                for i in range(0, 3): 
                    # Parsing the data
                    print("Match No: {}\n".format(i))
                    simple_dic['verdict'] = response["result"][i]['verdict']
                    simple_dic['av_detect'] = response["result"][i]['av_detect']
                    simple_dic['threat_score'] = response["result"][i]['threat_score']
                    simple_dic['hashed'] = response["result"][i]['sha256']
                    simple_dic['submit_name'] = response["result"][i]['submit_name']
                    simple_dic['analyzed_in'] = response["result"][i]['analysis_start_time']
                    msg = "Verdit: {}\nAV_Detection: {}\nThreat_Score: {}\nSHA256_HASH: {}\nSubmit_Name: {}\nAnalyzed_in: {}\n".format(
                        simple_dic['verdict'], simple_dic['av_detect'], simple_dic['threat_score'], simple_dic['hashed'], simple_dic['submit_name'], simple_dic['analyzed_in'])
                    print(msg)
            else:
                print("[+] Hybrid analysis has got {} matches\n".format(c))
                for i in range(0, 1):
                    # Parsing the data
                    print("Match No: {}\n".format(i))
                    simple_dic['verdict'] = response["result"][i]['verdict']
                    simple_dic['av_detect'] = response["result"][i]['av_detect']
                    simple_dic['threat_score'] = response["result"][i]['threat_score']
                    simple_dic['hashed'] = response["result"][i]['sha256']
                    simple_dic['submit_name'] = response["result"][i]['submit_name']
                    simple_dic['analyzed_in'] = response["result"][i]['analysis_start_time']
                    msg = "Verdit: {}\nAV_Detection: {}\nThreat_Score: {}\nSHA256_HASH: {}\nSubmit_Name: {}\nAnalyzed_in: {}\n".format(
                        simple_dic['verdict'], simple_dic['av_detect'], simple_dic['threat_score'], simple_dic['hashed'], simple_dic['submit_name'], simple_dic['analyzed_in'])
                    print(msg)
            return simple_dic

# ===================== ************* ===============================
# -----------Working and testing from here on -----------------------
# ===================== ************* ===============================
#http://check.getipintel.net/check.php?ip=66.228.119.72&contact=mr.px0r@gmail.com&format=json

ip = '188.40.75.132'

print(virustotal_query(ip, 'ip', True))
print(iphub_query(ip, 'ip', True))
print(getipintel_query(ip, 'ip', True))
print(shodan_query(ip, 'ip', True))
#print(fofa_query(ip, 'ip', True))
print(threatcrowd_query(ip, 'ip', True))
print(hybrid_query(ip, 'ip', True))
print(apility_query(ip, 'ip', True))
print(abuseipdb_query(ip, 'ip', True))
print(urlscan_query(ip, 'ip', True))
print(urlhause_query(ip, 'domain', True))