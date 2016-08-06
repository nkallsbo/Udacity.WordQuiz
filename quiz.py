# Sentences to fill in the blanks for
easy_strings = ("The current Presidents last name is __1__. "
                "He's wifes first name is __2__. "
                "They live in the __3__ __4__ in __5__ DC.")

medium_strings = ("HTML is short for __1__ __2__ __3__. "
                  "A markup language is a set of markup __4__. "
                  "Each HTML tag describes different __5__ content.")

hard_strings = ("__1__ is a programming __2__ that lets you work quickly "
                "and integrate __3__ more effectively. __4__ also known a "
                "arrays in other languages" "are one of the compound __5__ "
                "types that Python understands.")


# Lists of replacement words for each level
easy_parts_of_speech = ["Obama", "Michelle", "White", "House", "Washington"]
medium_parts_of_speech = ["HyperText", "Markup", "Language", "tags", "document"]
hard_parts_of_speech = ["Python", "language", "systems", "Lists", "data"]
    

# Play game
# quiz_string = string to fill in the blanks
# correct_answers = The correct strings/ answers
def quiz_game(quiz_string, correct_answers):
    """
    Plays the game
    :param quiz_string: string to fill in the blanks
    :param correct_answers: The correct strings/ answers
    :return: None
    """
    points = 0
    start_position = 1
    end_position = 6
    maximum_rounds = 5

    print quiz_string
    # Loop to type in words on each missing number
    for i in range(start_position, end_position):
        for j in range(start_position, end_position):
            user_input = raw_input("What is the answer to blank __%d__? " % (i))
            
            if user_input == correct_answers[i-1]:
                # Replace words in the strings
                quiz_string = quiz_string.replace("__%d__" % (i), user_input)
                points = points + 1
                print quiz_string
                break
            elif j == maximum_rounds:
                print "Game Over! You Loose! You got %d points!" % (points)
                return # Five faults in a row, game is over.
            else:
                print "Incorrect, try again"             

    print "You won! You are awesome! You got %d / 5 points!" % (points)

print ("Welcome to this Quiz Game!"
       "Choose difficulty by typing in Easy, Medium or Hard")

print ("RULES: You have to spell it right, even with capital letters!"
       "If it is a name or a city,"
       "you should write it with a uppercase letter!")
print

def select_difficulty():
    # User chooses difficulty by typing it in
    user_difficulty = raw_input("Type in difficulty here: ").lower()
    
    # Game starts depending on the level.
    if user_difficulty == "easy":
        quiz_game(easy_strings, easy_parts_of_speech)

    if user_difficulty == "medium":
        quiz_game(medium_strings, medium_parts_of_speech)

    if user_difficulty == "hard":
        quiz_game(hard_strings, hard_parts_of_speech)

select_difficulty()
    

