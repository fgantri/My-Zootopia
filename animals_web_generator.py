import json


def main():
    animals_data = load_data('animals_data.json')

    for animal in animals_data:
        pairs = [("Name", animal.get("name"))]
        locations = animal.get("locations")
        if locations is not None and len(locations) > 0:
            pairs.append(("Location", locations[0]))
        if animal["characteristics"] is not None:
            pairs.append(("Diet", animal["characteristics"].get("diet")))
            pairs.append(("Type", animal["characteristics"].get("type")))

        for prop, val in pairs:
            if val is not None:
                print(f"{prop}: {val}")
        print()


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


if __name__ == "__main__":
    main()
