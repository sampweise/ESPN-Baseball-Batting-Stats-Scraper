# ESPN-Baseball-Stats-Scraper
A baseball stats web scraper that takes ESPN's updated team batting stats and puts it into a data frame


# How to Use:



### Creating the object:
When calling the Scraper object it takes a string that is a key used for a team name

Example:
royals_df = Scraper('KC')



### Keys for creating object:
Kansas City Royals = 'KC' <br/>
Chicago White Sox = 'CHW' <br/>
Cleveland Indians = 'CLE' <br/>
Detroit Tigers = 'DET' <br/>
Minnesota Twins = 'MIN' <br/>
Baltimore Orioles = 'BAL' <br/>
Boston Red Sox = 'BOS' <br/>
New York Yankees = 'NYY' <br/>
Tampa Bay Rays = 'TB' <br/>
Toronto Blue Jays = 'TOR' <br/>
Houton Astros = 'HOU' <br/>
Los Angeles = 'LAA',
Oakland Athletics = 'OAK' <br/>
Seattle Mariners = 'SEA' <br/>
Texas Rangers = 'TEX' <br/>
Atlanta Braves = 'ATL' <br/>
Miami Marlins = 'MIA' <br/>
New York Mets = 'NYM' <br/>
Philadelphia Phillies = 'PHI' <br/>
Washington Nationals = 'WSH' <br/>
Chicago Cubs = 'CHC' <br/>
Cincinatti Reds = 'CIN' <br/>
Milwaukee Brewers = 'MIL' <br/>
Pittsburgh Pirates = 'PIT' <br/>
St. Louis Cardinals = 'STL' <br/>
Arizona Diamondbacks = 'ARI' <br/>
Colorado Rockies = 'COL' <br/>
Los Angeles Dodgers = 'LAD' <br/>
San Diego Padres = 'SD' <br/>
San Franciso Giants = 'SF' <br/>



### Methods:

#### Creating Data Frame:

Using the royals example above, this will create a dataframe for the specific team you used as your key

##### royal_df.create_df

#### Accesssing the Data Frame:

Using the royals example above, to access the data frame you use

##### royal_df.data_frame



# Progress:
So far I have only made a scraper for the AL Central, I am working on applying it to other MLB teams
