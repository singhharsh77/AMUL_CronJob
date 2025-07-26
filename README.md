# Amul Stock Checker Bot

[![Amul Stock Checker](https://github.com/singhharsh77/AMUL_CronJob/actions/workflows/stock-check.yml/badge.svg)](https://github.com/singhharsh77/AMUL_CronJob/actions/workflows/stock-check.yml)

> Automatically monitors stock availability of popular Amul High Protein drinks and sends email alerts when they become available — no manual checking required!

---

## 🚀 Overview

This project is a **serverless stock monitoring bot** that repeatedly checks the availability of selected high-demand Amul products and notifies you by email when they are back in stock.

Due to frequent **out-of-stock** situations for these products on Amul’s official store, this bot helps you **never miss restocks** by automating the process.

---

## 📦 Products Monitored

- [Amul High Protein Plain Lassi (200 ml, Pack of 30)](https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30)  
- [Amul High Protein Buttermilk (200 ml, Pack of 30)](https://shop.amul.com/en/product/amul-high-protein-buttermilk-200-ml-or-pack-of-30)  
- [Amul High Protein Rose Lassi (200 ml, Pack of 30)](https://shop.amul.com/en/product/amul-high-protein-rose-lassi-200-ml-or-pack-of-30)

---

## ⚙️ Features

- Checks product stock status every 15 minutes, 24/7 (configurable via GitHub Actions cron job)  
- Sends instant email notifications when a product is available  
- Runs serverlessly using GitHub Actions—no need for personal servers or computer uptime  
- Secure credential storage via GitHub Secrets (email credentials are never exposed)  

---

## 📋 How It Works

1. **GitHub Actions Runner** triggers `main.py` every 15 minutes based on a cron schedule.  
2. The script fetches each product page and parses for “Add to Cart” availability.  
3. If any product is found in stock, an email notification is sent to your preferred email address.  
4. Logs and workflow results are available in GitHub Actions for troubleshooting and confirmation.  

---

## 🛠 Setup Guide

1. **Fork or clone** this repository.  
2. Add your Gmail credentials and email details as [GitHub repository secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets):  
   - `EMAIL_USERNAME` (your Gmail address)  
   - `EMAIL_PASSWORD` (your Gmail app password)  
   - `TO_EMAIL` (email where notifications are sent)  
3. Adjust the cron schedule in `.github/workflows/stock-check.yml` if needed to change frequency.  
4. Commit and push the changes.  
5. Monitor workflow runs under the **Actions** tab and check your email for notifications.

---

## ⚠️ Important Notes

- Use a **Gmail App Password** instead of your real Gmail password for secure authentication.  
- Be mindful of GitHub Actions usage limits; frequent runs can use your allotted free minutes.  
- This bot respects Amul’s website by checking at polite intervals (default 15 minutes). Avoid overly frequent polling.  

---

## 📧 Email Notification Example

You will receive an email like this when a product is detected in stock:

Subject: Amul Product In Stock!

The product is now in stock:
https://shop.amul.com/en/product/amul-high-protein-plain-lassi-200-ml-or-pack-of-30

text

---

## 🎉 Contribution & Support

Feel free to raise issues or pull requests to improve the bot! Whether it’s adding Telegram notifications, supporting more products, or enhancing robustness, your contributions are welcome.

---

## 📜 License

This project is open source under MIT License. See [LICENSE](LICENSE) for details.

---

## 📫 Contact

For questions or help setting it up, open an issue here or contact me on GitHub.

---

Happy shopping and never miss a restock! 🥳🥛🥤
