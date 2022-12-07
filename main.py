# this prints the title and authors. 
print("Day of an SU Student\n by Nickie Vertigan")

#this asks the user to input the names of the characters to start the adventure
name1 = input ("What's your name? ")
name2 = input ("What's your roommate's name? ")
name3 = input ("What's your favorite professor's name? ")

# this sets the amount of energy to 20 (out of 25). The value will determine some events in the story based on how you answer the prompts.
energy = 20

# START of first encounter. your roommate is still sleeping and you do the same or walk to Deg
print ("\nGood morning " +name1 + "!"" You are a student at Susuquehanna University getting ready for your day full of classes. You currently have " +str(energy)+ " out of 25 energy \n "+name2+" is still sleeping. Should you get back in bed and sleep in or walk to Deg to get breakfast?")

# ask the user to decide to sleep in or walk to breakfast
answer = input ("\n Enter 'sleep in' or 'breakfast' (in all lowercase without apostrophes): ")

# if user chooses "sleep in", their energy will increase by 5 since they are getting extra rest.
if answer == "sleep in" and energy <= 25:
  # increases engery by 5 
  energy = energy+5
  #print outcome
  print("You wrap yourself in your blanket and get back in bed.\n Before you fall asleep you set your alarm so you won't be late for your first class.\n You shut your eyes and fall asleep, again. Your energy has increased by 5.\n You now have "+str(energy)+" out of 25!")

#if user chooses "breakfast", their engery will decrease by 5 since there is a long walk from their dorm to Deg
elif answer == "breakfast" and energy >= 5:
  energy = energy-5
  print ("\nIt's a long walk from your dorm to Deg. Your energy has decreased by 5. Breakfast was good. \nYou now have "+str(energy)+" out of 25")

  # punshish the user, by taking 3 of their energy, for inputing something other than the answer options
elif answer != "breakfast" and answer != "sleep in":
  energy = energy-3
  print("Oops! You did not enter one of the answer choices. That must have used some brain power!\n You now have "+str(energy)+" out of 25.")

# if they don't have enough energy, they stay in their room to eat and watch netflix
else:
  print("You stay in your room to watch netflix and eat ramen.")
#END OF FIRST ENCOUTNER

#START of second encounter! It is time to go to class. User runs to class, walks to class, or stops to talk on their way to class.  
print("\n It's time to go to your first class taught by "+name3+". Should you run to class, walk to class, or stop and talk to a friend on your way to class?")

# asks user if they want to run, walk or talk
answer = input ("\n Enter 'run', 'walk, or 'talk':")

#if they have enough energy and pick run, their energy will decrease by 10
if answer == "run" and energy >= 10:
  energy = energy - 10
  print ("\nYou ran to class and got there early. Good job, you are ready for class and having a great start to your day! You now have " +str(energy)+" out of 25 energy")

# if they have enough energy and pick walk, their energy will decrease by 5
elif answer == "walk" and energy >= 5:
  energy = energy-5
  print ("\n You walked to class and got there just in time with a minute to spare! Thank goodness you weren't late on your first day!\n You now have "+str(energy)+" out of 25")

#if they have enough energy and pick talk, their energy will decrease by 3 
elif answer == "talk" and energy >= 3:
  energy = energy-3
  print ("\n You see your friend from animal club and talked about the new executive board.\n While listening to their thoughts on the topic, you had a chance to catch your breath. \n Unfortunatley, that made you late for class and "+name3+" is not impressed.\n You now have "+str(energy)+" out of 25")

# if they enter something other than the options, they will lose 3 energy points
elif answer != "talk" and answer != "walk" and answer != "run":
  energy = energy-3
  print("Oops! You did not enter one of the answer choices. That must have used some brain power!\n You now have "+str(energy)+" out of 25")

# if they don't have enough energy, they skip class
else:
  print("You skip class and get marked as an unexcused absence.")
#END OF SECOND ENCOUNTER

#START of third encounter. User goes to a party or stays in for a movie night
print ("\n" +name2+ " told you there is a party happening tonight. It sounds like a ton of fun but do you have enough energy to go? You currently have " +str(energy)+" out of 25 energy. Should you go to the party or stay home and have a movie night?")

# asks user if they want to go out or stay in
answer = input ("\n Enter 'go out' or 'stay in': ")

#if user has enough energy, they go to the party and lose 5 energy points.
if answer == 'go out' and energy >=10:
  energy = energy-5
  print ("You went to the party and had fun but all of your energy is used up! Better catch up on sleep tomorrow night. You barely make it back to your dorm. You head hits the pillow and you are asleep in seconds. \n\n THE END")

# if user has enough energy, they stay in to watch movies and energy decreases by 3
elif answer == 'stay in' and energy >= 3:
  energy = energy- 3
  print ("You put on your favorite comfy clothes and made some popcorn. Time to settle into your bean bag chair and watch your favorite movie!\n\n THE END")
# if user enters something other than the answer choices, their energy goes down by 3
elif answer != 'stay in' and answer != 'go out':
  energy = energy-3
  print("Oops! You did not enter one of the answer choices! You are so tired that you can't even think properly!\n You call it a day and go to sleep.")

# if user doesn't have enough energy, they go to sleep
else:
  print("Uh oh! Going out sounds fun but you don't have enough energy. You are too tired from your long day. Time to get some rest. You finish your day by falling to sleep listening to ocean sounds. How peaceful! \n\n THE END")