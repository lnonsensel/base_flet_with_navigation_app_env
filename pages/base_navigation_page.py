from abc import abstractmethod
# Get main function used in packages lower
from base_page import BasePage
import flet as ft
from flet_route import Basket, Params
from dataclasses import dataclass

class NavigationPage(BasePage):
    def __init__(self) -> None:
        self.view = ft.View()

    @staticmethod
    @abstractmethod
    def get_navigation_metadata():
        pass
    
    def get_view(self, *args, **kwargs):
        return self.view

@dataclass
class PageNavigationMetadata:
    icon: ft.Image | bytes
    label: str
    route: str | None = None

@dataclass
class Page:
    navigation_page: NavigationPage
    navigation_metadata: PageNavigationMetadata