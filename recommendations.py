def get_recommendations(score):

    if score >= 80:
        return "Excellent water hygiene practices."

    elif score >= 50:
        return "Improve tank cleaning and filtration."

    else:
        return "Immediate improvements recommended in water hygiene and sanitation."