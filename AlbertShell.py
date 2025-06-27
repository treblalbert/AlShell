from textual.app import App, ComposeResult
from textual.widgets import Input, Static
from textual.containers import Vertical
from textual.reactive import reactive

class AlbertShell(App):
    TITLE = "AlbertShell"
    CSS = """
    Screen {
        background: #1e1e2f;
        color: #cdd6f4;
        padding: 1;
    }
    #header {
        height: 3;
        content-align: center middle;
        background: #313244;
        color: #89b4fa;
        border: round cornflowerblue;
        margin-bottom: 1;
        text-style: bold;
    }
    #messages {
        background: #313244;
        height: 80%;
        border: round cornflowerblue;
        padding: 1;
        overflow-y: auto;
    }
    #input {
        background: #45475a;
        border: round #89b4fa;
        height: 3;
        padding-left: 1;
    }
    """

    messages = reactive([])

    def compose(self) -> ComposeResult:
        yield Vertical(
            Static("Welcome to AlbertShell!", id="header"),
            Static(id="messages"),
            Input(placeholder="Type your command here...", id="input"),
        )

    def on_mount(self):
        self.query_one("#input").focus()

    def on_input_submitted(self, event: Input.Submitted):
        message = event.value.strip()
        if message:
            self.messages.append(message)
            self.update_messages()
        self.query_one("#input").value = ""

    def update_messages(self):
        messages_widget = self.query_one("#messages", Static)
        messages_widget.update("\n".join(self.messages))

if __name__ == "__main__":
    AlbertShell().run()
