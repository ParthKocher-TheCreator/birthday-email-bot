# 🎂 Birthday Wisher Automation

An automated Python script that checks for birthdays in a CSV database each day and sends a personalized, randomly selected birthday email via SMTP using Gmail.

---

## ✨ Features

- **Automated Matching:** Compares today's date against a list of contacts.
- **Dynamic Templates:** Picks a random letter template and customizes it with the recipient's name.
- **Secure Credentials:** Keeps email credentials private using environment variables (`.env`).
- **Batch Delivery:** Capable of sending emails to multiple contacts sharing the same birthday.

---

## 📁 Project Structure

```text
├── letter_templates/       # Text templates containing [NAME] placeholders
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
├── .env.example            # Environment variable template
├── .gitignore              # Files to ignore (e.g., .env, .idea/)
├── birthdays.csv           # Contact list (name, email, year, month, day)
├── main.py                 # Core automation script
└── README.md
