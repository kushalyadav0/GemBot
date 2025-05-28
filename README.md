# 🤖 GemBot

**GemBot** is a playful chatbot powered by **Google's Gemini API** and built with **Django**. It's designed for fun conversations, rapid prototyping, and learning how to work with LLMs in real-world apps.

---

## 🚀 Features

- 💬 Gemini-powered chatbot
- 🧠 Smart, quirky responses
- ⚙️ Django backend using Django Templates for UI
- 🧪 Built for experimentation, learning, and laughs

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Templating:** Django Templates (DTL)
- **AI Model:** Google Gemini API

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/gembot.git
cd gembot
```

### 2. Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your-google-gemini-api-key
```

And make sure you're loading this key in your Django settings using `python-dotenv` or `os.environ`.

### 4. Run Migrations & Start Server

```bash
python manage.py migrate
python manage.py runserver
```

Now visit `http://127.0.0.1:8000` and start chatting with GemBot!

---

## 📁 Project Structure

```
gembot/
├── core/         # Django app with chatbot logic
├── core_app/        # Project settings
├── templates/       # HTML templates
├── static/          # CSS/JS 
├── manage.py
├── requirements.txt
```

---

## 📌 Roadmap / TODO

- [ ] Conversation history
- [ ] Better UI/UX
- [ ] Authentication (optional)
- [ ] Deploy on Render / Railway / Heroku

---

## 🤝 Contributing

Feel free to fork the repo, open an issue, or create a pull request. All ideas and contributions are welcome!

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👤 Author

Made with ❤️ by [Kushal Yadav](https://www.linkedin.com/in/kushal-yadav-799310318)
