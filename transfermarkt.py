'''
Created on Apr 25, 2016
collect player profile data
from transfermarkt
http://www.transfermarkt.com/
@author: sourunsheng
'''

import pandas as pd
from bs4 import BeautifulSoup
import bs4 
import requests
import os

class player_data_collect:
    def __init__(self):
        pass
    
    
    def get_player_profile(self, print_out = True):
        '''
        get the player's profile of who played in La Liga last year and transfered to other club
        Only interested in top value players
        '''
        
        url = 'http://www.transfermarkt.com/transfers/letztetransfers/statistik/plus/0?land_id=157'

        s = requests.Session()
        s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/34.0.1847.116 Chrome/34.0.1847.116 Safari/537.36'
        s.headers['Host'] = 'www.transfermarkt.com'

        if print_out:
            print('Getting home/away data from %s ...' % url)

        try:
            r = s.get(url, timeout=10)
            r.raise_for_status()

        except requests.exceptions.ReadTimeout:
            print('\nServer not available. Skipped %s\n' % url)
            return

        soup = BeautifulSoup(r.text, 'html5lib')
        print soup

if __name__ == '__main__':
    
    player_data = player_data_collect()
    player_data.get_player_profile()
