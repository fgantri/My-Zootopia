from data_fetcher import fetch_data


def main():
  animal_name = input("Please enter an animal: ")
  rendered_results = render_animals_result(animal_name)
  render_animals_results_page(rendered_results)


def render_animals_results_page(rendered_animals):
  with open("animals_template.html", "r") as f:
    html = f.read()

  with open("animals.html", "w") as f:
    render_content = html.replace("__REPLACE_ANIMALS_INFO__", rendered_animals)
    f.write(render_content)
  print("Successfully rendered results in animals.html!")


def render_animals_result(animal_query):
  animals = fetch_data(animal_query)
  
  if len(animals) == 0:
    return f"<h2>The animal \"{animal_query}\" doesn't exist.</h2>"
  
  out = ""
  for animal in animals:
    locations = animal["locations"]
    location = locations[0] if len(locations) > 0 else None
    out += f"""
    <li class="cards__item">
      <div class="card__title">{animal["name"]}</div>
      <p class="card__text">
        <strong>Diet:</strong> {animal["characteristics"].get("diet")}<br/>
        <strong>Location:</strong> {location}<br/>
        <strong>Type:</strong> {animal["characteristics"].get("type")}<br/>
      </p>
    </li>
    """
  return out


if __name__ == "__main__":
  main()
