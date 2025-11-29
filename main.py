def select_patients(patients, k):
    """
    Select up to k patient names in the order they should be called.

    Patients are dictionaries with:
      - "name": string
      - "severity": integer 1 (most urgent) to 5 (least urgent)
      - "arrival_order": integer, smaller means arrived earlier

    Priority rules:
      1. Lower severity number first.
      2. If severity ties, lower arrival_order first.
    """

    # Step 7: Edge cases
    if k == 0 or not patients:
        return []

    # Step 6: Sort by priority rules
    sorted_patients = sorted(
        patients,
        key=lambda p: (p["severity"], p["arrival_order"])
    )

    # Choose top k and return only names
    return [p["name"] for p in sorted_patients[:k]]
