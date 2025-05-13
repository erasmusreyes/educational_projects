


Problem Statement:

A local restaurant organization would like to offer a website that recommends a restaurant to a user. The user will enter a type of food and an Eau Claire zip code and they will receive a recommendation on a restaurant. The user should have the option to quit and receive a thank you message. If the user enters an invalid entry or there are no restaurants to recommend, they user will receive a message stating that.  

Nouns: website, user, restaurant, entry, message

Verbs: recommend, enter, quit, receive



Defining diagram:
 
Inputs: userType, userLocation

Processing: 
check to see if quit was entered
check to see if userType & userLocation match a restaurant
display message
display error message
display thank you message

Outputs:
message
error message
thank you message


Flowchart: 

 



Pseudocode: 

function RecommendRestaurant
	initialize userType to ""
	initialize userLocation to 
	initialize message to ""
	initialize keepLooping to true

	while (keepLooping is true) 
	userType = prompt "Please enter a food type [Burgers, 			Chicken, Dessert, Pizza, Sandwiches, Tacos or "Quit" 			to stop. 
			
	if (userType ="Quit") 
	message = "Thank you for using Restaurant 					Recommender."
	set keepLooping to false
	alert with message
	else 
	userLocation = prompt "Please enter an Eau Claire zip code."

	if (userType ="Tacos" & userLocation = "54701") 
	message = "Super Taco 123 Red Road, Eau Claire."

	else if (userType = "Tacos" & userLocation = "54703") 
	message = "Taco Grande 456 Red Street, Eau Claire."

	else if (userType ="Burgers" & userLocation = "54701") 	message = "Happy Burger 789 Yellow Road, Eau Claire."

	else if (userType = "Burgers" & userLocation = "54703") 
	message = "Crazy Burger 123 Yellow Street, Eau Claire."

	else if (userType = "Pizza" & userLocation = "54701") 
	message = "Pizza Palace 456  Orange Road, Eau Claire."

	else if (userType = "Pizza" & userLocation = "54703") 
	message = "Geno's Pizza 789 Orange Street, Eau Claire."

	else if (userType = "Sandwiches" && userLocation = "54701") 
	message = "Super Sandwich 123 Green Road, Eau Claire."

	else if (userType = "Sandwiches" & userLocation = "54703") 
	message = "Awesome Sandwich 456 Green Street, Eau Claire."

	else if (userType = "Chicken" && userLocation = "54701") 
	message = "Chicken Unlimited 789 Blue Road, Eau Claire."

	else if (userType = "Chicken" && userLocation = "54703") 
	message = "Amazing Chicken 123 Blue Street, Eau Claire."

	else if (userType = "Dessert" && userLocation = "54701") 
	message = "Just Desserts 456 Indigo Road, Eau Claire."

	else if (userType = "Dessert" & userLocation = "54703") 
	message = "Only Dessert 789 Indigo Road, Eau Claire."

	else 
	message = "Sorry, we don't have any restaurants to 	recommend. Please try again."
	
	alert(message)
		

Call RecommendRestaurant



Test Cases: 

Variables: userType, userLocation, message, keepLooping

Test Case 1:

Input Values: Tacos, 54703

Expected Result: Taco Grande 456 Red Street, Eau Claire.

Actual Result: Taco Grande 456 Red Street, Eau Claire.


Test Case 2:

Input Values: Pizza, 54701

Expected Result: Pizza Palace 456 Orange Road, Eau Claire.

Actual Result: Pizza Palace 456 Orange Road, Eau Claire.


Test Case 3:

Input Values: Quit

Expected Result: Thank you for using Restaurant Recommender.

Actual Result: Thank you for using Restaurant Recommender.


Test Case 4:

Input Values: Pie, 54729

Expected Result: Sorry, we don't have any restaurants to 					recommend. Please try again.

Actual Result: Sorry, we don't have any restaurants to recommend. 			Please try again.







