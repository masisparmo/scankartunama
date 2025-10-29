from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Navigate to the local HTML file
        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # Make the edit form visible to capture all buttons
        page.evaluate("() => { document.getElementById('edit-form-card').classList.remove('hidden'); }")

        # Take a screenshot of the whole page
        page.screenshot(path='jules-scratch/verification/verification.png')

        browser.close()

if __name__ == '__main__':
    run()
