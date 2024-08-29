# Goodreads Website Clone 📚

Welcome to the **Goodreads Website Clone**! 🎉 This project is a Django-based web application that mimics the
functionality of Goodreads. Users can manage books, reviews, and bookmarks in a seamless and intuitive interface.

![img.png](img.png)

## 🛠️ Installation

To get started, clone the repository and install the necessary packages:

```bash
git clone https://github.com/PEMIDI/django-goodreads-clone.git
cd django-goodreads-clone
pip install -r requirements.txt
```

## 🧩 Requirements

Here's a list of packages used in the project:

- `Django==4.2`
- `djangorestframework==3.15.2`
- `djangorestframework-simplejwt==5.3.1`
- `drf-yasg==1.21.7`
- And many more!

## ⚙️ Configuration

Create a `.env` file in the `config` directory of the project and add your environment variables there.

```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```


## 🔧 Development

To run the development server:

```bash
python manage.py runserver
```



## Goodreads API Documentation


## Base URL

- **Host:** `localhost:8000`
- **Scheme:** `http`
- **Base Path:** `/`

## Authentication

The API uses basic authentication. Include your username and password in the headers for access.

## Endpoints

### Authentication

#### `/auth/`

- **Method:** `POST`
- **Description:** Authenticate the user. (Details not specified in the OpenAPI definition.)

### Token Management

#### `/api/token/`

- **Method:** `POST`
- **Description:** Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.
- **Request Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  ```json
  {
    "access": "string",
    "refresh": "string"
  }
  ```

#### `/api/token/refresh/`

- **Method:** `POST`
- **Description:** Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
- **Request Body:**
  ```json
  {
    "refresh": "string"
  }
  ```
- **Response:**
  ```json
  {
    "access": "string"
  }
  ```

### Books

#### `/books/`

- **Method:** `GET`
- **Description:** List books with pagination.
- **Query Parameters:**
  - `page` (optional): A page number within the paginated result set.
  - `page_size` (optional): Number of results to return per page.
- **Response:**
  ```json
  {
    "count": "integer",
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": "integer",
        "title": "string",
        "bookmark_counts": "string"
      }
    ]
  }
  ```

#### `/books/{id}/`

- **Method:** `GET`
- **Description:** Retrieve details of a specific book.
- **Path Parameters:**
  - `id`: A unique integer value identifying this book.
- **Response:**
  ```json
  {
    "title": "string",
    "reviews": [
      {
        "comment": "string",
        "score": "integer"
      }
    ],
    "user_reviews": "string",
    "comments_count": "integer",
    "average_score": "integer",
    "score_1_count": "integer",
    "score_2_count": "integer",
    "score_3_count": "integer",
    "score_4_count": "integer",
    "score_5_count": "integer"
  }
  ```

#### `/books/{id}/add-review/`

- **Method:** `POST`
- **Description:** Add a review to a specific book.
- **Path Parameters:**
  - `id`: A unique integer value identifying this book.
- **Request Body:**
  ```json
  {
    "comment": "string",
    "score": "integer"
  }
  ```
- **Response:**
  ```json
  {
    "title": "string",
    "reviews": [
      {
        "comment": "string",
        "score": "integer"
      }
    ],
    "user_reviews": "string",
    "comments_count": "integer",
    "average_score": "integer",
    "score_1_count": "integer",
    "score_2_count": "integer",
    "score_3_count": "integer",
    "score_4_count": "integer",
    "score_5_count": "integer"
  }
  ```

#### `/books/{id}/bookmark/`

- **Method:** `POST`
- **Description:** Add a book to bookmarks.
- **Path Parameters:**
  - `id`: A unique integer value identifying this book.
- **Request Body:**
  ```json
  {
    "id": "integer"
  }
  ```
- **Response:**
  ```json
  {
    "title": "string",
    "reviews": [
      {
        "comment": "string",
        "score": "integer"
      }
    ],
    "user_reviews": "string",
    "comments_count": "integer",
    "average_score": "integer",
    "score_1_count": "integer",
    "score_2_count": "integer",
    "score_3_count": "integer",
    "score_4_count": "integer",
    "score_5_count": "integer"
  }
  ```

## Definitions

### TokenObtainPair

- **Required Fields:**
  - `username`: (string) The username for authentication.
  - `password`: (string) The password for authentication.

### TokenRefresh

- **Required Fields:**
  - `refresh`: (string) The refresh token.
- **Optional Fields:**
  - `access`: (string) The new access token.

### Book

- **Required Fields:**
  - `title`: (string) The title of the book.
- **Optional Fields:**
  - `id`: (integer) The ID of the book.
  - `bookmark_counts`: (string) The number of bookmarks.

### BookReview

- **Optional Fields:**
  - `comment`: (string) The review comment.
  - `score`: (integer) The rating score (1-5).

### BookDetail

- **Required Fields:**
  - `title`: (string) The title of the book.
  - `reviews`: (array of BookReview) List of reviews for the book.
- **Optional Fields:**
  - `user_reviews`: (string) User reviews summary.
  - `comments_count`: (integer) The total number of comments.
  - `average_score`: (integer) The average score of the book.
  - `score_1_count`: (integer) Number of 1-star ratings.
  - `score_2_count`: (integer) Number of 2-star ratings.
  - `score_3_count`: (integer) Number of 3-star ratings.
  - `score_4_count`: (integer) Number of 4-star ratings.
  - `score_5_count`: (integer) Number of 5-star ratings.



## 📧 Contact

For any questions, you can reach out to me, Peyman Rashidi,
at [rashidi.peyman@gmail.com](mailto:rashidi.peyman@gmail.com).


note: This Readme generated using AI by my custom prompt to keep productivity,
but validated by me generaly.

### By the way, this is my goodreads account. I would be happy if you would like to meet there:

### https://www.goodreads.com/user/show/63726559-peyman-rashidi-pemidi