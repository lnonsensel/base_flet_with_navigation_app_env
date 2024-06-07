import flet as ft
TITLE = "Sample flet app"

VERTICAL_ALIGNMENT = ft.MainAxisAlignment.CENTER
WINDOW_WIDTH = 350
WINDOW_HEIGHT = 400
WINDOW_RESIZABLE = False

NAVIGATION_BAR_HEIGHT = 100

MAIN_PAGE_THEME = ft.Theme()
MAIN_PAGE_THEME.page_transitions.linux = ft.PageTransitionTheme.NONE
MAIN_PAGE_THEME.page_transitions.windows = ft.PageTransitionTheme.NONE
MAIN_PAGE_THEME.page_transitions.android = ft.PageTransitionTheme.NONE
MAIN_PAGE_THEME.page_transitions.ios = ft.PageTransitionTheme.NONE

def apply_config_to_page(page: ft.Page):
    page.title = TITLE
    page.vertical_alignment = VERTICAL_ALIGNMENT
    page.window_width = WINDOW_WIDTH
    page.window_height = WINDOW_HEIGHT
    page.window_resizable = WINDOW_RESIZABLE
    main_page_data.PAGE_WIDTH = page.width
    main_page_data.PAGE_HEIGHT = page.height
    page.theme = MAIN_PAGE_THEME
    page.update()


from dataclasses import dataclass

@dataclass
class MainPageData:
    PAGE_WIDTH: int | None = None 
    PAGE_HEIGHT: int | None = None 

main_page_data = MainPageData()