from typing import Dict, List
import re

from prompt_toolkit.lexers import Lexer


class SmartIPLLexer(Lexer):
    def __init__(self, entities: Dict[str, List[str]]):
        self.entities = entities

    def lex_document(self, document):
        def get_line(lineno):
            line = document.lines[lineno]
            tokens = []
            last_pos = 0
            pattern = r"(@(?P<cat>players|teams|venues|cities|umpires)-)(?P<rest>.*?)($|(?=@))"

            for match in re.finditer(pattern, line):
                tokens.append(("class:text", line[last_pos : match.start()]))
                tokens.append(("class:mention-tag", match.group(1)))

                cat = match.group("cat")
                full_rest = match.group("rest")
                valid_options = self.entities.get(cat, [])
                best_match_len = 0

                for i in range(len(full_rest), 0, -1):
                    sub = full_rest[:i]
                    if any(e.lower().startswith(sub.lower()) for e in valid_options):
                        best_match_len = i
                        break

                if best_match_len > 0:
                    tokens.append(("class:mention-value", full_rest[:best_match_len]))
                    tokens.append(("class:text", full_rest[best_match_len:]))
                else:
                    tokens.append(("class:text", full_rest))

                last_pos = match.end()

            tokens.append(("class:text", line[last_pos:]))
            return tokens

        return get_line
