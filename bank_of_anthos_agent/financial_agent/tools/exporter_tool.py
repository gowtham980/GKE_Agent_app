def export_data(data: str):
    """Exports data to a file."""
    with open("financial_summary.txt", "w") as f:
        f.write(data)
    return "Data exported successfully."