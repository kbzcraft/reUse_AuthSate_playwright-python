import asyncio
from playwright.async_api import async_playwright

async def loginToGithub(playwright):
    print("hello")
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto('https://github.com/login')
    # Interact with login form
    await page.get_by_label("Username or email address").fill("username") #username
    await page.get_by_label("Password").fill("pass") #password
    await page.get_by_role("button", name="Sign in").click()
    # Continue with the test
    await context.storage_state(path=".auth/github.json")
    # ---------------------
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await loginToGithub(playwright)

# asyncio.run(main())
