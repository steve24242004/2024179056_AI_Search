import json
import re
import os

# Load knowledge base
with open("hotel_kb.json", "r") as f:
    kb = json.load(f)

# Check if user data exists
user_file = "user_data.json"
if os.path.exists(user_file):
    with open(user_file, "r") as f:
        user_data = json.load(f)
    user_name = user_data.get("name", "")
else:
    user_data = {}
    user_name = ""

# Greet user
if user_name:
    print(f"Bot: Welcome back, {user_name}! How can I help you today?")
else:
    user_name = input("Bot: Hello! May I know your name? You: ").strip()
    if user_name:
        user_data["name"] = user_name
        with open(user_file, "w") as f:
            json.dump(user_data, f)
    print(f"Bot: Nice to meet you, {user_name}! How can I assist you today?")

# Main chat loop
while True:
    user_input = input("You: ").lower().strip()

    if not user_input:
        print("Bot: Please type something so I can assist you.")
        continue

    if re.search(r"\b(bye|exit|quit)\b", user_input):
        print("Bot:", kb["bye"])
        break

    elif re.search(r"\b(thank|thanks)\b", user_input):
        print(f"Bot: {kb['thanks']}")

    elif re.search(r"check|time|timing|open|close", user_input):
        print("Bot:", kb["timings"])

    elif re.search(r"room|suite|accommodation", user_input):
        print("Bot:", kb["rooms"])

    elif re.search(r"book|reserve|booking|stay", user_input):
        print("Bot:", kb["booking"])

    elif re.search(r"cancel|cancellation", user_input):
        print("Bot:", kb["cancel"])

    elif re.search(r"contact|phone|email", user_input):
        print("Bot:", kb["contact"])

    elif re.search(r"location|address|where", user_input):
        print("Bot:", kb["location"])

    else:
        print("Bot:", kb["fallback"])
