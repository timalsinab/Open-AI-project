import openai
import os
import requests

api_key = os.environ.get("OPEN_API_KEY")
if api_key is None:
    raise ValueError("API key not found. Please set the OPEN_API_KEY environment variable.")

openai.api_key = api_key


prompt = "What are your strengths and weaknesses?"

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    print("OpenAI Response:")
    print(response.choices[0].message['content'].strip())

except openai.error.AuthenticationError as e:
    print(f"Authentication error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


joke_api_url = "https://official-joke-api.appspot.com/random_joke"

try:
    joke_response = requests.get(joke_api_url)
    joke_response.raise_for_status()  
    joke_data = joke_response.json()

    
    print("\nRandom Joke:")
    print(f"{joke_data['setup']} - {joke_data['punchline']}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the GET request: {e}")
