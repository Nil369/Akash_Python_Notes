import requests as req

def get_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    res = req.get(url)
    data = res.json()

    # Check if the API request was successful and data is available
    if data["success"] and "data" in data:

        actual_name = data["data"]["name"]["first"]
        user_name = data["data"]["login"]["username"]
        location = data["data"]["location"]["country"]

        return actual_name, user_name, location

def main():
    try:
        actual_name, user_name, location = get_random_user()
        print("********************************")
        print(f"\nHi! my name is: {actual_name}")
        print(" ------------------")
        print(f"Username: {user_name}\nI live in {location}.\nThanks!!")
        print(" ------------------")
        print("\n********************************")
    except Exception as e:
        raise Exception("Failed to fetched user data !!")

if __name__ == "__main__":
    main()

