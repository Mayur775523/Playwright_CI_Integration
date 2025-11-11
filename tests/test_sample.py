def test_google_title(page):
    page.goto("https://www.google.com")
    title = page.title()
    assert "Google" in title
