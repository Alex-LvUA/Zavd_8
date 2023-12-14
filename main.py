from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    result = dict()
    b_Monday = []
    b_Tuesday = []
    b_Wednesday = []
    b_Thursday = []
    b_Friday = []

    weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weeks_b = [b_Monday, b_Tuesday, b_Wednesday, b_Thursday, b_Friday]

    def write_result(day):
        i = weeks.index(day)
        i = 0 if i > 4 else i
        n = 0
        for n in range(5):
            if len(weeks_b[i])>0:
                result[weeks[i]] = weeks_b[i] #запис словника
            n += 1
            i += 1
            i = 0 if i > 4 else i
        return result

    def select_users(date,user):
        if date.strftime("%A") == "Tuesday":
            b_Tuesday.append(user["name"])
        elif date.strftime("%A") == "Wednesday":
            b_Wednesday.append(user["name"])
        elif date.strftime("%A") == "Thursday":
            b_Thursday.append(user["name"])
        elif date.strftime("%A") == "Friday":
            b_Friday.append(user["name"])
        else:
            b_Monday.append(user["name"])

    for user in users:
        date_w = datetime(date.today().year, user["birthday"].month, user["birthday"].day).date()  # Дні народженні в цьому році
        if date.today().day>=26 and date_w.month==1:
            date_w=datetime(date.today().year+1, user["birthday"].month, user["birthday"].day).date()
        after_weeks = timedelta(days=6)
        before_monday = timedelta(days=2)
        after_monday = timedelta(days=4)
        date_after_week=date.today()+after_weeks
        date_before_monday = date.today() - before_monday
        date_after_monday = date.today() + after_monday

        if date.today().strftime("%A")=="Monday":
            if date_before_monday <= date_w <= date_after_monday:
                select_users(date_w, user)
        elif date.today()<=date_w<=date_after_week:
            select_users(date_w, user)

    result = write_result(date.today().strftime("%A"))
    return result


if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Keanu Reeves", "birthday": datetime(1964, 9, 2).date()},
        {"name": "Nicole Kidman", "birthday": datetime(1967, 6, 20).date()},
        {"name": "Milla Jovovich", "birthday": datetime(1975, 12, 17).date()},
        {"name": "Michael Kirk Douglas", "birthday": datetime(1944, 9, 25).date()},
        {"name": "Salvador Dalí", "birthday": datetime(1904, 5, 11).date()},
        {"name": "Ludwig van Beethoven", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Stephen Hawking", "birthday": datetime(1942, 1, 8).date()},
        {"name": "Michael Faraday", "birthday": datetime(1867, 8, 25).date()},
        {"name": "Олександр Смакула", "birthday": datetime(1900, 9, 9).date()},
        {"name": "Bill Gates2", "birthday": datetime(1955, 10, 29).date()},
        {"name": "Keanu Reeves2", "birthday": datetime(1964, 12, 12).date()},
        {"name": "Nicole Kidman2", "birthday": datetime(1967, 12, 13).date()},
        {"name": "Milla Jovovich2", "birthday": datetime(1975, 12, 18).date()},
        {"name": "Michael Kirk Douglas2", "birthday": datetime(1944, 12, 9).date()},
        {"name": "Salvador Dalí2", "birthday": datetime(1904, 5, 12).date()},
        {"name": "Ludwig van Beethoven2", "birthday": datetime(1955, 10, 29).date()},
        {"name": "Stephen Hawking2", "birthday": datetime(1942, 12, 10).date()},
        {"name": "Michael Faraday2", "birthday": datetime(1867, 8, 26).date()},
        {"name": "Олександр Смакула2", "birthday": datetime(1900, 9, 10).date()},
        {"name": "Bill Gates3", "birthday": datetime(1955, 10, 26).date()},
        {"name": "Keanu Reeves3", "birthday": datetime(1964, 12, 30).date()},
        {"name": "Nicole Kidman3", "birthday": datetime(1967, 1, 1).date()},
        {"name": "Milla Jovovich3", "birthday": datetime(1975, 1, 3).date()},
        {"name": "Michael Kirk Douglas3", "birthday": datetime(1944, 9, 21).date()},
        {"name": "Salvador Dalí3", "birthday": datetime(1904, 5, 9).date()},
        {"name": "Ludwig van Beethoven3", "birthday": datetime(1955, 10, 25).date()},
        {"name": "Stephen Hawking3", "birthday": datetime(1942, 1, 4).date()},
        {"name": "Michael Faraday3", "birthday": datetime(1867, 8, 21).date()},
        {"name": "Олександр Смакула3", "birthday": datetime(1900, 9, 6).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
