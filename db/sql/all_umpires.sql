SELECT umpires 
FROM (
    SELECT umpire_1 AS umpires FROM ipl_ball_by_ball UNION
    SELECT umpire_2 FROM ipl_ball_by_ball UNION
    SELECT tv_umpire FROM ipl_ball_by_ball UNION
    SELECT match_referee FROM ipl_ball_by_ball UNION
    SELECT review_umpire FROM ipl_ball_by_ball
) AS umpire_list
WHERE umpires IS NOT NULL;