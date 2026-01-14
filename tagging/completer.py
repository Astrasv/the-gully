from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML
import re


class IPLCompleter(Completer):
    def __init__(self, entities):
        self.entities = entities
        self.categories = list(entities.keys())

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor

        if text.endswith("@"):
            for cat in self.categories:
                yield Completion(
                    f"{cat}-",
                    start_position=0,
                    display=HTML(f"<span fg='#FFD700'>📁</span> <b>{cat}</b>"),
                )
            return

        match = re.search(r"@(?P<cat>\w+)-(?P<pre>[\w\s]*)$", text)
        if match:
            cat, pre = match.group("cat"), match.group("pre").lower()
            for option in self.entities.get(cat, []):
                if pre in option.lower():
                    yield Completion(
                        option,
                        start_position=-len(pre),
                        display=HTML(f"<span fg='#00FF00'>🏏</span> {option}"),
                    )
