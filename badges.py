def get_badge(score):

    if score >= 90:
        return "Water Warrior"

    elif score >= 70:
        return "Eco Guardian"

    elif score >= 50:
        return "Rain Hero"

    else:
        return "Learner"