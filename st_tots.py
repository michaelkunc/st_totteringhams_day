from bs4 import BeautifulSoup
from urllib2 import urlopen

TABLE_URL = "http://www.premierleague.com/en-gb/matchday/league-table.html"
TABLE_INDEXES = {'points': -1, 'games_played': 5}


class Soup(object):
    
    def __init__(self, url):
        html = urlopen(url).read()
        self.page = BeautifulSoup(html, "lxml")


class Team(object):

    GAMES_IN_SEASON = 38
    POINTS_PER_WIN = 3    

    def __init__(self, name, soup_object):
        tag = 'td'
        self.name = name
        self.games_played = self.get_team_games_played(soup_object, tag, name)
        # I think I need to remove points from an attribute and make it a function
        self.points = self.get_team_points(soup_object, tag, name)
        self.available_points = self.get_available_points(self.games_played)


    def get_available_points(self, games_played):
        return (Team.GAMES_IN_SEASON - games_played) * Team.POINTS_PER_WIN


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


print arsenal.games_played
print spurs.games_played

print "-------------------------------------"

def check_for_st_tots(arsenal, spurs):
    if (arsenal.points - spurs.points) > spurs.available_points:
        print "St Tots"
    else:
        arsenal.games_played += 1
        spurs.games_played += 1

while arsenal.games_played < 38 and spurs.games_played < 38:
    check_for_st_tots(arsenal, spurs)

print arsenal.games_played
print spurs.games_played



