import cli_commands
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Digits, Static




class RedbullApp(App):

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Digits(str(cli_commands.amount_flavours()))
        yield Static(str(cli_commands.list_flavours()), classes="title")

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

def main():
    print(cli_commands.list_flavours())    


if __name__ == "__main__":
    app = RedbullApp()
    app.run()
    # main()
