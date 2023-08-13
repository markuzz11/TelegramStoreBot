# Telegram Shop Bot

**Telegram bot with Django Administration**

---

## Description

This repository provides a simple template for creating a Telegram bot tailored for shopping purposes. The project utilizes the `telebot` and `django` packages.

## Comments

A table with goods has already been added here but everything else is up to you

Almost all of directories and packages is making automatically with creating django app. I added `tgbot` part and `setupDjangoORM` for connect django orm with tgbot

## Usage and Installation

1. **Create Telegram Bot:**
    - Begin by creating a bot on Telegram using the **@BotFather**.
    - Create a file named `tgtoken.py` and assign your bot token value to a variable within this file.

2. **Setup Django Project:**
    - Create a Django project on your local machine.
    - Generate a `secretkey.py` file and set the `SECRET_KEY` value (as seen in `settings.py`) within this file.

3. **Run Django Server:**
    - To launch the Django server, open your terminal and execute: `python manage.py runserver`.

4. **Run Telegram Bot:**
    - To utilize the Telegram bot, run the `main.py` script in the `tgbot` directory.

