# User Profile API

### This project provides a REST API for managing user profiles with CRUD (Create, Read, Update, Delete) functionalities.

This repository contains Django REST framework API views for managing user profiles.


## Create User Profile

- **URL:** `http://localhost:8000/user/`
- **Method:** POST
- **Request Body (JSON):**
  ```json
  {
      "name": "User 1",
      "email": "user1@example.com",
      "profile_picture": "https://example.com/profile.jpg"
  }
  ```

## Fetch User Profiles

- **URL:** `http://localhost:8000/user/profiles/?page=1&page_size=1`
- **Method:** GET

### Parameters
- `page`: Specifies the page number of results to retrieve. In this URL, `page=1` indicates that the first page of results is being requested.
- `page_size`: Specifies the number of items per page. Here, `page_size=1` indicates that only one item should be included per page.

## Fetch User Profile by ID
Use this endpoint to fetch a user profile by its ID.
- **URL:** `http://localhost:8000/profiles/{id}/`
- **Method:** GET
Replace {id} with the ID of the user profile you want to fetch.

## Update User Profile by id
Use this endpoint to update a user profile by its ID.
- **URL:** `http://localhost:8000/profiles/{id}/`
- **Method:** PUT
- **Request Body (JSON):**
  ```json
  {
      "name": "User 1",
      "email": "user1@example.com",
      "profile_picture": "https://example.com/profile.jpg"
  }
  ```
Replace {id} with the ID of the user profile you want to update.

## Delete User Profile
Use this endpoint to delete a user profile by its ID.

- **URL:** `http://localhost:8000/profiles/{id}/`
- **Method:** DELETE
Replace {id} with the ID of the user profile you want to delete.
