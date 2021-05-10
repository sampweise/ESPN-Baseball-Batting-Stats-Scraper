# ESPN-Baseball-Stats-Scraper
A baseball stats web scraper that takes ESPN's updated team batting stats and puts it into a data frame

# How to Use:

### Creating the object
When calling the Scraper object it takes a string that is a key used for a team name

Example:
royals_df = Scraper('KC')

### Keys for creating object
Kansas City Royals = 'KC'
Chicago White Sox = 'CHW'
Cleveland Indians = 'CLE'
Detroit Tigers = 'DET'
Minnesota Twins = 'MIN'

### Methods

#### Creating Data Frame

Using the royals example above, this will create a dataframe for the specific team you used as your key

##### royal_df.create_df

#### Accesssing the Data Frame

Using the royals example above, to access the data frame you use

##### royal_df.data_frame

# Progress
So far I have only made a scraper for the AL Central, I am working on applying it to other MLB teams
