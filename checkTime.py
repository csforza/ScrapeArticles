#!/usr/bin/python
from datetime import datetime, timedelta

TODAY = datetime.now().strftime("%d %b %Y")
ONE_DAY_AGO_DATE = (datetime.now() - timedelta(days=1)).strftime("%d %b %Y")
TWO_DAYS_AGO_DATE = (datetime.now() - timedelta(days=2)).strftime("%d %b %Y")


# returns false if article is up-to-date, true if not
def check_time(article_date):
    if TODAY in article_date:
        return False
    elif ONE_DAY_AGO_DATE in article_date:
        return False
    elif TWO_DAYS_AGO_DATE in article_date:
        return False
    else:
        return True
