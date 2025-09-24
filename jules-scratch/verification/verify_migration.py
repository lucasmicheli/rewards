from playwright.sync_api import Page, expect
import logging

logging.basicConfig(level=logging.INFO)

def test_homepage(page: Page):
    """
    This test verifies that the homepage loads correctly.
    """
    try:
        logging.info("Navigating to http://localhost:3000")
        page.goto("http://localhost:3000")
        logging.info("Navigation complete.")

        logging.info("Page content:")
        print(page.content())

        logging.info("Looking for heading 'Electronics'")
        heading = page.get_by_role("heading", name="Electronics")
        expect(heading).to_be_visible()
        logging.info("Heading found and visible.")

        screenshot_path = "jules-scratch/verification/verification.png"
        logging.info(f"Taking screenshot to {screenshot_path}")
        page.screenshot(path=screenshot_path)
        logging.info("Screenshot taken.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        # Re-raise the exception to fail the test
        raise
