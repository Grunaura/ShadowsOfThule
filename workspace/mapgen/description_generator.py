import random
from faker import Faker
import spacy

faker = Faker()
nlp = spacy.load("en_core_web_sm")

def generate_description(entity, name):
    if entity == "Universe":
        return generate_universe_description()
    elif entity == "Planet":
        return generate_planet_description(name)
    elif entity == "Continent":
        return generate_continent_description(name)
    elif entity == "Country":
        return generate_country_description(name)
    elif entity == "Region":
        return generate_region_description(name)
    elif entity == "State":
        return generate_state_description(name)
    elif entity == "Province":
        return generate_province_description(name)
    elif entity == "City":
        return generate_city_description(name)
    elif entity == "Village":
        return generate_village_description(name)
    elif entity == "Town":
        return generate_town_description(name)
    elif entity == "Landmark":
        return generate_landmark_description(name)
    else:
        return ""

def generate_universe_description():
    return "A vast cosmos"

def generate_planet_description(name):
    return f"A mysterious and enchanting planet called {name} in the far reaches of the universe."

def generate_continent_description(name):
    return f"A continent named {name} rich in history and ancient ruins."

def generate_country_description(name):
    return f"A country known as {name} with its own unique characteristics and cultural heritage."

def generate_region_description(name):
    return f"A region called {name} where you can experience the beauty of nature and the local traditions."

def generate_state_description(name):
    return f"A state named {name} with its own distinct landscapes and connections to the environment."

def generate_province_description(name):
    return f"A province named {name} known for its notable features and contributions."

def generate_city_description(name):
    return f"A bustling city called {name} that offers a vibrant mix of cultures and opportunities."

def generate_village_description(name):
    return f"A peaceful village known as {name} where you can enjoy tranquility and the local community."

def generate_town_description(name):
    return f"A charming town named {name} that captures the essence of small-town life and hospitality."

def generate_landmark_description(name):
    doc = nlp(faker.text())
    sentences = [sent.text for sent in doc.sents]
    return f"A remarkable landmark called {name} that {random.choice(sentences)}"
