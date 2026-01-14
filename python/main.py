import cli_commands
from textual.containers import HorizontalGroup, VerticalScroll
from textual.app import *
from textual.widgets import *

total_flavours = cli_commands.amount_flavours()
flavours = cli_commands.list_flavours()


class Counter(HorizontalGroup):
    def __init__(self, i):
        super().__init__()
        self.i = i

    def compose(self) -> ComposeResult:
        yield Static(flavours[self.i][0], classes="flavour-name")
        yield Static(str(cli_commands.get_entry_total(flavours[self.i][0])), classes="flavour-count")

class RedbullApp(App):
    CSS_PATH = "RedbullApp.tcss"

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        with TabbedContent():
            with TabPane("Totals"):
                with VerticalScroll():
                    for i in range(0, total_flavours):
                        yield Counter(i)
            with TabPane("Add"):
                yield Static("test")
        yield Footer()


    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

def main():
    print(cli_commands.get_entry_total("Original"))    


if __name__ == "__main__":
    app = RedbullApp()
    app.run()
    #main()
