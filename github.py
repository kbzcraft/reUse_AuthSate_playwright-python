import asyncio
from playwright.async_api import async_playwright

async def run(playwright):
    browser = await playwright.chromium.launch(headless=False)
    while True:
        try:
            context = await browser.new_context(storage_state=".auth/github.json")
            print("login sucessfull")
            break
        except:
            print("log in from start")
            from loginGithub import loginToGithub
            async with async_playwright() as playwright:
                await loginToGithub(playwright)
            continue
    page = await context.new_page()
    await page.goto('https://github.com/login')
    #  Do what ever you want .....
    
    # searchBtnXpath ="//html/body/div[1]/div[1]/header/div/div[2]/div[1]/qbsearch-input/div[1]/div[1]/div/div/button"
    # searchInputAreaXpath="//html/body/div[1]/div[1]/header/div/div[2]/div[1]/qbsearch-input/div[1]/div[2]/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input"
    # searchBtn = page.locator(f'xpath={searchBtnXpath}')
    # await searchBtn.click() 
    # searchInputArea = page.locator(f'xpath={searchInputAreaXpath}')
    # q = input()
    # await searchInputArea.type(q)
    # await searchInputArea.press("Enter")

    # input()
    # ---------------------
    await context.close()
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
