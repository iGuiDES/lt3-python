# Task 1
upper_user_input: str = input("Type your sentence: ").upper()
print(upper_user_input)

# Task 2
replace_user_input: str = input("Type your sentence: ")
result_rui: str = ""

if "a" in replace_user_input.lower():
    result_rui = replace_user_input.lower().replace("a", "*")
    print(result_rui)
elif "а" in replace_user_input.lower():
    result_rui = replace_user_input.lower().replace("а", "*")
    print(result_rui)
else:
    print("Letter 'a' is not define")

# Task 3
len_user_input: str = input("Type your sentence: ")
result_lui: int = len(len_user_input)
print(result_lui)

# Other tasks
# Task 4
user_plain_text: str = input("Type your sentence: ")
user_control_word: str = input("Type your control word: ")

result_check_word: int = user_plain_text.lower().count(user_control_word.lower())
print(result_check_word)

# Task 5
url_list: list = ["https://prodtea.com.ua", "https://prod_dim.com.ua"]
for url in url_list:
    print(url.replace("prod", "qa"))
