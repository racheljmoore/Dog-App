# Dog Care Application
# Author: [Your Name]
# Date: [Date]
# Description: A Python program that provides information on dog breeds, training tips, and adoption centers.
https://github.com/your-username/your-repository.gitgit remote add origin https://github.com/your-username/your-repository.git
import json
import logging

# Set up logging to console instead of a file to avoid permission issues
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Base Class: Dog
class Dog:
    def __init__(self, name, breed, age, energy_level, grooming_needs):
        self.name = name
        self.breed = breed
        self.age = age
        self.energy_level = energy_level
        self.grooming_needs = grooming_needs
    
    def display_info(self):
        return f"Breed: {self.breed}, Age: {self.age}, Energy Level: {self.energy_level}, Grooming Needs: {self.grooming_needs}"
    
    def bark(self):
        return "Woof! Woof!"

# Derived Class: TrainingTips
class TrainingTips(Dog):
    def __init__(self, name, breed, age, energy_level, grooming_needs, training_type, difficulty_level):
        super().__init__(name, breed, age, energy_level, grooming_needs)
        self.training_type = training_type
        self.difficulty_level = difficulty_level
    
    def get_training_tips(self):
        tips = {
            "Basic Commands": "Use positive reinforcement. Reward with treats for correct behavior.",
            "Leash Training": "Keep sessions short and reward calm walking.",
            "House Training": "Take your dog out frequently and reward them for going outside."
        }
        return tips.get(self.training_type, "No tips available for this type of training.")

# Derived Class: AdoptionCenter
class AdoptionCenter:
    def __init__(self, name, location, contact_info, hours):
        self.name = name
        self.location = location
        self.contact_info = contact_info
        self.hours = hours
    
    def display_center_info(self):
        return f"Adoption Center: {self.name}, Location: {self.location}, Contact: {self.contact_info}, Hours: {self.hours}"

# Dictionary to store dog breed info
dog_breeds = {
    "Golden Retriever": {"size": "Large", "energy": "High", "grooming": "Moderate"},
    "Bulldog": {"size": "Medium", "energy": "Low", "grooming": "Low"},
    "Poodle": {"size": "Medium", "energy": "High", "grooming": "High"}
}

# Function to get breed info
def get_breed_info(breed):
    return dog_breeds.get(breed, "Breed not found.")

# Function to simulate user input for testing
def simulated_input(prompt):
    simulated_responses = {
        "Enter your choice: ": "1",
        "Enter the dog breed: ": "Golden Retriever",
        "Enter training type (Basic Commands, Leash Training, House Training): ": "Basic Commands"
    }
    return simulated_responses.get(prompt, "4")  # Default to exit

# User Menu
def main_menu():
    while True:
        print("\nWelcome to the Dog Care App!")
        print("1. Look up Dog Breed Info")
        print("2. Get Training Tips")
        print("3. Find Adoption Centers")
        print("4. Exit")
        
        choice = simulated_input("Enter your choice: ")
        logging.info(f"User selected option {choice}")
        
        if choice == "1":
            breed = simulated_input("Enter the dog breed: ")
            print(get_breed_info(breed))
        elif choice == "2":
            training = simulated_input("Enter training type (Basic Commands, Leash Training, House Training): ")
            tips = TrainingTips("Unknown", "Unknown", 0, "Unknown", "Unknown", training, "Medium")
            print(tips.get_training_tips())
        elif choice == "3":
            center = AdoptionCenter("Happy Paws Shelter", "Los Angeles, CA", "(123) 456-7890", "9 AM - 6 PM")
            print(center.display_center_info())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
git initgit remote add origin https://github.com/your-username/your-repository.gitgit add .
