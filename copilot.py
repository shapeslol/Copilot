import openai
import os
import json

CONFIG_FILE = "copilot_config.json"

def load_key():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f).get("api_key")
    key = input("Enter your OpenAI API key: ").strip()
    with open(CONFIG_FILE, "w") as f:
        json.dump({"api_key": key}, f)
    return key

def copilot_loop(api_key):
    openai.api_key = api_key
    history = []

    print("AI Copilot ready. Type your prompt, or 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        history.append({"role": "user", "content": user_input})

        try:
            res = openai.ChatCompletion.create(
                model="gpt-4",
                messages=history
            )
            reply = res.choices[0].message.content.strip()
            print("Copilot:", reply)
            history.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    key = load_key()
    copilot_loop(key)
