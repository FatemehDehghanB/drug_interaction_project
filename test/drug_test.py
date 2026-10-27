from drug_interaction_project.model.drugs import Drug

#true value
d1= Drug("aspirin")
print(d1)

#error in drug name
try:
    d2= Drug("آسپرین")
    print(d2)
except ValueError as e:
    print("Intentional error:", e)