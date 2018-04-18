def grade(score):
    if score<60:
        return "F"
    if score<=69 and score >=60:
        return "D"
    if score<=79 and score >=70:
        return "C"
    if score<=89 and score >=80:
        return "B"
    if score<=100 and score >=90:
        return "A"

cut=100
a = grade(cut)
print a,cut
