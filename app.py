def get_tide_status(hour):
    if hour % 12 in (0, 6):
        return "High Tide"
    elif hour % 12 in (3, 9):
        return "Low Tide"
    else:
        return "Mid Tide"
