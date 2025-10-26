
## 📘 **Flask + MongoDB Atlas Integration Project**

### 🎯 **Objective**

This project demonstrates how to build a simple Flask web application that:

1. Displays an `/api` route that returns a JSON list from a backend file.
2. Provides a frontend form to submit user data (Name and Email).
3. Stores the submitted data in **MongoDB Atlas**.
4. Redirects to a success page upon successful submission.

---

### 🧠 **Features**

* Flask backend with REST API (`/api`)
* MongoDB Atlas integration using **PyMongo**
* Data stored securely via environment variables (`.env`)
* Responsive HTML form with CSS styling
* Separate success page on successful form submission
* JSON data served from a local file (`data.json`)

---

### 🧩 **Tech Stack**

| Component                 | Technology            |
| ------------------------- | --------------------- |
| **Frontend**              | HTML, CSS, JavaScript |
| **Backend**               | Python (Flask)        |
| **Database**              | MongoDB Atlas (Cloud) |
| **Environment Variables** | python-dotenv         |
| **Version Control**       | Git & GitHub          |

---

### 🛠️ **Project Setup**

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

#### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
# or
source venv/bin/activate  # For macOS/Linux
```

#### 3️⃣ Install Dependencies

```bash
pip install flask pymongo python-dotenv
```

#### 4️⃣ Create `.env` File

In the project root folder, create a `.env` file and add your MongoDB URI:

```env
MONGO_URI="mongodb+srv://<username>:<password>@cluster0.xxxx.mongodb.net/<dbname>?retryWrites=true&w=majority"
```

> ⚠️ Never share your `.env` file or commit it to GitHub.
> Add `.env` to your `.gitignore`.

---

### ⚙️ **Run the Flask App**

```bash
python app.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000/
```

---

### 📂 **Project Structure**

```
flask-mongo/
│
├── app.py
├── data.json
├── .env
├── .gitignore
├── templates/
│   ├── index.html
│   └── success.html
└── static/
    └── main.js
```

---

### 🚀 **How It Works**

1. **`/api` Route** – Reads data from `data.json` and returns it as a JSON response.
2. **Frontend Form** – Takes Name & Email from the user.
3. **Form Submission** – Uses JavaScript (AJAX) to send data to `/submit`.
4. **MongoDB Atlas** – Stores the submitted data in the “submissions” collection.
5. **Success Page** – Displays a success message upon successful data insertion.

---

### 🧾 **Screenshots to Attach in Report**

Include the following screenshots in your submission document:

1. MongoDB Atlas cluster & database setup
2. `.env` file (hide credentials)
3. Flask app running in terminal
4. Web form before and after submission
5. Success message page
6. Data visible in MongoDB Atlas collection

---

### 📎 **Submission**

* Upload this project to your GitHub repository.
* Attach the GitHub repo link in your document.
* Add screenshots and explanation in Google Docs or Word file.

---

### 👩‍💻 **Author**

**Sejal Subhash Pawar**

📧 *sejalsubhash1104@gmail.com*

💼 *Aspiring Cloud & Python Developer | AWS Certified | MongoDB Atlas Integration Project*

