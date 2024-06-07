from typing import Coroutine
import flet as ft
from app_config import *
from pages import Page
from base_page import BasePage
from flet_route import Routing, path
from dataclasses import dataclass
import asyncio

@dataclass
class Navigation:
    navigation_bar: ft.NavigationBar | None = None

class Navigation:
    def __init__(self, page: ft.Page, pages_instances: list[Page]) -> None:
        self.elements = Navigation()
        self.page = page
        self.pages_instances = pages_instances

    async def navigate(self, event: ft.ControlEvent):
        selected_index = event.control.selected_index
        selected_page: Page = self.pages_instances[selected_index]
        self.page.go(selected_page.navigation_metadata.route)
        self.page.update()

    async def init_navigation_bar(self):
        destinations = [ft.NavigationDestination(icon = page_instance.navigation_metadata.icon, label=page_instance.navigation_metadata.label) for page_instance in self.pages_instances]
        navigation_bar = ft.NavigationBar(destinations=destinations,
                                          on_change=self.navigate,
                                          height=NAVIGATION_BAR_HEIGHT,
                                          animation_duration=0)
        for page_instance in self.pages_instances:
            page_instance.navigation_page.view.controls.append(navigation_bar)
        await self.page.add_async(navigation_bar)

    async def init_page_routes(self):
        app_routes = [
            path(
                url = page_instance.navigation_metadata.route,
                clear = True,
                view = page_instance.navigation_page.get_view
           ) for page_instance in self.pages_instances
        ]
        Routing(page=self.page,
                app_routes=app_routes)
        self.page.go('/')

    async def init_navigation_elements(self):
        await self.init_page_routes()
        navigation_bar = await self.init_navigation_bar()
        self.elements.navigation_bar = navigation_bar


    