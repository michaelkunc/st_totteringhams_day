[![Coverage Status](https://coveralls.io/repos/github/michaelkunc/st_totteringhams_day/badge.svg?branch=master)](https://coveralls.io/github/michaelkunc/st_totteringhams_day?branch=master)

# When is St Totteringham's Day?
All Arsenal FC Supporters look forward to a very special day of the year: St Totteringham's Day. This is the day when it is mathematically assured that Arsenal FC will finish above Tottenham Hotspur.

It was first created in 2002.

This tool will tell the user the earliest possible occurance of St Totteringham's Day based on the current table and the remaining schedule.

Upon load the tool will fetch the current table as well as the remaining schedule.

# MVP User Story

As a user I want to be able to see the earliest day that St. Totteringham's Day will occur. It should be based on the latest table and schedule data.

The script will assume that Arsenal win and Spurs lose every game until St Totteringham's Day occurs.

It should return a matchday in the form of a date and it should assume that Arsenal win and Spurs lose on that day.

# Psudeocode

1. Check the table to get the current points and number of matches for both Arsenal & Sp*rs.

2. Determine how many points are available for Sp*rs.

3. Is that number less than the current difference? If so, then we have achieved St. Totts. If not, we continue the iteration.

4. Assume that Arsenal wins and Sp*rs loses. And re-do the iteration.
