# 📰 Ads Board (Django)

A simple **ads board** built with Django as part of Sergey Balakirev’s course.  
Users can register, create, edit, and browse ads with images, categories, and search functionality.  

---

## 🚀 Features
- 🔐 User registration & authentication  
- 👤 User profile page  
- ➕ Create, edit, and delete ads  
- 🖼️ Image upload support  
- 📂 Categories and search  
- 📱 Responsive interface  

---

## 🛠 Tech Stack
- **Backend:** Django 4.x, Django ORM  
- **Frontend:** HTML, CSS (Bootstrap), Django Templates  
- **Database:** SQLite (default), can be switched to PostgreSQL  
- **Other:** Django Forms, Django Admin  

---

## 🏆 What I Learned
- Working with Django ORM & migrations
- Organizing project into apps
- Using Django Forms for validation
- Handling static & media files
- Customizing Django Admin

## 📌 Future Plans
⭐ Add favorites system
🔎 Improve search with filters (price, category)
🌐 Build REST API with Django REST Framework
🗄 Switch to PostgreSQL for production

## ⚡ Quick Start

```bash
# 1. Clone repository
git clone https://github.com/username/ads-board.git
cd ads-board

# 2. Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt

# 3. Apply migrations
python manage.py migrate

# 4. Create superuser (optional)
python manage.py createsuperuser

# 5. Run development server
python manage.py runserver
