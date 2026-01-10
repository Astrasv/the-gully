CREATE TABLE teams AS
SELECT 
    row_number() OVER (ORDER BY team) AS team_id, 
    team AS team_name
FROM (
    SELECT team_a AS team FROM ipl_ball_by_ball UNION
    SELECT team_b FROM ipl_ball_by_ball UNION
    SELECT batting_team FROM ipl_ball_by_ball UNION
    SELECT toss_winner FROM ipl_ball_by_ball UNION
    SELECT outcome_winner FROM ipl_ball_by_ball UNION
    SELECT review_by FROM ipl_ball_by_ball
) teams_subquery
WHERE team IS NOT NULL;