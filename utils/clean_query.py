
import re

def clean_query(text: str) -> str:
    """Removes @ symbols for the SQL Agent."""
    pattern = r'@(?P<cat>players|teams|venues|cities|umpires)-(?P<val>.*?)(?=\s|$)'
    def replacement(match):
        return f"{match.group('cat')}-{match.group('val')}"
    return re.sub(pattern, replacement, text)