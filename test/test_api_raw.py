from drugfyi.api import DrugFYI

with DrugFYI() as api:
    try:
        result = api.get_interaction("warfarin", "aspirin")
        print("خروجی خام API:", result)
    except Exception as e:
        print("خطای دقیق:", e)