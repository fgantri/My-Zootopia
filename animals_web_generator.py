import json


def main():
    """ generates html file based on template and json data """
    animals_data = generate_animals_data()
    with open("animals_template.html", "r") as f:
        html_template = f.read().replace(
            "__REPLACE_ANIMALS_INFO__", animals_data)
    with open("animals.html", "w") as f:
        f.write(html_template)


def generate_animals_data():
    """ Generates template string for animal data interpolation """
    output = ""
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        # get animal props if they exist else None and collect them into tuple pairs
        pairs = [("Name", animal.get("name"))]
        locations = animal.get("locations")
        if locations is not None and len(locations) > 0:
            pairs.append(("Location", locations[0]))
        if animal["characteristics"] is not None:
            pairs.append(("Diet", animal["characteristics"].get("diet")))
            pairs.append(("Type", animal["characteristics"].get("type")))

        # construct template string
        output += "<li class=\"cards__item\">"
        _, name = pairs[0]
        if name is not None:
            output += f"<div class=\"card__title\">{name}</div>"
        for prop, val in pairs:
            output += "<p class=\"card__text\">"
            if val is None:
                continue
            output += f"<strong>{prop}:</strong> {val}<br/>"

    return output + "</p></li>"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


if __name__ == "__main__":
    main()
