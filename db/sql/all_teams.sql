SELECT 
    team 
FROM (
    SELECT team_a AS team FROM ipl_ball_by_ball UNION
    SELECT team_b FROM ipl_ball_by_ball UNION
    SELECT batting_team FROM ipl_ball_by_ball UNION
    SELECT toss_winner FROM ipl_ball_by_ball UNION
    SELECT outcome_winner FROM ipl_ball_by_ball UNION
    SELECT review_by FROM ipl_ball_by_ball
) AS teams
WHERE team IS NOT NULL;