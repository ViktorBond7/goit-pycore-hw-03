from datetime import datetime

def get_days_from_today(date: str)->int:
    target_date = datetime.strptime(date, "%Y-%m-%d")
    time_now = datetime.now()
    result= (time_now - target_date).days
    return result

print(get_days_from_today("2025-02-09"))

