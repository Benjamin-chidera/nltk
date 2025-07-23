import re

result_search = re.search("pattern", r"string to contain the pattern")
# print(result_search)


result_search_2 = re.search("pattern", r"the phrase to find isn't in the string")

# print(result_search_2)

string = "sara was able to help me find the items i needed quickly"

new_string = re.sub("sara", "sarah", string)

# print(new_string)


customer_reviews = [
    "I absolutely loved this product! It exceeded my expectations and the quality is top-notch.",
    "Not satisfied at all. The item arrived late and was completely different from what I ordered.",
    "Decent experience overall. Customer service was responsive, but shipping took a bit longer than expected.",
    "Amazing! I’ve already recommended it to my friends. Totally worth the price.",
    "It works okay, but I’ve seen better for the same price. Wouldn’t buy it again.",
    "Fantastic value for money! Setup was easy and it performs exactly as described."
    "Sarah was very helpful and answered all my questions promptly.",
    "I had a great experience with Sarah. She was very knowledgeable and helpful.",
]

sarah_reviews = []

pattern_to_find = r"sarah?"

for string in customer_reviews:
    if re.search(pattern_to_find, string.lower()):
        sarah_reviews.append(string)

# print(sarah_reviews)    

a_reviews = []

pattern_to_find = r"^a"

for string in customer_reviews:
    if re.search(pattern_to_find, string.lower()):
        a_reviews.append(string)
# print(a_reviews)


pattern_to_find = r"y$"

end_y_reviews = []

for string in customer_reviews:
    if re.search(pattern_to_find, string.lower()):
        end_y_reviews.append(string)

print(end_y_reviews)