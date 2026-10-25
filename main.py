from datetime import datetime
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv("my_email")
password = os.getenv("password")


today = datetime.now()
today_tuple = (today.month, today.day)


data = pandas.read_csv("birthdays.csv")
matches = data[(data["month"] == today_tuple[0]) & (data["day"] == today_tuple[1])]

if not matches.empty:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        for _, person in matches.iterrows():
            template_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
            with open(template_path) as letter_file:
                contents = letter_file.read()
                contents = contents.replace("[NAME]", person["name"])

            connection.sendmail(
                from_addr=my_email,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}"
            )
