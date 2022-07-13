"""
In this project, you will create a flashcard application that you can use to quiz
yourself on academics, an interesting topic, or have a trivia competition with friends!

Lines starting with # TODO:
are instructions for what you have to fill out.
Many of these are left empty with a `pass`.
Once you finish the code for the TODO,
delete the `pass` statement.

The flashcards are read from the file `flashcards.csv`.
A csv (comma separated values) file has lines of values separated by commas.
In this case, the format is: question,answer,difficulty.
Take a look at the sample questions in the file to see this.
"""


class Flashcard:
    """
    The Flashcard class has the data for one question-answer pair.
    A flashcard also has a difficulty (easy, medium, hard).
    """

    def __init__(self, question, answer, difficulty):
        # TODO: create attributes of the Flashcard class using `self`.
        # Set the attributes equal to the three parameters
        self.question = question
        self.answer = answer
        self.difficulty = difficulty

    def __str__(self):
        return "%s %s %s" % (self.question, self.answer, self.difficulty)


class Game:
    """
    The game class reads the flashcards from the file `flashcards.csv`,
    asks those questions to the user, and gives them feedback on how they answered.
    """

    def __init__(self):
        """
        The constructor reads the flashcards from the csv and stores them in a list of Flashcard objects
        """

        # Flashcards is a list of type Flashcard
        self.flashcards = []

        # List of each line in the file
        lines = []
        # Open the csv file with the variable `file`
        with open("flashcards.csv") as file:
            # TODO: read the lines of the file into the `lines` list using `file.read().splitlines()`
            lines = file.read().splitlines()

        # Iterate over each line, creating a Flashcard object from each one
        for line in lines:
            # TODO: split `line` by commas and store the result in `words`
            # To split a string `s` by a comma, you would use `s.split(',')`
            words = line.split(',')

            # TODO: now, create a `flashcard` object using the elements in the `words` list.
            # Remember that the words are in the order: question, answer, difficulty
            flashcard = Flashcard(words[0], words[1], words[2])

            # TODO: append the newly created flashcard to `self.flashcards`
            self.flashcards.append(flashcard)

    def play(self):
        """
        The play method asks the user the flashcard questions and gives them feedback on how they did
        """

        # Count of questions the user got correct
        correct = 0

        # TODO: ask the user what difficulty of questions they would like to answer using the `input()` function
        difficulty = input("Enter question difficulty: ")

        # TODO: filter the flashcards for the flashcards that have the difficulty the user asked for.
        # Call the filter() function, passing in a lamda checking if the given flashcard's difficulty is this one
        # Remember that you have to cast the result of `filter()` to a list using `list()`.
        # When comparing the strings, convert them to lower case to handle differences in capitalization
        # using the `lower()` method
        self.flashcards = list(filter(lambda flashcard: flashcard.difficulty.lower() == difficulty.lower(), self.flashcards))

        # Iterate over the flashcards
        for flashcard in self.flashcards:
            # TODO: print the question and ask the user for an answer using `input()`
            user_answer = input(flashcard.question + " ")

            # TODO: compare `user_answer` with the actual answer of the flashcard,
            # and print whether they got the question right. If they were wrong,
            # print the correct answer so they can learn for next time.
            # TODO: update the `correct` variable based on if they got the question correct
            if user_answer.lower() == flashcard.answer.lower():
                correct += 1
                print("Correct!")
            else:
                print("Incorrect, the correct answer was:", flashcard.answer)

        # TODO: print how many questions they got correct, and the total number that they answered
        print("You got", correct, "out of", len(self.flashcards), "questions correct!")


def main():
    # TODO: create a Game object and play it
    game = Game()
    game.play()

    # TODO: now that you've finished the code, make some flashcards and put them in the csv!
    # They can be on any topic you're interested in. Remember, the format is: question,answer,difficulty

    # TODO: Got everything working and looking for a challenge?
    # Here are some ideas:
    #    - In the play method, shuffle the flashcards using the `random.shuffle()` function in the random package
    #    - In the play method, allow the user to enter "any" for a difficulty,
    #      and in that case don't filter the flashcards
    #    - Using a while loop in the main method, after a game is played,
    #      ask the user if they want to continue and if they do, start a new game


# Runs the main
if __name__ == "__main__":
    main()
