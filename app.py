from flask import Flask, render_template
import random
import string

app = Flask(__name__)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route("/")
def index():
    return "Привет! Это генератор паролей. Перейдите на страницу /generate для получения нового пароля."

@app.route("/generate")
def generate():
    password = generate_password()
    return f"Ваш новый пароль: {password}"

if __name__ == "__main__":
    app.run(debug=True)
