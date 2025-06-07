import random
print("Welcome to my quiz!!")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()
    
print("Then let's Play!!")
print("\nInitial score = 100 and for each wrong question 20 points will be deducted.")
question = 0
score = 100

question_ids=[0,1,2,3,4,5]

selected_questions = random.sample(question_ids,5)

for ran in selected_questions:
    if ran == 0:
        print("\ncurrent score: "+str(score))
        answer = input("What does CPU stand for? ")
        if answer.lower() == "central processing unit":
           print("Correct!")
           question += 1
        else:
            print("Wrong! It's Central Processing Unit")
            score -= 20

    
    elif ran == 1:
        print("\ncurrent score: "+str(score))
        answer = input("When is the International Workers' Day? ")
        if answer.lower() == "1st may " and "may 1":
           print("Correct!")
           question += 1
        else:
            print("Wrong! It's 1st May")
            score -= 20

    elif ran == 2:
        print("\ncurrent score: "+str(score))
        answer = input("What is the largest mammal in the world? ")
        if answer.lower() == "blue whale":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Blue Whale")
            score -= 20

    elif ran == 3:
        print("\ncurrent score: "+str(score))
        answer = input("Who is known as the 'Father of the Nation' in India? ")
        if answer.lower() == "mahatma gandhi" and "gandhi":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Mahatma Gandhi")
            score -= 20

    elif ran == 4:
       print("\ncurrent score: "+str(score))
       answer = input("Which is the fastest land animal? ")
       if answer.lower() == "cheetah":
            print("Correct!")
            question += 1
       else:
            print("Wrong! It's Cheetah")
            score -= 20

    elif ran == 5:
        print("\ncurrent score: "+str(score))
        answer = input("Who is the CEO of Tesla, Inc.? ")
        if answer.lower() == "elon musk":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Elon Musk")
            score -= 20

    elif ran == 6:
        print("\ncurrent score: "+str(score))
        answer = input("What planet is known as the Red Planet? ")
        if answer.lower() == "mars":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Mars")
            score -= 20

    elif ran == 7:
        print("\ncurrent score: "+str(score))
        answer = input(" What is the powerhouse of the cell? ")
        if answer.lower() == "mitochondia":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Mitochondria")
            score -= 20
            
    elif ran == 8:
        print("\ncurrent score: "+str(score))
        answer = input("Who is the founder of Microsoft? ")
        if answer.lower() == "bill gates":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Blue Whale")
            score -= 20

    elif ran == 9:
        print("\ncurrent score: "+str(score))
        answer = input(" Which is the longest river in the world? ")
        if answer.lower() == "nile river" or "nile":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Nile River")
            score -= 20


    else:
        print("\ncurrent score: "+str(score))
        answer = input("Which bird is known for its colorful tail feathers? ")
        if answer.lower() == "peacock":
            print("Correct!")
            question += 1
        else:
            print("Wrong! It's Peacock")
            score -= 20


print("You got " +str(question)+ " questions correct!")
print("You got " +str((question / 5)*100)+ "%")