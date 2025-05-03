import requests
import json
import os


base_url = "https://api.github.com"
header = None  # Global variable to store the token header
token_file = 'token.txt'  # Global variable for the token file
repo_name = None  # Global variable to store repository name

def get_token():
    global header #Accessing the global header variable
    try:
        if os.path.exists(token_file):
            with open(token_file, 'r') as file: #Reading token from the file
                token = file.read().strip()
                print("Token loaded from file.")
                header = {"Authorization": f"Bearer {token}"}  # Modifying global header and putting header like in Postman
                
        else:
            while True:
                token = input("Enter your GitHub Personal Access Token: ")
                # Checking if the token is valid by making a request to the GitHub API
                url = base_url + "/user"                      #Creating a url like in the browser (https://api.github.com/userkoname)
                header = {"Authorization": f"Bearer {token}"} #Header file like in POSTMAN
                response = requests.get(url, headers=header)  #GET Request like in POSTMAN

                if response.status_code == 200:  
                    print("Token is valid.")     #IF OK response from the server then
                    # Saving the token to the file
                    with open(token_file, 'w') as file:
                        file.write(token)
                    break
                else:
                    print(f"Invalid token. Status code: {response.status_code}. Please try again.") #Checking status code response from the server making it easier 
    except Exception as e:
        print(f"The Error while trying to get the  token is : {e}")

#Getting user details using GET just like in postman
def get_user_details():
    try:
        username = input("Enter Your GitHub username: ") 
        url = base_url + "/users/" + username            #Creating a url like in the browser
        response = requests.get(url, headers=header)     #GET Request like in POSTMAN
        if response.status_code == 200:
            user_data = response.json()                                    #Getting the response and storing it in user_data variable
            print("API response is \n", json.dumps(user_data, indent=4))   #Making the response readable and clear instead of single line
        else:
            print(f"Failed to fetch user details. Status code: {response.status_code}")
        return username
    except Exception as e:
        print(f"The Error while trying to get the userdetails is : {e}")  #To find out any exception that can ariise

# Creating a repository
def create_repo(username):
    global repo_name                                        #Accessing the global repo name variable
    try:
        url = base_url + "/user/repos"                      #Creating a url like in the browser
        create_repo_choice = input("Do you want to create a repository? (y/n): ").lower()  #asking user input to create a new repo or not?
        if create_repo_choice == 'y':                               #If user presses y then
            repo_name = input("Enter repository name: ")
            visibility = input("Should the repository be public or private? (public/private): ").lower()
            visibility = True if visibility == "public" else False   # Sets visibility as True for public repos and False for private repos 
            data = {
                "name": repo_name,                                  
                "description": "Created using GitHub API",
                "private": not visibility          # This makes the repository public becuase if user selecets True then this will be false
            }

            response = requests.post(url, headers=header, json=data)        #POST Request like in POSTMAN
            print(f"Response status code: {response.status_code}")
            

            if response.status_code == 201:
                print(f"Repository '{repo_name}' created successfully.")  #201 detrmines creation of something
            else:
                print(f"Failed to create repository. Status code: {response.status_code}")
        else:
            print("Repository creation skipped.")
    except Exception as e:
        print(f"Error while creating repository: {e}")

#Checking Repository Status
def check_repo_status(username):                                    #Passing the username for easy access
    global repo_name
    try:
        if repo_name:
            url = base_url + '/repos/' + username + '/' + repo_name   #Creating a url like in the browser
            response = requests.get(url, headers=header)              #GET Request like in POSTMAN
            if response.status_code == 200:
                repo_data = response.json()
                repo_url = repo_data['html_url']                       #Getting the link to the repository of the user
                repo_visibility = "Public" if not repo_data['private'] else "Private"
                print(f"Repository URL: {repo_url}")                   #Getting the url of the repo
                print(f"Repository Visibility: {repo_visibility}")     #Checking private or public status of repo
                return True                                            # Repo exists
            else:
                print(f"Repository not found. Status code: {response.status_code}")
                return False  # Repo doesn't exist
        else:
            print("No repository to check.")
            return False
    except Exception as e:
        print(f"Error while checking repository status: {e}")
        return False

#Updating the Repository Visibility
def update_repo(username):
    global repo_name
    try:
        if repo_name:       #Checking if repo_name has a value
            # Checking if visibility change should be skipped
            change_visibility = input("Do you want to change visibility? (y/n): ").lower()
            if change_visibility == 'y':
                visibility = input("Change visibility to (public/private): ").lower()
                if visibility not in ['public', 'private']:               #validation to not accept null data
                    print("Invalid input. Skipping visibility change.")
                    return  # Exiting the function without making any changes
                
                visibility = True if visibility == "public" else False
                url = f"{base_url}/repos/{username}/{repo_name}"
                data= {"private": not visibility}
                response = requests.patch(url, headers=header, json=data)     #PATCH request as in Postman

                if response.status_code == 200:
                    print(f"Repository '{repo_name}' visibility updated successfully.")
                else:
                    print(f"Failed to update repository visibility. Status code: {response.status_code}")
            else:
                print("Visibility change skipped.")
        else:
            print("No repository to update.")
    except Exception as e:
        print(f"Error while updating repository visibility: {e}")


#Deleting Repository
def delete_repo(username):
    global repo_name
    try:
        if repo_name:
            confirm = input(f"Do you want to delete the repository '{repo_name}'? (y/n): ").lower()
            if confirm == 'y':                                      #Confirming User Input
                url = f"{base_url}/repos/{username}/{repo_name}"
                response = requests.delete(url, headers=header)     #DELETE request as in Postman
                if response.status_code == 204:
                    print(f"Repository '{repo_name}' deleted successfully.")
                else:
                    print(f"Failed to delete repository. Status code: {response.status_code}")
            else:
                print("Repository deletion skipped.")
        else:
            print("No repository to delete.")
    except Exception as e:
        print(f"Error while deleting repository: {e}")

def main():
    global repo_name
    try:
        get_token()                             # No need to return anything, header is stored globally

        if header:                               #Checking if header value exists then only proceed
            username = get_user_details()        #userdetails returns username so storing it here
            create_repo(username)                #sending the same username to createrepo function to make it easier

        # Allowing user to choose to skip repo creation and delete an existing repo instead
        if repo_name is None:                   # Checking if repo name is not defined yet
            repo_name = input("Enter the name of an existing repository to edit: ")

        if repo_name:  # Ensuring reponame has a value before accessing it
            repo_exists = check_repo_status(username)       #Checking the details of the repo in that username
            if repo_exists:
                # Asking if the user wants to skip visibility change and delete directly
                skip_visibility_change = input("Do you want to skip visibility change and delete the repository? (y/n): ").lower()
                
                if skip_visibility_change == 'y':
                    delete_repo(username)  # Skip visibility change and directly delete the repo
                else:
                    update_repo(username)  # Updating visibility if the user wants to change it
                    delete_repo(username)  # Then deleting the repository if required
            else:
                print("Repository does not exist.")
                
    except Exception as e:                  #catching the exception if arises
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":      #Calling the main function
    main()
