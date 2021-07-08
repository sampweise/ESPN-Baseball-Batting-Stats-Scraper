import pandas as pd
import requests
from bs4 import BeautifulSoup
from src.team_names import Team_Names

class Scraper():
    def __init__(self, name):
        if(Team_Names.check_names(name)):     
            self.url = 'https://www.espn.com/mlb/team/stats/_/name' + Team_Names.Teams[name]
            self.page = requests.get(self.url)
            self.parsed = BeautifulSoup(self.page.text, 'html.parser')
            self.ids = [*range(0,15)]
            self.players_data=[]
            self.header_name=[]
            #Narrows the search since similar class names on the websites
            self.narrow = self.parsed.find('div', attrs = {'class' : 'Table__ScrollerWrapper relative overflow-hidden'})
            self.names_list=[]
        else:
            print('Sorry the name you entered could not be found!')

    def scrape_columns(self):
        row = self.narrow.find('thead', attrs= {'class' : 'Table__header-group Table__THEAD'})
        for name in row.find_all('th'):
            self.header_name.append(name.get_text())

    def scrape_names(self):
        name_body = self.parsed.find('tbody', attrs={'class' : 'Table__TBODY'})
        for i in self.ids:
            row = name_body.find('tr', attrs={'data-idx' : self.ids[i]})
            for names in row.find_all('td'):
                self.names_list.append(names.find('span').get_text())

    def scrape_data(self):
        #Grabbing the class the data is in and extracting the text (stats) 
        #Then storing it into an 2D list where each i index is another player
        for i in self.ids:
            temp_players=[]
            row = self.narrow.find('tr', attrs={'data-idx' : self.ids[i]})
            for data in row.find_all('td'):
                 temp_players.append(data.get_text())
            self.players_data.append(temp_players)

    def create_df(self):
        self.scrape_columns()
        self.scrape_names()
        self.scrape_data()
        self.data_frame = pd.DataFrame(columns=self.header_name)
        temp_df = pd.DataFrame(self.players_data)
        temp_df.columns = self.header_name
        self.data_frame = pd.concat([self.data_frame,temp_df])
        self.data_frame.insert(loc=0, column='Players', value=self.names_list)

