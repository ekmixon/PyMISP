#!/usr/bin/env python

import requests
import json

# Suppress those "Unverified HTTPS request is being made"
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from keys import misp_url, misp_key, misp_verifycert
proxies = {

}

'''
Checks if the connection to a sync server works
returns json object
'''

def check_connection(connection_number):

    misp_headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': misp_key}
    req = requests.get(
        misp_url + f'servers/testConnection/{connection_number}',
        verify=misp_verifycert,
        headers=misp_headers,
        proxies=proxies,
    )


    return json.loads(req.text)


if __name__ == "__main__":

    result = check_connection(1)
    print(result)
