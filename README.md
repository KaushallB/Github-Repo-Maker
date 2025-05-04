# GitHub Repo Maker using Python and Requests

## Context

While learning API testing in Python during my internship, I came across the powerful requests library. I was fascinated by how we can send HTTP requests directly in Python — just like we do in tools like Postman. This gave me the idea to create a GitHub Repository Maker tool using the GitHub REST API.

This project allows you to:
- Authenticate with GitHub using a **Personal Access Token (Classic)**
- Create a new repository
- Check repository status and visibility
- Update the visibility of an existing repository
- Delete the repository

##  Features

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

1) Go to GitHub Settings
Visit: https://github.com/settings/tokens

2) Click on "Generate new token (classic)"

3) Provide a note and expiration date (e.g., "For API script use")

4) Select scopes/permissions
   Make sure to check:

   repo (Full control of private repositories)

  delete_repo (To delete repositories)

5) Click "Generate token"

6) Copy the token shown ONCE
   Paste it into the terminal when the script asks for it. The token will be stored securely in token.txt for later use.



