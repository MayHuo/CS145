# Collaborators: Fill in names and SUNetIDs here

def query_one():
    """Query for Stanford's venue"""
    return """
       SELECT
         venue_name,
         venue_capacity
       FROM `bigquery-public-data.ncaa_basketball.mbb_teams`
       WHERE market = 'Stanford';
    """

def query_two():
    """Query for games in Stanford's venue"""
    return """
       SELECT COUNT(DISTINCT game_id)
       FROM `bigquery-public-data.ncaa_basketball.mbb_teams_games_sr`
       WHERE venue_name = 'Maples Pavilion'
       AND season = 2013;
    """

def query_three():
    """Query for maximum-red-intensity teams"""
    return """
       SELECT market, color
       FROM `bigquery-public-data.ncaa_basketball.team_colors`
       WHERE color like ANY ('#ff%', '#FF%')
       ORDER BY market;
    """

def query_four():
    """Query for Stanford's wins at home"""
    return """
       SELECT
         COUNT(game_id) as number,
         ROUND(AVG(points), 2) as avg_stanford,
         ROUND(AVG(opp_points), 2) as avg_opponent
       FROM `bigquery-public-data.ncaa_basketball.mbb_teams_games_sr`
       WHERE market = 'Stanford'
         AND season BETWEEN 2013 AND 2017
         AND home_team = true
         AND win = true;
    """

def query_five():
    """Query for players for birth city"""
    return """
       SELECT
         COUNT(DISTINCT player_id) as num_players
       FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr` as pg
       JOIN `bigquery-public-data.ncaa_basketball.mbb_teams` as t
       ON pg.team_id = t.id
       WHERE pg.birthplace_state = t.venue_state
        AND pg.birthplace_city = t.venue_city;
    """

def query_six():
    """Query for biggest blowout"""
    return """
       SELECT
         win_name,
         lose_name,
         win_pts,
         lose_pts,
         win_pts - lose_pts as margin
      FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`
      ORDER BY margin DESC LIMIT 1;
    """

def query_seven():
    """Query for historical upset percentage"""
    return """
        SELECT
          ROUND(
            (SUM(CASE WHEN win_seed > lose_seed THEN 1 ELSE 0 END) *100)/COUNT(*),
            2) AS upset_percentage
        FROM `bigquery-public-data.ncaa_basketball.mbb_historical_tournament_games`;
    """

def query_eight():
    """Query for teams with same states and colors"""
    return """
       WITH cte AS
           (SELECT
              team.id AS id,
              name,
              venue_state,
              color.color as team_color
            FROM `bigquery-public-data.ncaa_basketball.mbb_teams` AS team
            JOIN `bigquery-public-data.ncaa_basketball.team_colors` AS color
            ON team.id = color.id
            )
    SELECT
       A.name AS teamA,
       B.name AS teamB,
       A.venue_state AS state
    FROM cte AS A
    INNER JOIN cte AS B
    ON A.team_color = B.team_color AND A.venue_state = B.venue_state
    WHERE A.name < B.name
    ORDER BY teamA;
    """

def query_nine():
    """Query for top geographical locations"""
    return """
       SELECT
          birthplace_city AS city,
          birthplace_state AS state,
          birthplace_country AS country,
          SUM(points) AS total_points
        FROM `bigquery-public-data.ncaa_basketball.mbb_players_games_sr`
        WHERE team_market = 'Stanford' AND points > 0
        GROUP BY birthplace_city, birthplace_state, birthplace_country
        ORDER BY total_points DESC limit 3;
    """

def query_ten():
    """Query for teams with lots of high-scorers"""
    return """
       SELECT
          team_market,
          COUNT(DISTINCT player_id) as num_players
        FROM
          (
            SELECT
              game_id, player_id, team_market,
              SUM(points_scored) AS points,
              
            FROM `bigquery-public-data.ncaa_basketball.mbb_pbp_sr`
            WHERE period = 1 AND season >= 2013 AND points_scored > 0
            GROUP BY game_id, player_id, team_market
            HAVING points >= 15
          )
        GROUP BY team_market
        HAVING num_players > 5
        ORDER BY num_players DESC limit 5;
    """

def query_eleven():
    """Query for highest-winner teams"""
    return """
       SELECT
          market,
          COUNT(*) AS top_performer_count
        FROM
         (
          SELECT
            market,
            wins,
            RANK() OVER(PARTITION BY season ORDER BY wins DESC) AS rankinseason
          FROM `bigquery-public-data.ncaa_basketball.mbb_historical_teams_seasons`
          WHERE season BETWEEN 1900 AND 2000
          QUALIFY rankinseason = 1
         )
        WHERE market IS NOT NULL
        GROUP BY market
        ORDER BY top_performer_count DESC LIMIT 5;
    """