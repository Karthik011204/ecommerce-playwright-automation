import os

ENV = os.getenv("ENV", "qa")

if ENV == "qa":
    BASE_URL = "https://demowebshop.tricentis.com/"
else:
    BASE_URL = "https://demowebshop.tricentis.com/"

EMAIL = os.getenv("EMAIL", "existinguser@gmail.com")
PASSWORD = os.getenv("PASSWORD", "Test@123")

HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
BROWSER_NAME = os.getenv("BROWSER", "chromium")
