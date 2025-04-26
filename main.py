import requests
from getTranscript import getVideoTranscript
import os

api_key = os.environ.get("GROQ_API_KEY")
endpoint = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


youtubeLink = input("Enter the youtube link: ")
if youtubeLink:
    fullText = getVideoTranscript(youtubeLink)
    if "Youtube Link Extraction Error" in fullText:
        print(fullText)
        exit()
   
    prompt = f"""You are a professional summarizer. Summarize the following text: 
                {fullText}.
                Make it short and concise.
                Return the summary in the language of the provided youtube transcript.
            """

    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "user", "content": f"{prompt}"}
        ],
        "max_tokens": 2048
    }

    response = requests.post(endpoint, headers=headers, json=data).json()
    print(response['choices'][0]['message']['content'])


