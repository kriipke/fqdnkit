from domainavailability import *
import requests
import re
import pytest

wxa_api_key = 'at_88IhFPfWkyNq0hyzwy7hnBUVo0cov'

# returns a list of names (to be appended with tlds elsewhere)
def gen_nchar_names(n,charset='abcdefjhijklmnopqrstubwxyz1234567890'):
    name_list = []
    for i in charset:
        for j in charset:
            name_list.append("{}{}".format(i,j))
    return name_list

def get_tlds(source='ianna'):
    if source == 'ianna':
        tld_list_url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
        re_exclude_list = [ r'^$',r'^#']
    else:
        raise Exception

    response_raw = requests.request("GET", tld_list_url)
    response_lines = response_raw.text.lower().splitlines()

    tlds = [ d for d in response_lines for i in re_exclude_list if not re.search(i, d)]
    return tlds

def filter_tlds(tlds, re_include_list=[], re_exclude_list=[]):

    # EXAMPLE REGEX FILTERS:
    #   re_include_list = [r'^$',r';^#',r'^[xXaA]']
    #   re_exclude_list = [r'^xn-',r'^#']

    if re_exclude_list:
        tlds = [ d for d in tlds for i in re_exclude_list
                    if not re.search(i, d) ]
    if re_include_list:
        tlds = [ d for d in tlds for i in re_include_list
                    if re.search(i, d) ]
    return tlds

def fqdn_permutations(pqdns,fqdns):
    permutations = []
    for i in charset:
        for j in charset:
            permutations.append("{}.{}".format(i,j))
    return permutations

def check_fqdns(fqdns):
    client = Client(wxa_api_key)
    availability_results = {}
    for fqdn in fqdns:
        availability_results[fqdn] = client.data(fqdn).is_available()
    return availability_results

def test_function():
	tlds = filter_tlds(get_tlds(),re_include_list = [r'^$',r';^#',r'^[xXaA]'])
	assert tlds[0] == 'aaa'

def main():
    print(get_tlds())
    
if __name__ == '__main__':
    main()
