import os
import openai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.environ['OPEN_API_KEY']

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)