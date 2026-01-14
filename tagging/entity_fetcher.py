from typing import Dict, List
import tagging.config  # noqa: F401
import psycopg2
from pathlib import Path


class EntityFetcher:
    def __init__(self):
        try:
            self.config = tagging.config.TaggingConfig()
            self.conn = psycopg2.connect(
                host=self.config.host,
                port=self.config.port,
                database=self.config.database,
                user=self.config.user,
                password=self.config.password,
            )
        except Exception:
            self.conn = None

    def fetch_entities(self) -> Dict[str, List[str]]:

        team_file = Path("db/sql/all_teams.sql")
        players_file = Path("db/sql/all_players.sql")
        umpires_file = Path("db/sql/all_umpires.sql")
        venues_file = Path("db/sql/all_venues.sql")
        cities_file = Path("db/sql/all_cities.sql")

        # SQL text
        teams_sql = team_file.read_text()
        players_sql = players_file.read_text()
        umpires_sql = umpires_file.read_text()
        venues_sql = venues_file.read_text()
        cities_sql = cities_file.read_text()

        queries = {
            "players": players_sql,
            "teams": teams_sql,
            "venues": venues_sql,
            "cities": cities_sql,
            "umpires": umpires_sql,
        }
        res = {}
        with self.conn.cursor() as cur:
            for k, q in queries.items():
                cur.execute(q)
                res[k] = sorted({r[0].strip() for r in cur.fetchall() if r[0]})
        return res
