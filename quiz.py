import random
import questions as ques

class Quiz():
    def __init__(self):
        self.quiz = ques.Questions().quiz
        self.score = 0

    def start_quiz(self):

        for i in self.quiz:
            print("===#===#===#===")
            #print the questions
            print(self.quiz[i]['question'])

            #print the options
            print(self.quiz[i]['options'])

            #input the answer
            ans = input('please enter the correct option(a,b,c,d): ').lower()
            if ans == self.quiz[i]['answer']: self.score += 1

        print("===#===#===#===")
        print(f"your score is: {self.score}/{len(self.quiz)}")
            

game = Quiz()
game.start_quiz()