# 🛡️ YooTube Phishing Keylogger (Educational Demo)

This project is a **local, lab-only phishing simulation** that mimics a YouTube login page using typosquatting and a keylogger to demonstrate common red team techniques. It is intended for **educational and cybersecurity training purposes only**.

> ⚠️ **DISCLAIMER**: This tool is for ethical use only in controlled environments such as CTFs, labs, or red team exercises with proper authorization. Do NOT use this to target anyone without their informed consent — doing so may violate laws such as the Computer Fraud and Abuse Act (CFAA).

---

## 🚀 Features

- 🔐 Fake login form that captures:
  - Email
  - Password
  - IP address
- 🖱️ JavaScript keylogger that logs all keystrokes in real-time
- 🖼️ Background screenshot mimicking real YouTube homepage
- 🔁 Redirects to real YouTube after "login"
- 💾 Logs credentials and keystrokes locally

---

## 🗂️ File Structure
  - flask.py
  - static/
  -   background.png
  -   templates/
  -     index.html
  - creds.txt
  - web_keylog.txt

🛡️ Educational Goals
- Teach how typosquatting + phishing attacks are executed
- Demonstrate common pitfalls users face (auto-login, form spoofing)
- Prepare blue teams to recognize and defend against credential harvesting techniques
