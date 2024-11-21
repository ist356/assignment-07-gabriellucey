import re
from playwright.sync_api import Playwright, sync_playwright
from menuitemextractor import extract_menu_item
from menuitem import MenuItem
import pandas as pd

def tullyscraper(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
  
    items = []
    for item in page.query_selector_all("h3.foodmenu__menu-section-title"):
        title = item.inner_text()
        for row in item.query_selector("~ *").query_selector("~ *").query_selector_all("div.foodmenu__menu-item"):
            text = row.inner_text()
            menu_item = extract_menu_item(title, text)
            items.append(menu_item.to_dict())
    data = pd.DataFrame(items)
    data.to_csv("./cache/tullys_menu.csv", index=False)
    context.close()
    browser.close()


with sync_playwright() as playwright:
    tullyscraper(playwright)
