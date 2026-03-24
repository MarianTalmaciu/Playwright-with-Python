def test_example():
    assert 1 + 1 == 2


# playwright pytest script to open a browser and go to google.com and verify the title

# from playwright.sync_api import Page


# def test_google_title(page: Page):
#     # open browser and navigate to Google
#     page.goto("https://www.google.com")

#     # verify the title contains 'Google'
#     assert "Google" in page.title()