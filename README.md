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

## 🔒 Authentication

To authenticate, use the following endpoints:

- **Token Obtain Pair**: `POST /api/token/`
- **Token Refresh**: `POST /api/token/refresh/`

## 🔧 Development

To run the development server:

```bash
python manage.py runserver
```

## 📝 Contributing

Feel free to open issues or pull requests if you have any improvements or bug fixes. Contributions are always welcome!

## 📧 Contact

For any questions, you can reach out to me, Peyman Rashidi,
at [rashidi.peyman@gmail.com](mailto:rashidi.peyman@gmail.com).

---

Feel free to adjust any sections as needed!