# askYear = input("Please enter a year (YYYY): ")
# askMonth = input("Please enter a month (MM): ")
# askDay = input("Please enter a day (DD): ")

user_date = input("Please enter a date in the format YYYY-MM-DD: ")

day = user_date[8:]
month = user_date[5:7]
year1 = user_date[:2]
year2 = int(user_date[2:4])
year = float(user_date[:4])

month_codes = {
    "01": 4, "02": 0, "03": 0, "04": 3, "05": 5, "06": 1, "07": 3, "08": 6, "09": 2, "10": 4, "11": 0, "12": 2
}

year1_codes = {
    "16": 0, "17": 5, "18": 3, "19": 1, "20": 0, "21": 5, "22": 3
}

year2Math = (year2) % 4
year1Math = int(year1) % 4

part1Math = year2 // 4
part2Math = int(year1_codes[year1]) + int(month_codes[month]) + int(day) + part1Math + 2 + year2
part3Math = (part2Math) % 7

if year1Math == 0:
    if year2Math == 0:
        if month == "01" or month == "02":
            part3Math -= 1
        else:
            pass
    else:
        pass

# elif year1Math == 0:
#     if month == "01" or month == "02":
#         part3Math
#     else: 
#         pass
else:
    pass

weekDays = {
    6: "Saturday",
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday"
}

print(weekDays[part3Math])

