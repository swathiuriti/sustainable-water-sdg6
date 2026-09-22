
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "sdg6_project_2026"


# ---------------- HOME ----------------
@app.route("/")
def home():

    session.clear()

    session["hygiene_score"] = 0
    session["sanitation_score"] = 0
    session["quality_score"] = 0
    session["quiz_score"] = 0
    session["menstrual_score"] = 0
    session["waste_score"] = 0

    return render_template(
        "index.html"
    )
# ---------------- HYGIENE ----------------

@app.route("/hygiene")
def hygiene():
    return render_template("hygiene.html")


@app.route("/submit_hygiene", methods=["POST"])
def submit_hygiene():

    score = 0
    recommendations = []

    if request.form["tank"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Water tanks should be cleaned every 3–6 months."
        )

    if request.form["filter"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Use a water filter to remove impurities."
        )

    if request.form["covered"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Always keep drinking water covered."
        )

    if request.form["vessels"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Clean storage vessels regularly."
        )

    if request.form["boiling"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Boil water when quality is uncertain."
        )

    session["hygiene_score"] = score

    return render_template(
        "result.html",
        score=score,
        recommendation=recommendations
    )


# ---------------- SANITATION ----------------

@app.route("/sanitation")
def sanitation():
    return render_template("sanitation.html")


@app.route("/submit_sanitation", methods=["POST"])
def submit_sanitation():

    score = 0
    recommendations = []

    if request.form["meals"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Wash hands before meals."
        )

    if request.form["toilet"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Wash hands after toilet use."
        )

    if request.form["soap"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Use soap while washing hands."
        )

    if request.form["waste"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Segregate waste properly."
        )

    if request.form["stagnant"] == "Yes":
        score += 2
    else:
        recommendations.append(
            "Remove stagnant water regularly."
        )

    session["sanitation_score"] = score

    return render_template(
        "result.html",
        score=score,
        recommendation=recommendations
    )


# ---------------- QUALITY ----------------

@app.route("/quality")
def quality():
    return render_template("quality.html")


# ---------------- QUIZ ----------------

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")


# ---------------- WASTE ----------------

@app.route("/waste")
def waste():
    return render_template("waste_game.html")


# ---------------- MENSTRUAL ----------------

@app.route("/menstrual")
def menstrual():
    return render_template("menstrual.html")


# ---------------- CHLORINATION ----------------

@app.route("/chlorination")
def chlorination():
    return render_template("chlorination.html")


# ---------------- CALCULATOR ----------------

@app.route("/calculator")
def calculator():
    return render_template("calculator.html")


# ---------------- WATER SAVING ----------------

@app.route("/water-saving")
def water_saving():
    return render_template("water_saving.html")


# ---------------- IMPACT ----------------

@app.route("/impact")
def impact():
    return render_template("impact.html")


@app.route(
"/save_quality",
methods=["POST"]
)
def save_quality():

    session["quality_score"] = int(
        request.form["score"]
    )

    return "ok"



@app.route(
"/save_quiz",
methods=["POST"]
)
def save_quiz():

    session["quiz_score"] = int(
        request.form["score"]
    )

    return "ok"



@app.route(
"/save_menstrual",
methods=["POST"]
)
def save_menstrual():

    session["menstrual_score"] = int(
        request.form["score"]
    )

    return "ok"


@app.route(
"/save_waste",
methods=["POST"]
)
def save_waste():

    session["waste_score"] = int(
        request.form["score"]
    )

    return "ok"





@app.route("/dashboard")
def dashboard():

    return render_template(
        "dashboard.html",

        hygiene=session.get(
            "hygiene_score",
            0
        ),

        sanitation=session.get(
            "sanitation_score",
            0
        ),

        quality=session.get(
            "quality_score",
            0
        ),

        quiz=session.get(
            "quiz_score",
            0
        ),

        menstrual=session.get(
            "menstrual_score",
            0
        ),

        waste=session.get(
            "waste_score",
            0
        )
    )

    return render_template(
        "dashboard.html",
        hygiene=hygiene,
        sanitation=sanitation,
        quality=quality,
        quiz=quiz,
        menstrual=menstrual,
        waste=waste
    )

# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)
gunicorn app:app
