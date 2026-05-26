EMISSION_FACTORS = {
    "diesel_liter": 2.68,
    "electricity_kwh": 0.82,
    "flight_km": 0.15,
}

def normalize_sap_record(raw):

    fuel = raw.get("Brennstofftyp")

    quantity = float(raw.get("Menge", 0))

    unit = raw.get("Einheit")

    normalized_quantity = quantity

    if unit.lower() in ["l", "liter", "liters"]:
        normalized_unit = "liter"
    else:
        normalized_unit = unit

    co2e = quantity * 2.68

    return {
        "scope": "Scope 1",
        "category": "Fuel",
        "activity_value": quantity,
        "activity_unit": unit,
        "normalized_value": normalized_quantity,
        "normalized_unit": normalized_unit,
        "co2e_kg": co2e,
    }