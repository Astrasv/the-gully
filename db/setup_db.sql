-- CREATE DATABASE IF NOT EXISTS ipl_database;

DROP TABLE IF EXISTS ipl_ball_by_ball;
CREATE TABLE ipl_ball_by_ball (
    id SERIAL PRIMARY KEY,

    -- Match metadata
    match_id INTEGER,
    city TEXT,
    dates DATE[],
    match_number INTEGER,
    season INTEGER[],
    venue TEXT,
    team_a TEXT,
    team_b TEXT,

    -- Toss
    toss_winner TEXT,
    toss_decision TEXT,

    -- Outcome
    outcome_winner TEXT,
    outcome_by_wickets INTEGER,
    outcome_by_runs INTEGER,
    player_of_match TEXT[],

    -- Officials
    umpire_1 TEXT,
    umpire_2 TEXT,
    tv_umpire TEXT,
    match_referee TEXT,

    -- Innings / delivery
    innings_val INTEGER,
    batting_team TEXT,
    ball_over INTEGER,
    ball_number INTEGER,
    batter TEXT,
    bowler TEXT,
    non_striker TEXT,

    -- Runs
    runs_batter INTEGER,
    runs_extras INTEGER,
    runs_total INTEGER,

    -- Extras
    extra_wides INTEGER,
    extra_legbyes INTEGER,
    extra_noballs INTEGER,

    -- Wicket
    wicket_player_out TEXT,
    wicket_kind TEXT,
    wicket_fielders TEXT[],

    -- Review
    review_by TEXT,
    review_umpire TEXT,
    review_decision TEXT,
    review_type TEXT,
    review_umpires_call BOOLEAN,

    -- Replacement
    replacement_in TEXT,
    replacements_out TEXT
);
