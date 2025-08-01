import os
import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URLS = [
    "https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30",
    "https://shop.amul.com/en/product/amul-high-protein-buttermilk-200-ml-or-pack-of-30",
    "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"
    "https://shop.amul.com/en/product/amul-high-protein-paneer-400-g-or-pack-of-24",
    "https://shop.amul.com/en/product/amul-high-protein-paneer-400-g-or-pack-of-2",
    "https://shop.amul.com/en/product/amul-high-protein-milk-250-ml-or-pack-of-8"
]

EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
TO_EMAIL = os.environ['TO_EMAIL']

headers = {'User-Agent': 'Mozilla/5.0'}

def check_stock(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Save the HTML content to inspect the button visually
        with open("page.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())

        # Search for a button that contains 'Add to Cart'
        add_to_cart_button = soup.find("button", string=lambda s: s and "add to cart" in s.lower())
        
        return add_to_cart_button is not None
    except Exception as e:
        print(f"Error checking {url}: {e}")
        return False

def send_email(product_url):
    subject = "Amul Product In Stock!"
    body = f"The product is now in stock:\n{product_url}"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_USERNAME, TO_EMAIL, message)

for url in PRODUCT_URLS:
    if check_stock(url):
        send_email(url)

print("Username:", EMAIL_USERNAME)
print("To:", TO_EMAIL)
