# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 10:17:31 2021

@author: lobit
"""

# en class alltid begynner med en storbokstav
class Question:
    def __init__(self, prompt , answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "Hvor mange bein har en tusenbein? \n\n(a) 1 \n(b) 4 \n(c) 1000",
    "I hvilken kontinent ligger Norge? \n\n(a) Europe \n(b) Afrika \n(c) Asia",
    "Når er det Jul? \n\n(a) brannbil? \n(b) mandag \n(c) 25 desember",
    "I hvilken galakse bor menneskene? \n\n(a) Jaeren \n(b) Milky Way \n(c) Jord"]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c"),
    Question(question_prompts[3], "b")]

def test_svar(questions):
    score_teller = 0
    for question in questions:
        answer = input(question.prompt + "\n" + "\nSvar:\nc")
        if answer == question.answer:
            score_teller += 1
    print("\nDu fikk " + str(score_teller) + '/' + str(len(questions)) + " riktig \n")
    
test_svar(questions)    

