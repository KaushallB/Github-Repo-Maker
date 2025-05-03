# Github-Repo-Maker
# GitHub Repo Maker using Python and Requests

## 📘 Context

While learning API testing in Python during my internship, I came across the powerful requests library. I was fascinated by how we can send HTTP requests directly in Python — just like we do in tools like Postman. This gave me the idea to create a GitHub Repository Maker tool using the GitHub REST API.

This project allows you to:
- Authenticate with GitHub using a **Personal Access Token (Classic)**
- Create a new repository
- Check repository status and visibility
- Update the visibility of an existing repository
- Delete the repository

## 🚀 Features

- Token is stored securely in a `token.txt` file for reuse.
- Simple CLI interface for creating and managing repositories.
- All GitHub API calls are handled with appropriate request methods (GET, POST, PATCH, DELETE).
- Clear messages and exception handling for better user experience.

---

## 🔧 Requirements

You need Python installed. This project uses the following Python standard and external modules:

- `requests`
- `os`
- `json`

### Install required package

If `requests` is not already installed, you can install it using:

```bash
pip install requests
```

 ### How to Create a GitHub Personal Access Token (Classic)
Follow these steps to generate a Personal Access Token (PAT):

##Step-by-Step Instructions:

Go to your GitHub account.

Click your profile picture (top-right corner) → Settings

In the left sidebar, click Developer settings

Click Personal access tokens → Tokens (classic)

Click the green "Generate new token (classic)" button

Add a Note (e.g., Repo Maker Script) and expiration (e.g., 30 days or No expiration)

Under Scopes, select:

repo – Full control of private repositories

delete_repo – To allow deleting repositories

Click Generate token

Copy the token shown ONLY ONCE — it won't be shown again!

Paste it when the Python script asks for it. It will be saved in token.txt for future use.
