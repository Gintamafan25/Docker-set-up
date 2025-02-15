from flask import Flask, render_template, request, redirect, url_for
import json, os

app = Flask(__name__)



# Load menu from file
MENU_FILE = os.path.join("templates", "menu.json")
SERVICE_FILE = os.path.join("templates", "services.json")
def load_file(document):
    try:
        print(f"Attempting to open: {document}")  # Debug print
        with open(document, "r") as file:
            data = json.load(file)
            print(f"Loaded data: {data}")  # Debug print
            return data
    except FileNotFoundError:
        print(f"File not found: {document}")  # Debug print
        return {"empty3": []}
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")  # Debug print
        return {"empty2": []}
    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}")  # Debug print
        return {"empty": []}
def save_menu(menu, document):
    with open(document, "w") as file:
        json.dump(menu, file, indent=4)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    menu_items = load_file(MENU_FILE)
    return render_template("menu.html", menu=menu_items)

@app.route("/services")
def services():
    services = load_file(SERVICE_FILE)
    return render_template("services.html", services=services)

@app.route("/update_menu", methods=["GET", "POST"])
def update_menu():
    if request.method == "POST":
        new_menu = request.form.get("menu")
        menu_list = [item.strip() for item in new_menu.split("\n") if item.strip()]
        save_menu(menu_list)
        return redirect(url_for("menu"))
    return render_template("update_menu.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
