from bs4 import BeautifulSoup
from urllib2 import urlopen

TABLE_URL = "http://www.premierleague.com/en-gb/matchday/league-table.html"
GAMES_IN_SEASON = 38
POINTS_PER_WIN = 3
TABLE_INDEXES = {'points': -1, 'games_played': 5}


class Soup(object):
    
    def __init__(self, url):
        html = urlopen(url).read()
        self.page = BeautifulSoup(html, "lxml")


class Team(object):

    def __init__(self, name, soup_object):
        tag = 'td'
        self.name = name
        self.games_played = self.get_team_games_played(soup_object, tag, name)
        self.team_points = self.get_team_points(soup_object, tag, name)
        self.available_points = self.get_available_points(self.games_played)


    def get_available_points(self, games_played):
        return (GAMES_IN_SEASON - games_played) * POINTS_PER_WIN


    def get_team_points(self, soup_object, tag, team):
        team_data = self.get_team_data(soup_object, tag, team)
        return self.soup_to_int(team_data, TABLE_INDEXES['points'])


    def get_team_games_played(self, soup_object, tag, team):
        team_data = self.get_team_data(soup_object, tag, team)
        return self.soup_to_int(team_data, TABLE_INDEXES['games_played'])

    def get_team_data(self, soup_object, tag, team):
        team = soup_object.find(tag, text=team)
        return team.parent()

    def soup_to_int(self, result_set, index):
        return int(result_set[index].get_text())

#some runner code to further evaluate

football_data = Soup(TABLE_URL)

arsenal = Team("Arsenal", football_data.page )
spurs = Team("Tottenham Hotspur", football_data.page)




print arsenal.team_points
print spurs.team_points