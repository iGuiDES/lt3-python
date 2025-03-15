# Task 1
upper_user_input = input("Type your sentence: ")
print(upper_user_input.upper())


# Task 2
replace_user_input = input("Type your sentence: ")
if "a" not in replace_user_input:
    print("letter 'a' not found")
else:
    print(replace_user_input.replace("a", "*"))


# Task 3
len_user_input = input("Type your sentence: ")
print(len(len_user_input))


# Other tasks
# Task 4
user_plain_text = input("Type your sentence: ")
user_control_word = input("Type your control word: ")

print(user_plain_text.lower().count(user_control_word.lower()))


# Task 5
url_list = ["https://prodtea.com.ua", "https://prod_dim.com.ua"]
for url in url_list:
    print(url.replace("prod", "qa"))