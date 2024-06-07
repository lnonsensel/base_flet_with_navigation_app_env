from app_config import apply_config_to_page
from navigation import Navigation
from pages import get_pages
import flet as ft

main_window_class = Navigation

async def main(page: ft.Page):
    apply_config_to_page(page)
    navigation_pages = await get_pages()
    window = main_window_class(page, navigation_pages)
    await window.init_navigation_elements()


if __name__ == '__main__':
    ft.app(target = main, view = ft.AppView.WEB_BROWSER, port=5000, assets_dir='assets')