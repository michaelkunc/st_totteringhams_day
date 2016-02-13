from bs4 import BeautifulSoup
from urllib2 import urlopen

TABLE_URL = "http://www.premierleague.com/en-gb/matchday/league-table.html"
GAMES_IN_SEASON = 38
POINTS_PER_WIN = 3
arsenal_pts = 0
spurs_pts = 0
arsenal_games_remaining = 0
spurs_games_remaining = 0


# will retrieve current table data for Arsenal and Sp*rs
def get_table():
    return 'is this thing on?'


def compare_difference_available(point_difference, available_points):
    return point_difference > available_points


def points_difference(arsenal_pts, spurs_pts):
    return arsenal_pts - spurs_pts


def get_available_points(games_played):
    return (GAMES_IN_SEASON - games_played) * POINTS_PER_WIN


def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")

def get_points(url):
    soup = make_soup(url)