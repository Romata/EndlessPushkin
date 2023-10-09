import requests
import random
import os
#API Key for https://makersuite.google.com/app/home
my_secret = os.environ['PaLM-API-Key']
# Get a poetry string from Google Bard using the API
def get_poetry_string():
  response = requests.get("https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText", 
    params={"key": my_secret, "prompt": "Write a poem in the style of Alexander Pushkin", "temperature": 0.7, "max_tokens": 100, "language": "ru"}
  )
  poetry_string = response.json()["text"]
  return poetry_string

# Generate a continuous output of poetry strings
def generate_continuous_output():
  while True:
    poetry_string = get_poetry_string()
    print(poetry_string)

# Fine-tune the poetry generated by Google Bard using the dataset provided by the app
def fine_tune_poetry(poetry_string):
  # Load the dataset
  dataset = []
  with open("vysotskiy.txt", "r") as f:
    for line in f:
      dataset.append(line.strip())

  # Train a language model on the dataset
  model = train_language_model(dataset)

  # Generate a new poetry string using the fine-tuned model
  new_poetry_string = generate_poetry_string(model)

  return new_poetry_string

# Deploy the web app to Replit
def deploy_web_app():
  # Create a new Replit project
  replit_project = requests.post("https://api.replit.com/projects", json={
    "name": "Endless Vysotskiy",
    "language": "python"
  })

  # Get the Replit project URL
#  replit_project_url = replit_project.json()["url"]

  # Push the code to the Replit project
  #requests.post(f"https://api.replit.com/projects/{replit_project_url}/files/main.py", data=open("main.py", "rb"))

  # Start the Replit project
  #requests.post(f"https://api.replit.com/projects/{replit_project_url}/run")

if __name__ == "__main__":
  # Fine-tune the poetry generated by Google Bard using the dataset provided by the app
  #poetry_string = fine_tune_poetry(get_poetry_string())

  # Generate a continuous output of poetry strings
  generate_continuous_output()