def quiz_start():
    quiz = {
        "Question1" :{
            "question": "What is the capital of france?",
            "Answer" : "Paris"
        },
        "Question2": {
            "question": "How many genders are there",
            "Answer": "2"
        },
        "Question3":{
            "question": "What is the second month of the year",
            "Answer": "February"
        },
        "Question4":{
            "question": "What is the third month of the year",
            "Answer": "March"
        },
        "Question5":{
            "question": "What is the fourth month of the year",
            "Answer": "April"
        },
        "Question6":{
            "question": "What is the fifth month of the year",
            "Answer": "May"
        },
        "Question7":{
            "question": "What is the sixth month of the year",
            "Answer": "June"
        },
        "Question8":{
            "question": "What is the seventh month of the year",
            "Answer": "July"
        },
        "Question9":{
            "question": "What is the eight month of the year",
            "Answer": "August"
        },
        "Question10":{
            "question": "What is the ninth month of the year",
            "Answer": "September"
        },
        "Question11":{
            "question": "What is the tenth month of the year",
            "Answer": "October"
        },
        "Question12":{
            "question": "What is the eleventh month of the year",
            "Answer": "November"
        },
        "Question13":{
            "question": "What is the twelfth month of the year",
            "Answer": "December"
        },
        

    }


    score = 0

    for key, value in quiz.items():
        print(value['question'])
        answer = input("Answer? ")

        if answer.lower() == value['Answer'].lower():
            print("Correct")
            score = score + 1
            print ("Your score is " + str(score) + "\n")
        else:
            print ("Wrong ")
            print("The answer is " + str (value['Answer']))
            print ("Your score is " + str(score) +"\n")


    percentage = (score/13)*100
    print("Your percentage success is " +  str(int(percentage))+"%")
      




