from sympy.polys.benchmarks.bench_galoispolys import p_20

from drug_interaction_project.model.patients import Patient
from drug_interaction_project.tools.validation import Validator

#true value
p1 = Patient("Fatemeh", "Dehghan", "0313176558", ["aspirin", "diazepam"])
print(p1)

#error in national id
try:
    p2= Patient("ali", "rezai" , "031317655" ,["warfarin"])
    print(p2)
except ValueError as e:
    print("intentional error:", e)

#error in name
try:
    p2= Patient("علی", "rezai" , "0313176558" ,["warfarin"])
    print(p2)
except ValueError as e:
    print("intentional error:", e)

#erros in last name
try:
    p2= Patient("ali", "رضایی" , "0313176558" ,["warfarin"])
    print(p2)
except ValueError as e:
    print("intentional error:", e)


