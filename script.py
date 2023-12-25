
import firebase_admin
from firebase_admin import credentials, firestore

# Replace with your own Firebase project credentials file
credpath = r"cred.json"
login = credentials.Certificate(credpath)
firebase_admin.initialize_app(login)

db = firestore.client()

def get_user_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    address = input("Enter your address: ")
    fav_food = input("Enter your favorite food: ")
    
    return {
        "name": name,
        "age": age,
        "address": address,
        "favorite_food": fav_food
    }

def store_user_details(user_details):
    users_ref = db.collection('User Details')
    users_ref.add(user_details)

def main():
    print("Hello! Please provide your details.")
    
    user_details = get_user_details()
    
    print("\nStoring your details on Firebase...\n")
    
    store_user_details(user_details)
    
    print("Details successfully stored on Firebase!")

if __name__ == "__main__":
    main()