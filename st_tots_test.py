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

	def test_get_table(self):
		self.assertEqual('is this thing on?', st_tots.get_table())

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
		self.assertEqual("Arsenal", st_tots.get_team_name(ST_TOTSTESTS.url, ST_TOTSTESTS.tag, ST_TOTSTESTS.team).get_text())

	def test_team_data(self):
		team_index = 4
		self.assertEqual("Arsenal", st_tots.get_team_data(ST_TOTSTESTS.url, ST_TOTSTESTS.tag, ST_TOTSTESTS.team)[team_index].get_text())

#woud like to fix these 'magic numbers' in this test method
	def test_get_team_games_played(self):
		min_games_in_season = 0
		max_games_in_season = 38
		games_played = st_tots.get_team_games_played(ST_TOTSTESTS.url, ST_TOTSTESTS.tag, ST_TOTSTESTS.team)
		self.assertTrue(min_games_in_season <= games_played <= max_games_in_season)

	def test_get_team_points(self):
		points = st_tots.get_team_points(ST_TOTSTESTS.url, ST_TOTSTESTS.tag, ST_TOTSTESTS.team)
		self.assertTrue(ST_TOTSTESTS.min_points <= points <= ST_TOTSTESTS.max_points)

		
if __name__ == '__main__':
	unittest.main()