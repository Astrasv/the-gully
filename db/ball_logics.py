class BallLogics:
    def __init__(self, info, data):
        self.info = info
        self.data = data

    def match_meta(self):
        match_meta = {
            "city": self.info.get("city"),
            "dates": self.info.get("dates", []),  # Array
            "match_number": self.info.get("event", {}).get("match_number"),
            "season": self.info.get("season"),
            "venue": self.info.get("venue"),
            "team_a": self.info.get("teams", [None, None])[0],
            "team_b": self.info.get("teams", [None, None])[1],
            "toss_winner": self.info.get("toss", {}).get("winner"),
            "toss_decision": self.info.get("toss", {}).get("decision"),
            "outcome_winner": self.info.get("outcome", {}).get("winner"),
            "outcome_by_wickets": self.info.get("outcome", {})
            .get("by", {})
            .get("wickets"),
            "outcome_by_runs": self.info.get("outcome", {}).get("by", {}).get("runs"),
            "player_of_match": self.info.get("player_of_match", []),  # Array
            "umpire_1": self.info.get("officials", {}).get("umpires", [None, None])[0],
            "umpire_2": self.info.get("officials", {}).get("umpires", [None, None])[1],
            "tv_umpire": self.info.get("officials", {}).get("tv_umpires", [None])[0],
            "match_referee": self.info.get("officials", {}).get(
                "match_referees", [None]
            )[0],
        }

        return match_meta

    def handle_wickets(self, delivery):
        wickets = delivery.get("wickets", [])
        wicket_player_out = wickets[0].get("player_out") if wickets else None
        wicket_kind = wickets[0].get("kind") if wickets else None
        wicket_fielders = (
            [f.get("name") for f in wickets[0].get("fielders", [])] if wickets else []
        )

        keys = ["wicket_player_out", "wicket_kind", "wicket_fielders"]
        result = {k: locals()[k] for k in keys}
        return result

    def handle_reviews(self, review):
        review_by = review.get("by")
        review_umpire = review.get("umpire")
        review_decision = review.get("decision")
        review_type = review.get("type")
        review_umpires_call = (
            review.get("umpires_call") if not review.get("by") else False
        )
        keys = [
            "review_by",
            "review_umpire",
            "review_decision",
            "review_type",
            "review_umpires_call",
        ]

        result = {k: locals()[k] for k in keys}
        return result

    def handle_replacements(self, delivery):
        # Handle Impact Player Replacements
        replacements = delivery.get("replacements", {}).get("match", [])
        rep_in = replacements[0].get("in") if replacements else None
        rep_out = replacements[0].get("out") if replacements else None

        result = {"replacement_in": rep_in, "replacements_out": rep_out}

        return result

    def handle_extras(self, delivery):
        extra_wides = delivery.get("extras", {}).get("wides", 0)
        extra_legbyes = delivery.get("extras", {}).get("legbyes", 0)
        extra_legbyes = delivery.get("extras", {}).get("byes", 0)
        extra_noballs = delivery.get("extras", {}).get("noballs", 0)

        keys = ["extra_wides", "extra_legbyes", "extra_legbyes", "extra_noballs"]

        result = {k: locals()[k] for k in keys}
        return result

    def handle_ball_details(self, delivery):
        batter = delivery.get("batter")
        bowler = delivery.get("bowler")
        non_striker = delivery.get("non_striker")
        runs_batter = delivery.get("runs", {}).get("batter")
        runs_extras = delivery.get("runs", {}).get("extras")
        runs_total = delivery.get("runs", {}).get("total")

        keys = [
            "batter",
            "bowler",
            "non_striker",
            "runs_batter",
            "runs_extras",
            "runs_total",
        ]

        result = {k: locals()[k] for k in keys}
        return result
