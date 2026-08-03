from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1200, "height": 630})
    page.goto("file:///tmp/ai-weekly/og-page.html", wait_until="networkidle")
    page.wait_for_timeout(1500)
    page.screenshot(path="/tmp/ai-weekly/og-image.png", full_page=False)
    browser.close()
print("screenshot done")
