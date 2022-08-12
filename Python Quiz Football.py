"""
Filename: Python Football Quiz
Author: Muhammad Tahir
Description: This is a football quiz designed to test your overall knoladge of the game.
"""

print("Welcome to my football quiz, you will be asked 10 multiple choice questions about the footballing world. Please enter the number next to your desired answer, Good Luck!")

Questions = ["1. Which team won the premier league in the 21/22 season?", "2. Which team has won the champions league the most amount of times?", "3. Which team has spent the most money in the past 10 years?", "4.Which team currently is in the most amount of debt","5. Who is currently the highest goal scorer in the world", "6. Who is currently the highest paid footballer in the world", "7. How many clubs has manager Jose Mourinho managed?", "8. Which manager has won the most amount of titles/trophies of all time?", "9. Which team has won the world cup the most amount of times?", "10. Who won the 2010 World Cup?"]
Answers = [1, 3, 2, 2, 1, 3, 1, 3, 2, 1]

for i in range(10):
    print(Questions[i])
    if i == 0:
        print("Answers: 1)Manchester City, 2)Macnhester United, 3)Liverpool")
    elif i == 1:
        print("Answers: 1)Manchester United, 2)Chelsea, 3)Real Madrid")
    elif i == 2:
        print("Answers: 1)Barcelona, 2)Manchester United, 3)Valencia")
    elif i == 3:
        print("Answers: 1)Tottenham, 2)Barcelona, 3)Bayern Mucich")
    elif i == 4:
        print("Answers: 1)Cristiano Ronaldo, 2)Lionel Messi, 3)Robert Lewangoalski")
    elif i == 5:
        print("Answers: 1)Sam Booth, 2)Neymar Junior, 3)Lionel Messi")
    elif i == 6:
        print("Answers: 1)Sam Booth, 2)Neymar Junior, 3)Lionel Messi")
    elif i == 7:
        print("Answers: 1)6 clubs, 2)4 clubs, 3)5 clubs")
    elif i == 8:
        print("Answers: 1)Jose Mourinho, 2)Pep Guardiola, 3)Sir Alex Ferguson")
    elif i == 9:
        print("Answers: 1)Austrailia, 2)Brazil, 3)England")
    elif i == 10:
        print("Answers: 1)Spain, 2)Brazil, 3)Portugal")
     

    validation = True
    while validation:
        user_answer= int(input("Enter the answer"))        
        if user_answer in range(1,3):
            if user_answer == Answers[i]:
                print("Correct Good Job")
                validation = False
            else:
                print("incorrect")
                validation = False
        else:
            print("Please enter a number between 1 and 3")
        
   
  
