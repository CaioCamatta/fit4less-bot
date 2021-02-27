# Fit4Less Bot

## Instructions

1. Clone repository
2. Create virtualenv `virtualenv venv` and activate it `source venv/bin/activate`
3. Install packages `pip install -r requirements.txt`
4. Setup .env with your information
5. Run the program `python bot.py`

Based on `chakrakan`'s bot. Modified by Caio C. Coelho.

### Environment File

Your `.env` file should live in the root of the program (same level as `bot.py`), and should look like this:

```
EMAIL="email@email.com"
PASSWORD="mypassword"
BOOKING_DAYS_FROM_NOW=2
TIME="11:00 AM"
FIT4LESS_LOGIN_URL="https://myfit4less.gymmanager.com/portal/login.asp"
```
