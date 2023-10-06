import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Function to read text from a file
def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to generate questions from text
def generate_questions(text):
    # Customize the prompt to instruct the model to generate questions
    prompt = f"Generate questions based on the following text, and make it more brief: \n{text}\n\nQuestions:\n1. "
    
    # Generate questions using the OpenAI GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        n=20,
        api_key=api_key  # Pass the API key
    )
    
    # Extract and return the generated questions
    questions = response.choices[0].text.strip()
    
    return questions

# Replace 'your_text_file.txt' with the path to your text file
file_path = 'output_file_2.txt'

# Read text from the text file
extracted_text = read_text_from_file(file_path)

# Generate questions from the extracted text
generated_questions = generate_questions(extracted_text)

# Print the generated questions
print(generated_questions)

# Define the file path where you want to save the questions
file_path = "generated_questions.txt"

# Open the file for writing
with open(file_path, "w", encoding="utf-8") as file:
    # Write the generated questions to the file
    file.write(generated_questions)

print(f"Generated questions have been saved to {file_path}")


