import json


def main():
    animals_data = generate_animals_data()
    with open("animals_template.html", "r") as f:
        html_template = f.read().replace(
            "__REPLACE_ANIMALS_INFO__", animals_data)
    with open("animals.html", "w") as f:
        f.write(html_template)



def generate_animals_data():
    output = ""
    animals_data = load_data('animals_data.json')
    for animal in animals_data:
        output += "<li class=\"cards__item\">"
        pairs = [("Name", animal.get("name"))]
        locations = animal.get("locations")
        if locations is not None and len(locations) > 0:
            pairs.append(("Location", locations[0]))
        if animal["characteristics"] is not None:
            pairs.append(("Diet", animal["characteristics"].get("diet")))
            pairs.append(("Type", animal["characteristics"].get("type")))

        for prop, val in pairs:
            if val is not None:
                output += f"{prop}: {val}<br>"
        output += "</li>"
    return output


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


if __name__ == "__main__":
    main()
