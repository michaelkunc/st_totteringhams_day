import unittest
import st_tots

class ST_TOTSTESTS(unittest.TestCase):
	@classmethod
	def setUpClass(ST_TOTSTESTS):
		ST_TOTSTESTS.points_per_win = 3
		ST_TOTSTESTS.games_per_season = 38
		ST_TOTSTESTS.max_points = ST_TOTSTESTS.games_per_season * ST_TOTSTESTS.points_per_win
		ST_TOTSTESTS.soup = st_tots.Soup('http://www.premierleague.com/en-gb/matchday/league-table.html')
		ST_TOTSTESTS.arsenal = st_tots.Team('Arsenal', ST_TOTSTESTS.soup)
		ST_TOTSTESTS.spurs = st_tots.Team('Tottenham Hotspur', ST_TOTSTESTS.soup)

#need to review this test to make sure it's testing something valuable.
	def test_init_Soup(self):
		class_name = str(type(ST_TOTSTESTS.soup))
		self.assertEqual("<class 'st_tots.Soup'>", class_name)

	def test_Team__init__games_played(self):
		self.assertTrue(0 < ST_TOTSTESTS.arsenal.games_played < ST_TOTSTESTS.games_per_season)


	def test_Team__init__team_points(self):
		self.assertTrue(0 < ST_TOTSTESTS.arsenal.points < ST_TOTSTESTS.max_points)

#this is a slightly gnarley test case.
	def test_Team_get_team_data(self):
		self.assertEqual('<td class="col-pos">3</td>', str(ST_TOTSTESTS.arsenal.get_team_data(ST_TOTSTESTS.soup, 'td', "Arsenal")[0]))


	def test_Team_available_points(self):
		self.assertTrue(0 < ST_TOTSTESTS.arsenal.available_points(ST_TOTSTESTS.arsenal.games_played) < ST_TOTSTESTS.max_points)

	def test_check_for_st_tots_not_achieved(self):
		self.assertFalse(st_tots.st_tots(ST_TOTSTESTS.arsenal, ST_TOTSTESTS.spurs))

	def test_check_for_st_tots_achieved(self):
		#stubbing out attributes to trigger the else condition
		arsenal = st_tots.Team('Arsenal', ST_TOTSTESTS.soup)
		arsenal.points = 100
		spurs = st_tots.Team('Tottenham Hotspur', ST_TOTSTESTS.soup)
		spurs.points = 0
		self.assertTrue(st_tots.st_tots(arsenal, spurs))

	def test_end_of_season(self):
		self.assertFalse(st_tots.end_of_season(ST_TOTSTESTS.arsenal, ST_TOTSTESTS.spurs))


	def test_simulate_remaining_season(self):
		st_tots.simulate_remaining_season(ST_TOTSTESTS.arsenal, ST_TOTSTESTS.spurs)
		self.assertEqual( st_tots.Messages.st_tots_message(), st_tots.simulate_remaining_season(ST_TOTSTESTS.arsenal, ST_TOTSTESTS.spurs))

	def test_simulate_remaining_season_end_of_season(self):
		#stubbing attributes to trigger the elif condition
		arsenal = st_tots.Team('Arsenal', ST_TOTSTESTS.soup)
		arsenal.games_played = 38
		arsenal.points = 0
		spurs = st_tots.Team('Tottenham Hotspur', ST_TOTSTESTS.soup)
		spurs.games_played = 38
		spurs.points = 0
		self.assertEqual( st_tots.Messages.end_of_season_message(), st_tots.simulate_remaining_season(arsenal, spurs))


if __name__ == '__main__':
	unittest.main()