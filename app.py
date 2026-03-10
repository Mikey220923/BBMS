from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# -----------------------------
# DATABASE INITIALIZATION
# -----------------------------
def init_db():
    conn = sqlite3.connect('bloodbank.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            blood_group TEXT NOT NULL,
            contact TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# HOME PAGE
# -----------------------------
@app.route('/')
def home():
    return render_template("index.html")


# -----------------------------
# REGISTER DONOR
# -----------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        blood_group = request.form['blood_group']
        contact = request.form['contact']

        conn = sqlite3.connect('bloodbank.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO donors (name, blood_group, contact) VALUES (?, ?, ?)",
            (name, blood_group, contact)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('view_donors'))

    return render_template("register.html")


# -----------------------------
# VIEW ALL DONORS
# -----------------------------
@app.route('/donors')
def view_donors():
    conn = sqlite3.connect('bloodbank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors")
    data = cursor.fetchall()
    conn.close()

    return render_template("donors.html", donors=data)


# -----------------------------
# SEARCH DONORS
# -----------------------------
@app.route('/search', methods=['GET', 'POST'])
def search():
    results = []

    if request.method == 'POST':
        blood_group = request.form['blood_group']

        conn = sqlite3.connect('bloodbank.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM donors WHERE blood_group = ?",
            (blood_group,)
        )
        results = cursor.fetchall()
        conn.close()

    return render_template("search.html", donors=results)


# -----------------------------
# MAIN
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)

    @app.route('/dashboard')
def dashboard():
    total_donors = len(donors)

    blood_groups = set()
    for donor in donors:
        blood_groups.add(donor['blood_group'])

    total_blood_groups = len(blood_groups)

    return render_template('dashboard.html',
                           total_donors=total_donors,
                           total_blood_groups=total_blood_groups)