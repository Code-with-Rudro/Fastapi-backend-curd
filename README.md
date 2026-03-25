# 🚀 FastAPI CRUD Performance Web Application

A full-stack CRUD web application built using **FastAPI (Backend)** and **HTML, CSS, JavaScript (Frontend)**.

This project demonstrates how to build a modern web application with API integration, dynamic UI updates, and JSON-based data handling.

The application allows users to **Create, Read, Update, and Delete products** through an interactive web interface connected to a FastAPI backend.

---

# 📌 Project Overview

This project was developed to practice **Full Stack Development** by integrating:

- ⚡ FastAPI backend
- 🎨 HTML, CSS, JavaScript frontend
- 📦 JSON-based data storage
- 🔗 REST API communication

The application provides a **clean and simple UI** where users can manage product data easily.

---

# ✨ Features

- ✅ Create new product entries
- ✅ View all products dynamically
- ✅ Update product details
- ✅ Delete products instantly
- ✅ RESTful API integration
- ✅ JSON-based data management
- ✅ Interactive frontend UI
- ✅ FastAPI backend with high performance
- ✅ Responsive card-based layout

---

# 🧰 Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript (Vanilla JS)

## Backend

- FastAPI
- Python
- Uvicorn

## Data Handling

- JSON File Storage

## Development Tools

- VS Code
- Git & GitHub
- REST API Testing

---

# 📂 Project Structure

```
# 📂 Project Structure

fastapi-ecommerce
│
├── app
│   ├── __pycache__
│   │   └── main.cpython-314.pyc
│   │
│   ├── data
│   │   └── products.json
│   │
│   ├── schema
│   │   ├── __pycache__
│   │   └── product.py
│   │
│   ├── service
│   │   ├── __pycache__
│   │   └── products.py
│   │
│   ├── .env
│   └── main.py
│
├── frontend
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── venv
├── requirements.txt
└── README.md
```

---

# 🔌 API Endpoints

## Get All Products

```
GET /products
```

Returns all product records.

---

## Get Product By ID

```
GET /products/{id}
```

Fetch a single product using its ID.

---

## Create Product

```
POST /products
```

Creates a new product.

---

## Update Product

```
PUT /products/{id}
```

Updates an existing product.

---

## Delete Product

```
DELETE /products/{id}
```

Removes a product from the database.

---

# 🖥️ Frontend Interface

The frontend is built using **HTML, CSS, and JavaScript** and communicates with the FastAPI backend using **Fetch API**.

### UI Features

- Dynamic product listing
- Card-based UI layout
- Add product form
- Update product functionality
- Delete product option

---

# 📸 Application Output

## 🏠 Homepage

![Homepage UI](https://i.ibb.co/CKqJ0Xx9/Screenshot-2026-03-25-185812.png)

---

## ➕ Create Product

![Create Product](https://i.ibb.co/fYvqd8tc/Screenshot-2026-03-25-185654.png)

---

## ✏️ Update Product

![Update Product](https://i.ibb.co/Qv6C9hzT/Screenshot-2026-03-25-185726.png)

---

## 🗑 Delete Product

![Delete Product](https://i.ibb.co/9m4vqNL7/Screenshot-2026-03-25-185710.png)

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/fastapi-crud-project.git
cd fastapi-crud-project
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment

### Windows

```
venv\Scripts\activate
```

### Linux / Mac

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Run FastAPI Server

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 5️⃣ Open Frontend

Open **index.html** in your browser.

---

# 📊 Project Learning Outcomes

Through this project I learned:

- How to build REST APIs using FastAPI
- How frontend communicates with backend APIs
- JSON data storage and handling
- CRUD operation implementation
- Full stack project structure
- API testing and debugging

---

# 🚀 Future Improvements

- Database integration (PostgreSQL / MongoDB)
- Authentication system
- Admin dashboard
- Product image upload
- Pagination & filtering
- Docker deployment

---

# 👨‍💻 Author

**Rudra Prasad Panigrahi**

🎓 B.Tech in Computer Science and Engineering  
🏫 QIS College of Engineering and Technology

💼 Passionate about:

- 🤖 Artificial Intelligence & Machine Learning
- 💻 Full Stack Development
- 🔗 API Development
- 🚀 Building real-world projects

---

# ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork the project
- 📢 Share with others
