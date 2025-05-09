import random
import MinjurSubba_02240084_A2_PB

class Games:
    def __init__(self):
        self.overall_score = 0
        
        '''This will store the overall Score'''
        

    def main_menu(self):
        print("welcome!! Choose the game of your liking!")
        print("1. Guessing Game")
        print("2. Rock, Paper, and Scissors")
        print("3. Trivia Persuit Game")
        print("4.Pokemon card binder")
        print("5. overall scoring System")
        print("0. Exit")
        
    def run(self):
        while True:
            self.main_menu()
            try:
                user_input = int(input("Please choose a number from 0 to 5: "))
                if user_input == 1:
                    self.guessing_game()
                elif user_input == 2:
                    self.rock_paper_scissor()
                elif user_input == 3:
                    self.trivia_quiz_game()
                elif user_input == 4:
                    partB = MinjurSubba_02240084_A2_PB.PokemonCardBinderManager()
                    partB.run()  
                elif user_input == 5:
                    print(f"Your Overall Score so far is: {self.overall_score} points!")
                elif user_input == 0:
                    print("i hope you enjoyed")
                    break
                else:
                    print("That is not an option, buddy!")
            except ValueError:
                print("Please enter a valid number, buddy!")
  
        '''This loop is used to call specific functions according to the users input. if the user chooses one
  it will call on the gussing game function. And if the uer wants to exit, it will type 3 and break the loop
   and end the program.'''
    
        
        

    def guessing_game(self):
        while True:
            print("You chose Guessing Game!")
            guessing_number = random.randint(1, 40)
            attempt = 0

            print("Guess the number! (from 1 to 40)")

            while True:
                try:
                    user_guess = int(input("What number did you guess? "))
                    attempt += 1
                    difference = abs(guessing_number - user_guess)

                    if guessing_number == user_guess:
                        self.overall_score += 5
                        print(f"Congrats man! You are right! You guessed it in {attempt} attempts!")
                        break
                    elif difference <= 2:
                        print("Woah! You are about to reach the number!")
                    elif difference <= 8:
                        print("Quite near buddy. Try guessing again!")
                    elif user_guess > guessing_number:
                        print("Too high, try guessing lower!")
                    else:
                        print("Too low, try guessing higher!")

                except ValueError:
                    print("Number buddy, enter a number!")

            play_again = input("do you want to play again? (Yes/No): ").lower()
            if play_again != "yes":
                break
 
    '''this function represents the gussing game. what it does here is, first i gave a range of number
 (from 1-40) and then by using random prompt, i made the program choose a random number from
 1 to 40, then i made a variable to find the difference of the two, input of the user and the random number
 by the program. then by usong if statement i made conditions such that the user csn guess for the number as
 described above'''

 
 
    def rock_paper_scissor(self):
        while True:
            print("You chose to play Rock, Paper, and Scissors!")

            computer_choices = ["rock", "paper", "scissors"]
            for_computer = random.choice(computer_choices)

            user_choice = input("Choose: Rock, Paper, or Scissors? ").lower()

            if user_choice not in computer_choices:
                print("Please choose a valid option (Rock, Paper, or Scissors).")
                continue

            print(f"Computer chose: {for_computer}")

            if user_choice == for_computer:
                print("It's a tie!!")
            elif for_computer == "rock" and user_choice == "paper":
                print("YOU WON!")
                self.overall_score +=5
            elif for_computer == "paper" and user_choice == "scissors":
                print("YOU WON!")
                self.overall_score +=5
            elif for_computer == "scissors" and user_choice == "rock":
                self.overall_score += 5
                print("YOU WON!")
            else:
                print("Sorry, but you lost!")

            play_again = input("do you want to play again? (Yes/No): ").lower()
            if play_again != "yes":
                break
            
            
    '''This function is for rock, paper and scissor game. at first, by using the random prompt,
    i made the program randomly choose from the three. then made the user input his choice from the three.
    then by using conditional loops, i made some statements for the user to win as mentioned above.
    and when they do win, they get an overall score of five points tha will be stored in the overall scorer'''      
            
            
            

    def trivia_quiz_game(self):
        print("You chose the Trivia Pursuit Quiz Game!")

        while True:
            score = 0
            print("Pick a category:")
            print("1. Science")
            print("2. History")
            print("3. Engineering")

            category = input("Choose a category from 1 to 3: ")

            if category == "1":
                print("you chose Science! SO HERE IS YOUR QUESTION !")
                print("Question One: Why do Humans have eyebrows?")
                print("A.To raise it when you are in trouble.")
                print("B. To prevent sweat from ATTACKING OUR EYES!!!")
                print("C. For beauty purposes")
                print("D. Maybe so that akiens can recognise us better")
                answer1 = input("Your answer: ").lower()
                if answer1 == "b":
                    print("Correct!")
                    score += 1
                else:
                    print("sorry mate. the correct answer was, B. To prevent sweat from ATTACKING OUR EYES!!!")

                print("Q2: Which part of your body can glow in dark, But you cannot see it?")
                print("A.Eyes, if you have a cat eye.")
                print("B. Belly buttons in full moon")
                print("C. Teeths, under UV light(Spooky)")
                print("D. Skin , if you are light skinned?")
                answer2 = input("Your answer: ").lower()
                if answer2 == "c":
                    print("Correct!")
                    score += 1
                else:
                    print("Oops! The correct answer was, C.Teeths, under UV light(Spooky)")

            elif category == "2":
                print("you chose HISTORY! SO HERE IS YOUR QUESTION !")
                print("Q1: Wha did bhutan do in 2016 to protect the enviroment?")
                print("A. Trained Monks to recycle")
                print("B. Planted 100,000 Trees")
                print("C. Educated Highlanders on Recycling")
                print("D. Reduced intake of Tourists")
                answer1 = input("Your answer: ").lower()
                if answer1 == "b":
                    print("Correct!")
                    score += 1
                else:
                    print("Nope! Correct answer was B. Planted 100,000 Trees")

                print("Q2: What was Napoleons actual height?")
                print("A) 3 feet tall, basically a hobbit general ")
                print("B) 6 foot 4 inches but only when wearing heels")
                print("C) Average height, but he had short temper syndrome")
                print("D) Taller than his horse.")
                answer2 = input("Your answer: ").lower()
                if answer2 == "c":
                    print("Correct!")
                    score += 1
                else:
                    print("Nope! It was C) Average height, but he had short temper syndrome. Rude, honestly")

            elif category == "3":
                print("you chose ENGINEERING! SO HERE IS YOUR QUESTION !")
                print("Q1. Why don't engineers sleep during Sem End?")
                print("A) Because They love the caffeine drive")
                print("B) Because circuit diagrams visit them in their dreams to haunt them")
                print("C) Because if they close their eyes, the Kirchhoff laws will vanish")
                print("D) All of the above, plus emotional damage")
                answer1 = input("Your answer: ").lower()
                if answer1 == "d":
                    print("Correct!")
                    score += 1
                else:
                    print("Incorrect! Answer was, D. (Engineering = caffeine + anxiety + a little spark of hope)")

                print("Q2. What does an engineer usually say when a prototype catches fire?")
                print("A) It's not a failure, it's a feature")
                print("B) We are just, testing if it is fireproof")
                print("C) Okay... so we will not do that again")
                print("D) All of the above while casually sipping cold tea")
                answer2 = input("Your answer: ").lower()
                if answer2 == "d":
                    print("Correct!")
                    score += 1
                else:
                    print("well um it was D. Prototypes always BURN the first few times (engineering tradition)")

            else:
                print("come on man, choose from the given option")
                continue

            self.overall_score += score
            print(f"Your final score is {score}!")

            play_again = input("Wanna try another category? (Yes/No): ").lower()
            if play_again != "yes":
                print("ok then, i will see you again soon")
                break

    
    '''This is a function for trivia games whereby i made two question for three categories. Whenever player 
 says the correct answer, they get one point and it gets added up and at the last they get the total score.'''


game = Games()
game.run()


'''calling the class for smooth running'''