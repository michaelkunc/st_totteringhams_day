import unittest
import st_tots


class TOTSTESTS(unittest.TestCase):

    @classmethod
    def setUpClass(TOTSTESTS):
        TOTSTESTS.points_per_win = 3
        TOTSTESTS.games_per_season = 38
        TOTSTESTS.max_points = TOTSTESTS.games_per_season * TOTSTESTS.points_per_win
        TOTSTESTS.table_soup = st_tots.Soup(
            'http://www.premierleague.com/en-gb/matchday/league-table.html')
        TOTSTESTS.arsenal = st_tots.Team('Arsenal', TOTSTESTS.table_soup)
        TOTSTESTS.spurs = st_tots.Team(
            'Tottenham Hotspur', TOTSTESTS.table_soup)
        TOTSTESTS.match_soup = st_tots.Soup(
            'http://www.bbc.com/sport/football/teams/arsenal/fixtures')
        TOTSTESTS.match_days = st_tots.Matchdays(TOTSTESTS.match_soup)

    def test_http_response_table(self):
        page = st_tots.urlopen(st_tots.TABLE_URL)
        self.assertEqual(200, page.getcode())

    def test_http_response_match(self):
        page = st_tots.urlopen(st_tots.MATCHDAY_URL)
        self.assertEqual(200, page.getcode())

# need to review this test to make sure it's testing something valuable.
    def test_init_Soup(self):
        class_name = str(type(TOTSTESTS.table_soup))
        self.assertEqual("<class 'st_tots.Soup'>", class_name)

    def test_Team__init__games_played(self):
        self.assertTrue(0 < TOTSTESTS.arsenal.games_played <
                        TOTSTESTS.games_per_season)

    def test_Team__init__team_points(self):
        self.assertTrue(0 < TOTSTESTS.arsenal.points < TOTSTESTS.max_points)

# this is a slightly gnarley test case.
    def test_Team_get_team_data(self):
        self.assertEqual('<td class="col-pos">3</td>', str(
            TOTSTESTS.arsenal.get_team_data(TOTSTESTS.table_soup, 'td', "Arsenal")[0]))

    def test_Team_available_points(self):
        self.assertTrue(0 < TOTSTESTS.arsenal.available_points(
            TOTSTESTS.arsenal.games_played) < TOTSTESTS.max_points)

    def test_Matchdays_init_matches(self):
        self.assertEqual(list, type(TOTSTESTS.match_days.matches))

    def test_check_for_st_tots_not_achieved(self):
        self.assertFalse(st_tots.st_tots(TOTSTESTS.arsenal, TOTSTESTS.spurs))

    def test_check_for_st_tots_achieved(self):
        # stubbing out attributes to trigger the else condition
        arsenal = st_tots.Team('Arsenal', TOTSTESTS.table_soup)
        arsenal.points = 100
        spurs = st_tots.Team('Tottenham Hotspur', TOTSTESTS.table_soup)
        spurs.points = 0
        self.assertTrue(st_tots.st_tots(arsenal, spurs))

    def test_end_of_season(self):
        self.assertFalse(st_tots.end_of_season(
            TOTSTESTS.arsenal, TOTSTESTS.spurs))

        #need to fix this test case so it calls the entire message.
    def test_simulate_remaining_season(self):
        st_tots.simulate_remaining_season(TOTSTESTS.arsenal, TOTSTESTS.spurs, TOTSTESTS.match_days)
        self.assertEqual(st_tots.Messages.st_tots_message() + 'Sat 2 Apr', st_tots.simulate_remaining_season(TOTSTESTS.arsenal, TOTSTESTS.spurs, TOTSTESTS.match_days))

    def test_simulate_remaining_season_end_of_season(self):
        # stubbing attributes to trigger the elif condition
        arsenal = st_tots.Team('Arsenal', TOTSTESTS.table_soup)
        arsenal.games_played = 38
        arsenal.points = 0
        spurs = st_tots.Team('Tottenham Hotspur', TOTSTESTS.table_soup)
        spurs.games_played = 38
        spurs.points = 0
        self.assertEqual(st_tots.Messages.end_of_season_message(
        ), st_tots.simulate_remaining_season(arsenal, spurs, TOTSTESTS.match_days))


if __name__ == '__main__':
    unittest.main()
