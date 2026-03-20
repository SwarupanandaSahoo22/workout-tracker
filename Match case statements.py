# Match case statements: An alternative of using many 'elif' statements.
#                        Execute some codes if value matches the 'case'.
#                        Benfit: Cleaner and syntax is more readable.


# def is_weekend(day):
#     match day:
#         case "Sunday":
#             return True
#         case "Monday":
#             return False
#         case "Tuesday":
#             return False
#         case "Wednesday":
#             return False
#         case "Thursday":
#             return False
#         case "Friday":
#             return False
#         case "Saturday":
#             return True
#         case _:
#             return False
        

# print(is_weekend("Friday"))



def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(is_weekend("Thursday"))