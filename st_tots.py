from bs4 import BeautifulSoup
from urllib2 import urlopen
import re

TABLE_URL = "http://www.premierleague.com/en-gb/matchday/league-table.html"
TABLE_INDEXES = {'points': -1, 'games_played': 5}
MATCHDAY_URL = 'http://www.bbc.com/sport/football/teams/arsenal/fixtures'

class Soup(object):
    
    def __init__(self, url):
        html = urlopen(url).read()
        self.page = BeautifulSoup(html, 'lxml')


class Team(object):

    GAMES_IN_SEASON = 38
    POINTS_PER_WIN = 3    

    def __init__(self, name, soup_object):
        tag = 'td'
        self.name = name
        self.games_played = self.get_team_games_played(soup_object, tag, name)
        self.points = self.get_team_points(soup_object, tag, name)


    def available_points(self, games_played):
        return (Team.GAMES_IN_SEASON - games_played) * Team.POINTS_PER_WIN


    def get_team_points(self, soup_object, tag, team):
        team_data = self.get_team_data(soup_object, tag, team)
        return self.soup_to_int(team_data, TABLE_INDEXES['points'])


    def get_team_games_played(self, soup_object, tag, team):
        team_data = self.get_team_data(soup_object, tag, team)
        return self.soup_to_int(team_data, TABLE_INDEXES['games_played'])


    def get_team_data(self, soup_object, tag, team):
        team = soup_object.page.find(tag, text=team)
        return team.parent()


    def soup_to_int(self, result_set, index):
        return int(result_set[index].get_text())

#this is kinda broke
class Matchdays(object):

        def __init__(self, url):
            html = urlopen(url).read()
            page = BeautifulSoup(html, 'lxml')
            self.matches = [e.text().strip() for e in page('td', class_='match-date')]


class Messages(object):
        st_tots = 'we have achieved St tots'
        end_of_season = "it's the end of the season"
    
        @classmethod
        def st_tots_message(cls):
            return cls.st_tots

        @classmethod
        def end_of_season_message(cls):
            return cls.end_of_season



def st_tots(arsenal, spurs):
    if (arsenal.points - spurs.points) > spurs.available_points(spurs.games_played):
        return True

def end_of_season(arsenal, spurs):
    if arsenal.games_played == 38 and spurs.games_played == 38:
        return True


def simulate_remaining_season(arsenal, spurs):
    if st_tots(arsenal, spurs) == True: 
        message = Messages.st_tots_message()
        return message
    elif end_of_season(arsenal, spurs) == True:
        message = Messages.end_of_season_message()
        return message
    else: 
        arsenal.points += 3
        arsenal.games_played += 1
        spurs.games_played += 1
        return simulate_remaining_season(arsenal, spurs)


#runner code
# soup = Soup(TABLE_URL)
# arsenal = Team("Arsenal", soup)
# spurs = Team("Tottenham Hotspur", soup)    
# simulate_remaining_season(arsenal, spurs)

# match_soup = Soup(MATCHDAY_URL)

# matches = Matchdays(MATCHDAY_URL)

# print matches.matches