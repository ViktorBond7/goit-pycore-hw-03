from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.15"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users: list[dict])-> list[dict]:
    result = []
    today = datetime.today().date()
    next_week = today + timedelta(days=7)

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо день народження вже минув цього року, переносимо його на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Якщо день народження випадає у наступний тиждень
        if today <= birthday_this_year <= next_week:
            weekday = birthday_this_year.weekday()
            if weekday == 6:
                birthday_this_year += timedelta(days=1)
            elif weekday == 5:
                birthday_this_year += timedelta(days=2)
            result.append({
                "name": user["name"],
                "birthday": birthday_this_year.strftime("%Y-%m-%d")
            })

    return result
       
   
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)



