

# Goodreads Website Clone 📚

Welcome to the **Goodreads Website Clone**! 🎉 This project is a Django-based web application that mimics the functionality of Goodreads. Users can manage books, reviews, and bookmarks in a seamless and intuitive interface.

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

Create a `.env` file in the root directory of the project and add your environment variables there. 

```plaintext
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

## 📂 Models

The project includes several models:

### CustomUser 👤

Custom user model extending `AbstractUser` with an additional `role` field.

```python
class CustomUser(AbstractUser):
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={"unique": _("A user with that username already exists.")},
        default=f"user__{uuid.uuid4().hex[:8]}"
    )
    email = models.EmailField(_("email address"), unique=True)
    role = models.CharField(_("role"), max_length=10, choices=UserType.ROLE_CHOICES, default=UserType.MEMBER)
```

### Book 📕

A model representing books with details like title, summary, and publication year.

```python
class Book(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_('title'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('slug'))
    summary = models.TextField(max_length=1000, verbose_name=_('summary'))
    year = models.DateField(verbose_name=_('year of publication'))
```

### Author 🖋

A model for authors with first and last names.

```python
class Author(BaseModel):
    first_name = models.CharField(max_length=150, verbose_name=_('first name'))
    last_name = models.CharField(max_length=150, verbose_name=_('last name'))
```

### Review ⭐️

A model for user reviews of books, including score and comments.

```python
class Review(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name=_('book'), related_name='reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name=_('user'), related_name='reviews')
    comment = models.TextField(max_length=1000, verbose_name=_('comment'), blank=True)
    score = models.IntegerField(verbose_name=_('score'), validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, default=0)
```

### Bookmark 🔖

A model for bookmarking books by users.

```python
class Bookmark(BaseModel):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, verbose_name=_('book'), related_name='bookmarks')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, verbose_name=_('user'), related_name='bookmarks')
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

For any questions, you can reach out to me, Peyman Rashidi, at [rashidi.peyman@gmail.com](mailto:rashidi.peyman@gmail.com).

---

Feel free to adjust any sections as needed!