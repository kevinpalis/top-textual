from textual.widget import Widget
from textual.reactive import reactive
from textual.widgets import DataTable
from textual.message import Message
from textual import events
from utils.data_source import get_process_data
import asyncio

class ProcessTable(Widget):
    def __init__(self, refresh_interval: float = 10.0, data_provider=get_process_data) -> None:
        super().__init__()
        self.refresh_interval = refresh_interval
        self.data_provider = data_provider
        self.table = DataTable()

    async def on_mount(self) -> None:
        await self.update_table()
        self.set_interval(self.refresh_interval, self.update_table)
        await self.mount(self.table)

    async def update_table(self) -> None:
        data = self.data_provider()
        self.table.clear(columns=True)
        self.table.add_columns(*data[0])
        for row in data[1:]:
            self.table.add_row(*row)