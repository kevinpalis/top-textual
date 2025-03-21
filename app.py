# app.py
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer
from textual.reactive import reactive
from components.process_table import ProcessTable

class TopLikeApp(App):
    CSS_PATH = "styles/app.css"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    interval = reactive(10.0)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(ProcessTable(refresh_interval=self.interval))
        yield Footer()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = TopLikeApp()
    app.run()