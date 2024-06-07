from abc import abstractmethod, ABC
import flet as ft

class BasePage(ABC):
    def __init___(self):
        self.view = ft.View()

    @abstractmethod
    async def get_elements(self) -> tuple[ft.Control]:
        pass
