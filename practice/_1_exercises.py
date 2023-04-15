# with open("sample.txt") as file:
#     text = file.read()
# words = text.split()
# for word in words:
#     index = word.find("el")
    # if index != -1:
    #     print(index)
        # print(word)


# current_year = 2023
# born_year = input("Which year you were born? ")


# time_in_world = current_year - int(born_year)


# print(time_in_world)




# age = (current_year) - int(born_year)
# print(age)




from datetime import datetime

# We get the seconds of now to as precise as possible
now_seconds = datetime.now().timestamp()

#we ask the date
birthday = input("Birthday in YYYY-MM-DD? ")

# We get the seconds of the user date to as precise as possible
birthday_seconds = datetime.strptime(birthday, "%Y-%m-%d").timestamp()

# we create a new date from the result of subtracting the two variables with  the seconds on them
print(datetime.fromtimestamp(now_seconds - birthday_seconds))




# date_str = "2023/04/04"
# datetime_obj = datetime.strptime(date_str, "%Y/%m/%d")
# print(datetime_obj)
# today = datetime.today().date()
# print(today)
# date_obj = datetime_obj.date()

# print(today - date_obj)


























































# from collections import Counter

# with open("sample.txt") as file:
#     text = file.read().lower()
# words = text.split()
# word_counts = Counter(words)
# top_ten = word_counts.most_common(10)
# for word, count in top_ten:
#     print(f"{word}: {count}")