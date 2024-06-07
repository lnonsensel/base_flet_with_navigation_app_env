# IMPORT ALL PAGES
from pages.base_navigation_page import BasePage # Sample

from pages.base_navigation_page import NavigationPage, Page
import flet as ft
import typing as tp


pages_classes: list[tp.Type[NavigationPage]] = [BasePage]

async def get_pages() -> list[Page]:
    pages: list[Page] = []
    for page_class in pages_classes:
        page_instance = page_class()
        await page_instance.get_elements()
        pages.append(
            Page(page_instance,
                 page_instance.get_navigation_metadata())
        )
    return pages

