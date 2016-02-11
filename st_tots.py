
GAMES_IN_SEASON = 38
POINTS_PER_WIN = 3

#will retrieve current table data for Arsenal and Sp*rs
def get_table():
	return 'is this thing on?'

#compare current point to available points
def compare_difference_available(point_difference, available_points):
	return point_difference > available_points

#return the difference in pts between arsenal and spurs
def points_difference(arsenal_pts, spurs_pts):
	return arsenal_pts - spurs_pts

#return the remaining available points for a given number of games played
def get_available_points(games_played):
	return (GAMES_IN_SEASON - games_played) * POINTS_PER_WIN


