SELECT player_name
FROM (
        SELECT batter AS player_name
        FROM ipl_ball_by_ball
        UNION
        SELECT bowler
        FROM ipl_ball_by_ball
        UNION
        SELECT non_striker
        FROM ipl_ball_by_ball
        UNION
        SELECT wicket_player_out
        FROM ipl_ball_by_ball
        UNION
        SELECT unnest(wicket_fielders)
        FROM ipl_ball_by_ball
        UNION
        SELECT unnest(player_of_match)
        FROM ipl_ball_by_ball
        UNION
        SELECT replacement_in
        FROM ipl_ball_by_ball
        UNION
        SELECT replacements_out
        FROM ipl_ball_by_ball
    ) t
WHERE
    player_name IS NOT NULL;