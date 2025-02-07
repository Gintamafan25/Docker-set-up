from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Load menu from file
MENU_FILE = "menu.json"
def load_menu():
    try:
        with open(MENU_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_menu(menu):
    with open(MENU_FILE, "w") as file:
        json.dump(menu, file, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    menu_items = load_menu()
    return render_template("menu.html", menu=menu_items)

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/update_menu", methods=["GET", "POST"])
def update_menu():
    if request.method == "POST":
        new_menu = request.form.get("menu")
        menu_list = [item.strip() for item in new_menu.split("\n") if item.strip()]
        save_menu(menu_list)
        return redirect(url_for("menu"))
    return render_template("update_menu.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
