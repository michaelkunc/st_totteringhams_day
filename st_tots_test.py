import unittest
import st_tots

class ST_TOTSTESTS(unittest.TestCase):
	@classmethod
	def setUpClass(ST_TOTSTESTS):
		ST_TOTSTESTS.url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'
		ST_TOTSTESTS.tag = 'td'
		ST_TOTSTESTS.team = 'Arsenal'
		ST_TOTSTESTS.points_per_win = 3
		ST_TOTSTESTS.games_per_season = 38
		ST_TOTSTESTS.max_points = ST_TOTSTESTS.games_per_season * ST_TOTSTESTS.points_per_win
		ST_TOTSTESTS.min_points = 0
		ST_TOTSTESTS.soup = st_tots.make_soup(ST_TOTSTESTS.url)


	def test_compare_difference_available(self):
		point_difference = 6
		available_pts = 30
		result = st_tots.compare_difference_available(point_difference, available_pts)
		self.assertFalse(result)


	def test_points_difference(self):
		arsenal_pts = 58
		spurs_pts = 55
		self.assertEqual(3, st_tots.points_difference(arsenal_pts, spurs_pts))


	def test_get_available_points(self):
		games_played = 25
		self.assertEqual(39, st_tots.get_available_points(games_played))


	def test_make_soup(self):
		class_name = str(type(st_tots.make_soup(ST_TOTSTESTS.url)))
		self.assertEqual("<class 'bs4.BeautifulSoup'>", class_name)


	def test_get_team_name(self):
		self.assertEqual("Arsenal", st_tots.get_team_name(ST_TOTSTESTS.soup, 'td', ST_TOTSTESTS.team).get_text())


	def test_team_data(self):
		team_index = 4
		self.assertEqual("Arsenal", st_tots.get_team_data(ST_TOTSTESTS.soup, ST_TOTSTESTS.tag, ST_TOTSTESTS.team)[team_index].get_text())


	def test_get_team_games_played(self):
		min_games_in_season = 0
		games_played = st_tots.get_team_games_played(ST_TOTSTESTS.soup, ST_TOTSTESTS.tag, ST_TOTSTESTS.team)
		self.assertTrue(min_games_in_season <= games_played <= ST_TOTSTESTS.games_per_season)


	def test_get_team_points(self):
		points = st_tots.get_team_points(ST_TOTSTESTS.soup, ST_TOTSTESTS.tag, ST_TOTSTESTS.team)
		self.assertTrue(ST_TOTSTESTS.min_points <= points <= ST_TOTSTESTS.max_points)


	def test_soup_to_int(self):
		team_data = st_tots.get_team_data(ST_TOTSTESTS.soup, ST_TOTSTESTS.tag, ST_TOTSTESTS.team)
		games_played_index = 5
		self.assertEqual(int, type(st_tots.soup_to_int(team_data, games_played_index)))

	def test_check_soup_object(self):
		self.assertRaises(ValueError, st_tots.check_soup_object, 'not a BeautifulSoup object')

	def test_Team__init__games_played(self):
		arsenal = st_tots.Team(ST_TOTSTESTS.team, ST_TOTSTESTS.soup)
		self.assertTrue(0 < arsenal.games_played < ST_TOTSTESTS.games_per_season)


	def test_Team__init__team_points(self):
		arsenal = st_tots.Team(ST_TOTSTESTS.team, ST_TOTSTESTS.soup)
		self.assertTrue(0 < arsenal.team_points < ST_TOTSTESTS.max_points)



if __name__ == '__main__':
	unittest.main()