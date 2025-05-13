function RecommendRestaurant() {
	var userType = "";
	var userLocation = 0;
	var message = "";
	var keepLooping = true;

	while (keepLooping) {
		userType = prompt("Please enter a food type [Burgers, Chicken, Dessert, Pizza, Sandwiches, Tacos]" + "\n" + "or \"Quit\" to stop.");
		if (userType && userType.toLowerCase() === "quit") {
			message = "Thank you for using Restaurant Recommender.";
			keepLooping = false;
			alert(message);
		} else {
			userLocation = prompt("Please enter an Eau Claire zip code.");
      
      userType = userType ? userType.toLowerCase() : "";
      userLocation = userLocation ? userLocation.trim() : "";

			if (userType.toLowerCase() === "tacos" && userLocation === "54701") {
				message = "Super Taco 123 Red Road, Eau Claire.";

			} else if (userType.toLowerCase() === "tacos" && userLocation === "54703") {
				message = "Taco Grande 456 Red Street, Eau Claire.";

			} else if (userType.toLowerCase() === "burgers" && userLocation === "54701") {
				message = "Happy Burger 789 Yellow Road, Eau Claire.";

			} else if (userType.toLowerCase() === "burgers" && userLocation === "54703") {
				message = "Crazy Burger 123 Yellow Street, Eau Claire.";

			} else if (userType.toLowerCase() === "pizza" && userLocation === "54701") {
				message = "Pizza Palace 456  Orange Road, Eau Claire.";

			} else if (userType.toLowerCase() === "pizza" && userLocation === "54703") {
				message = "Geno's Pizza 789 Orange Street, Eau Claire.";

			} else if (userType.toLowerCase() === "sandwiches" && userLocation === "54701") {
				message = "Super Sandwich 123 Green Road, Eau Claire.";

			} else if (userType.toLowerCase() === "sandwiches" && userLocation === "54703") {
				message = "Awesome Sandwich 456 Green Street, Eau Claire.";

			} else if (userType.toLowerCase() === "chicken" && userLocation === "54701") {
				message = "Chicken Unlimited 789 Blue Road, Eau Claire.";

			} else if (userType.toLowerCase() === "chicken" && userLocation === "54703") {
				message = "Amazing Chicken 123 Blue Street, Eau Claire.";

			} else if (userType.toLowerCase() === "dessert" && userLocation === "54701") {
				message = "Just Desserts 456 Indigo Road, Eau Claire.";

			} else if (userType.toLowerCase() === "dessert" && userLocation === "54703") {
				message = "Only Dessert 789 Indigo Road, Eau Claire.";

			} else {
				message = "Sorry, we don't have any restaurants to recommend. Please try again.";
			}
			alert(message);
		}
	}
}
RecommendRestaurant();