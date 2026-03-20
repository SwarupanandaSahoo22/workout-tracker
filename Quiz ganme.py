# # Quiz ganme

# questions = ("What is the capital of India?",
#             "Who is known as the Father of the Nation in India?",
#             "Which planet is known as the Red Planet?",
#             "How many continents are there in the world?",
#             "Which is the largest ocean in the world?")

# options = (("A. Kolkata", "B. Chennai", "C. Mumbai", "D. Delhi"), 
#            ("A. Netaji Subhas Chandra Bose", "B. Mahatma Gandhi", "C. Dr. Rajendra Prasad", "D. Pandit Jawahar Lal Nehru"),
#            ("A. Mars ", "B. Neptune", "C. Jupiter", "D. Mercury"), 
#            ("A. 8", "B. 7", "C. 9", "D. 10"), 
#            ("A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean"))

# answers = ("D", "B", "A", "B", "C")
# guesses = []
# score = 0
# ques_num = 0

# for question in questions:
#     print("--------------------")
#     print(question)
#     for option in options[ques_num]:
#         print(option)

#     guess = input("Enter (A, B, C, D): ").upper()
#     guesses.append(guess)

#     if guess == answers[ques_num]:
#         score += 1
#         print("CORRECT!(LFG🗿👌)")


#     else:
#         print("INCORRECT!(Never Give Up🤺)")
#         print(f"The correct answer of this question is: {answers[ques_num]}")
#     ques_num += 1

# print("--------------------")
# print("      RESULT🎉      ")
# print("--------------------")

# print(" Your guesses: ", end="")
# for guess in guesses:
#     print(guess, end=" ")

# print()

# print("Correct answers: ", end="")
# for answer in answers:
#     print(answer, end=" ")

# print()

# score = score / len(questions) * 100
# print(f"Your total score is: {score}%")

# if score >= 90:
#     print ("Giga chad FR!🗿")
# elif score >= 70:
#     print("Respect🫡")
# elif score >= 50:
#     print("Nice!👌")
# else:
#     print("Never Give Up!🤜🤛")















questions = ("Who wrote the Indian national anthem “Jana Gana Mana”?", 
            "Which is the smallest continent in the world?",
            "What is the currency of Japan?", 
            "Who was the first Prime Minister of India?", 
            "Which gas is most abundant in the Earth atmosphere?")

options = (("A. Dr. Rajendra Prasad", "B. Rabindranath Tagore", "C. Mahatma Gandhi", "D. Dr. B.R. Ambedkar"), 
           ("A. Australia", "B. Africa", "C. Antartica", "D. North America",), 
           ("A. Dollar", "B. Yen", "C. Euro", "D. Rubles",), 
           ("A. Mahatma Gandi", "B. Moti Lal Nehru", "C. Jawaharlal Nehru", "D. Subhas Chandra Bose",), 
           ("A. Oxygen", "B. Argon", "C. Carbon Dioxide", "D. Nitrogen",))

answers = ("B", "A", "B", "C", "D")

guesses = []
score = 0
ques_num = 0


for question in questions:
    print("-------------------------")
    print(question)
    for option in options[ques_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)

    if guess == answers[ques_num]:
        score += 1
        print("CORRECT!👍")
    else:
        print("INCORRECT!👎")
        print(f"The correct answers for this question is: {answers[ques_num]}")
    ques_num += 1



print("=" * 30)
print("\n RESULTS!🎉 \n")
print("=" * 30)

print("Your Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")

print()

print("Correct answers: ", end="")
for answer in answers:
    print(answer, end=" ")


print()

score = score / len(questions) * 100
print(f"Your toal score is: {score}%")

if score >= 90:
    print ("Giga chad FR!🗿")
elif score >= 70:
    print("Respect🫡")
elif score >= 50:
    print("Nice!👌")
else:
    print("Never Give Up!🤜🤛")