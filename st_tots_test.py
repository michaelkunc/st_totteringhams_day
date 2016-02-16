import unittest
import st_tots

class ST_TOTSTESTS(unittest.TestCase):

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
		url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'
		class_name = str(type(st_tots.make_soup(url)))
		self.assertEqual("<class 'bs4.BeautifulSoup'>", class_name)

	# def test_get_team(self):
	# 	url = 'http://www.premierleague.com/en-gb/matchday/league-table.html'
	# 	tag = 'td'
	# 	team = 'Arsenal'
	# 	self.assertEqual("Arsenal", st_tots.get_team(url, tag, team))

if __name__ == '__main__':
	unittest.main()