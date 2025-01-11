import random
import questions as ques

class Quiz():
    def __init__(self):
        self.quiz = ques.Questions().quiz
        self.score = 0
        self.wrong_ans = []

    def start_quiz(self):

        for i in self.quiz:
            print("===#===#===#===")
            #print the questions
            print(self.quiz[i]['question'])

            #print the options
            print(self.quiz[i]['options'])

            #input the answer
            while(True):
                try:
                    ans = input('please enter the correct option(a,b,c,d): ').lower()
                    if ans not in ('a','b','c','d'):
                        raise ValueError("incorrect value")
                    else:
                        if ans == self.quiz[i]['answer']:
                            self.score += 1
                        else: 
                            self.wrong_ans.append(i)
                        print("===#===#===#===")
                        break
                except ValueError as e:
                    print("===#===#===#===")
                    print(f"error: {e}")
                    print(f"please enter a legal answer: (a,b,c,d)")
                    print("===#===#===#===")
                    print(self.quiz[i]['question'])
                    print(self.quiz[i]['options'])

        print("===#===#===#===")
        print("TEST FINISHED")
        print("===#===#===#===")

        if self.score != len(self.quiz):
            print(f"the questions you attempted wrong are:".upper())
            for i in self.wrong_ans:
                print(self.quiz[i]['question'])
                print(self.quiz[i]['options'])
                print("correct ans: " + self.quiz[i]['answer'])
                print("===#===#===#===")

        print(f"your score is: {self.score}/{len(self.quiz)}")
        print("===#===#===#===")

        


game = Quiz()
game.start_quiz()