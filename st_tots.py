from bs4 import BeautifulSoup
from urllib2 import urlopen


TABLE_URL = "http://www.premierleague.com/en-gb/matchday/league-table.html"
TABLE_INDEXES = {'points': -1, 'games_played': 5}
MATCHDAY_URL = 'http://www.bbc.com/sport/football/teams/arsenal/fixtures'


class Soup(object):
#need to put some error handling here
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


class Matchdays(object):

    def __init__(self, soup_object):
        self.matches = [e.text.strip() for e in soup_object.page.findAll('td', class_='match-date')]


class Messages(object):
    st_tots = 'The earliest matchday for St Tots is '
    end_of_season = "it's the end of the season"

    @classmethod
    def st_tots_message(cls):
        return cls.st_tots

    @classmethod
    def end_of_season_message(cls):
        return cls.end_of_season

    @classmethod
    def list_element_to_string(self, element):
        return str(element)


def st_tots(arsenal, spurs):
    if (arsenal.points - spurs.points) > spurs.available_points(spurs.games_played):
        return True


def end_of_season(arsenal, spurs):
    if arsenal.games_played == 38 and spurs.games_played == 38:
        return True


def simulate_remaining_season(arsenal, spurs, match):
    if st_tots(arsenal, spurs) == True:
        return Messages.st_tots_message()  + Messages.list_element_to_string(match.matches[0])
    elif end_of_season(arsenal, spurs) == True:
        message = Messages.end_of_season_message()
        return message
    else:
        arsenal.points += 3
        arsenal.games_played += 1
        spurs.games_played += 1
        match.matches.pop(0)
        return simulate_remaining_season(arsenal, spurs, match)


