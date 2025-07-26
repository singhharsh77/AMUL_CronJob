import os
import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URLS = [
    "https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30",
    "https://shop.amul.com/en/product/amul-high-protein-buttermilk-200-ml-or-pack-of-30",
    "https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30"
]

EMAIL_USERNAME = os.environ['EMAIL_USERNAME']
EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']
TO_EMAIL = os.environ['TO_EMAIL']

def check_stock(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        return "add to cart" in soup.text.lower()
    except Exception:
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
