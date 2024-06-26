# Routes

## Subscribed groups routes

#### Add Listener

- **URL:** 
  - `POST /listeners/Addlistener`

- **Function:**
  - `Addlistener`

- **Description:**
  - Creates a new listener entry for a group.

- **Parameters:**

| Parameter           | Type   | Description                 |
|----------------------|--------|-----------------------------|
| groupId              | string | Group ID for the listener   |

- **Request Body Example:**
  ```json
  {
    "groupId": "abc123"
  }
  ```

- **Returns:**
  - Success: JSON response with a success message and HTTP status 201 (Created).
  - Error: JSON response with an error message and HTTP status 400 (Bad Request) if the request is invalid.

---

## Posts routes

#### Create Posts

- **URL:** 
  - `POST /posts/createPosts`

- **Function:**
  - `createPosts`

- **Description:**
  - Creates a new post with specified title, content, author, date, initial likes, and dislikes.

- **Parameters:**

| Parameter           | Type   | Description                 |
|----------------------|--------|-----------------------------|
| title                | string | Title of the post           |
| content              | string | Content of the post         |
| author               | string | Author of the post          |
| date                 | string | Date of the post (optional) |

- **Request Body Example:**
  ```json
  {
    "title": "Sample Post",
    "content": "This is the content of the post.",
    "author": "John Doe",
    "date": "2024-06-26"
  }
  ```

- **Returns:**
  - Success: JSON response with a success message and HTTP status 201 (Created).
  - Error: JSON response with an error message and HTTP status 400 (Bad Request) if the request is invalid.
