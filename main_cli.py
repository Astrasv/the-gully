import os
from datetime import datetime


import httpx
from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.shortcuts import clear

from agents.sql_agent import SQLAgent

from tagging.entity_fetcher import EntityFetcher
from tagging.tag_lexer import SmartIPLLexer
from tagging.completer import IPLCompleter
from utils.clean_query import clean_query


cricket_style = Style.from_dict(
    {
        "username": "#FFD700 bold",
        "at": "#ffffff",
        "host": "#00BFFF bold",
        "colon": "#888888",
        "pound": "#32CD32",
        "text": "#ffffff",
        "mention-tag": "#FF4500 bold",
        "mention-value": "#00BFFF bold",
        "toolbar.accent": "#32CD32 bold",
        "completion-menu.completion.current": "bg:#0055aa #ffffff",
    }
)


def get_bottom_toolbar():
    now = datetime.now().strftime("%H:%M")
    return HTML(
        f' <b fg="#32CD32">THE GULLY</b> '
        f'<span fg="#666666">|</span> '
        f'<span fg="#ffffff">{now}</span> '
        f'<span fg="#666666">|</span> '
        f'Status: <b fg="#32CD32">LIVE 🟢</b>'
    )


kb = KeyBindings()


@kb.add("enter")
def _(event):
    if event.app.current_buffer.complete_state:
        event.app.current_buffer.complete_state = None
    else:
        event.app.current_buffer.validate_and_handle()


def show_man_page():
    clear()
    # FIX: Used proper <b fg="..."> tags which are valid XML for prompt_toolkit
    content = """
    <span fg="#FFD700">THE-GULLY</span>                     <span fg="#ffffff">Bowl your questions</span>                     <span fg="#FFD700">THE-GULLY</span>

    <b fg="#00BFFF">NAME</b>
        the-gully - Ask anything about IPL .. Literally ANYTHING !!!

    <b fg="#00BFFF">SYNOPSIS</b>
        <span fg="#32CD32">coach@stadium:🏏</span> [QUERY] 

    <b fg="#00BFFF">DESCRIPTION</b>
        This is The Gully CLI tool that converts natural language questions about IPL cricket
        history into answers. Stats gets cooked right in front of your eyes. Find answers to questions which even google cannot find.

    <b fg="#00BFFF">SYNTAX</b>
        Use the <span fg="#FF4500">@</span> symbol to trigger the entity menu.
        When every you want to use a player, team, venue, city or umpire name, start typing
        with the <span fg="#FF4500">@</span> symbol followed by the category and a hyphen.
        
        <span fg="#FF4500">@players-Name</span>      Target specific batters/bowlers
        <span fg="#FF4500">@teams-Name</span>        Target specific IPL franchises
        <span fg="#FF4500">@venues-Name</span>       Target stadiums
    
    <b fg="#00BFFF">CONTROLS</b>
        <span fg="#FFD700">TAB / Arrows</span>       Navigate suggestions
        <span fg="#FFD700">ENTER</span>              Select suggestion / Submit query
        <span fg="#FFD700">Ctrl + D</span>           Exit application
        <span fg="#FFD700">Ctrl + C</span>           Cancel current input
    <b fg="#00BFFF">EXAMPLES</b>
        How many sixes did <span fg="#FF4500">@players-MS Dhoni</span> score overall?
        Which matches were played at <span fg="#FF4500">@venues-M Chinnaswamy Stadium</span>?
        List all umpires who have officiated matches in <span fg="#FF4500">@cities-Bangalore</span>.
    <b fg="#00BFFF">OTHER COMMANDS</b>
        To exit the application, type <span fg="#FF4500">exit</span> or <span fg="#FF4500">quit</span> or press <span fg="#FF4500">Ctrl + D</span>.
        To view this manual again, type <span fg="#FF4500">help</span> or <span fg="#FF4500">man</span>

    <span fg="#888888">Press any key to enter the stadium...</span>
    """
    print_formatted_text(HTML(content))

    try:

        import sys

        if os.name == "nt":  
            import msvcrt

            msvcrt.getch()
        else:  # Unix/Linux
            import tty, termios

            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except Exception:
        input()


def print_agent_response(response_text: str):
    """Renders the Agent's response in a nice component box."""
    print_formatted_text(
        HTML(
            f"\n <span fg='#32CD32'>┌── 🤖 The Gully Analysis ──────────────────────────────────┐</span>"
        )
    )
    print_formatted_text(HTML(f" <span fg='#32CD32'>│</span>"))

    import textwrap

    wrapped = textwrap.wrap(response_text, width=70)
    for line in wrapped:
        # Escape special characters in content to prevent XML parsing errors
        safe_line = line.replace("<", "&lt;").replace(">", "&gt;")
        print_formatted_text(HTML(f" <span fg='#32CD32'>│</span>   {safe_line}"))

    print_formatted_text(HTML(f" <span fg='#32CD32'>│</span>"))
    print_formatted_text(
        HTML(
            f" <span fg='#32CD32'>└───────────────────────────────────────────────────────────┘</span>\n"
        )
    )


def main():
    show_man_page()
    clear()

    print_formatted_text(
        HTML("<span fg='#888888'>Initializing Neural Engine...</span>")
    )

    try:
        agent = SQLAgent()
        print_formatted_text(HTML("<span fg='#32CD32'>✔ Agent Online</span>"))
    except Exception as e:
        print_formatted_text(HTML(f"<span fg='#FF4500'>✘ Agent Error: {e}</span>"))
        return

    fetcher = EntityFetcher()
    entities = fetcher.fetch_entities()
    smart_lexer = SmartIPLLexer(entities)

    session = PromptSession(
        completer=IPLCompleter(entities),
        lexer=smart_lexer,
        style=cricket_style,
        key_bindings=kb,
        bottom_toolbar=get_bottom_toolbar,
        refresh_interval=1.0,
    )

    splash = """
    <span fg="#87CEFA">
     ██████╗ ██╗   ██╗██╗     ██╗     ██╗   ██╗
    ██╔════╝ ██║   ██║██║     ██║     ╚██╗ ██╔╝</span>
    <span fg="#1E90FF">██║  ███╗██║   ██║██║     ██║      ╚████╔╝ 
    ██║   ██║██║   ██║██║     ██║       ╚██╔╝  </span>
    <span fg="#4169E1">╚██████╔╝╚██████╔╝███████╗███████╗   ██║   
     ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   </span>
    """
    print_formatted_text(HTML(splash))
    print_formatted_text(
        HTML(
            "\n<span fg='#888888'>Type your query below. e.g., 'How many sixes did @players-MS Dhoni score overall?'</span>\n"
        )
    )

    while True:
        try:
            prompt_msg = [
                ("class:username", "coach"),
                ("class:at", "@"),
                ("class:host", "stadium"),
                ("class:colon", ":"),
                ("class:pound", "🏏 "),
            ]

            user_input = session.prompt(prompt_msg)

            if user_input.strip():
                processed_query = clean_query(user_input)

                try:
                    if processed_query.lower() in {"exit", "quit"}:
                        print_formatted_text(
                            HTML("\n<span fg='#FF4500'>Stumps called. Adios!</span>")
                        )
                        break
                    elif processed_query.lower() in {"help", "man"}:
                        show_man_page()
                    else:
                        endpoint_url = "http://127.0.0.1:8001/agents/query"
                        params = {"query": processed_query}
                        
                        try:
                            with httpx.Client(timeout=120.0) as client:
                                response = client.get(endpoint_url, params=params)
                                response.raise_for_status() 
                                data = response.json()
                                agent_response = data.get("response", "No response from agent.")
                        except httpx.RequestError as exc:
                            agent_response = f"An error occurred while requesting {exc.request.url!r}."
                        
                        print_agent_response(str(agent_response))
                except Exception as e:
                    print_formatted_text(
                        HTML(
                            f"\n<span fg='#FF4500'>Error executing query: {e}</span>\n"
                        )
                    )

        except KeyboardInterrupt:
            continue
        except EOFError:
            print_formatted_text(
                HTML("\n<span fg='#FF4500'>Stumps called. Adios!</span>")
            )
            break


if __name__ == "__main__":
    main()
