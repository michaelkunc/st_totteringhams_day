from bs4 import BeautifulSoup
from urllib2 import urlopen

TABLE_URL = "http://www.premierleague.com/en-gb/matchday/league-table.html"
GAMES_IN_SEASON = 38
POINTS_PER_WIN = 3
TABLE_INDEXES = {'points': -1, 'games_played': 5}


def compare_difference_available(point_difference, available_points):
    return point_difference > available_points


def points_difference(arsenal_pts, spurs_pts):
    return arsenal_pts - spurs_pts


def get_available_points(games_played):
    return (GAMES_IN_SEASON - games_played) * POINTS_PER_WIN


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


def get_team_name(url, tag, team):
    soup = make_soup(url)
    return soup.find(tag, text=team)


def get_team_data(url, tag, team):
    team = get_team_name(url, tag, team)
    return team.parent()


def get_team_games_played(url, tag, team):
    team_data = get_team_data(url, tag, team)
    return soup_to_int(team_data, TABLE_INDEXES['games_played'])


def get_team_points(url, tag, team):
    team_data = get_team_data(url, tag, team)
    return soup_to_int(team_data, TABLE_INDEXES['points'])


def soup_to_int(result_set, index):
    return int(result_set[index].get_text())
