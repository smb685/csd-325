def city_country(city, country, population=None, language=None):
    """Return a string in the format City, Country - population xxx, Language."""
    result = f"{city.title()}, {country.title()}"

    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"

    return result


# Function calls
print(city_country("santiago", "chile", 5000000, "spanish"))
print(city_country("paris", "france", 2148000))
print(city_country("nairobi", "kenya"))
