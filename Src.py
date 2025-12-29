from openai import OpenAI
import os

client = OpenAI()

def analyze_code(code: str) -> str:
    prompt = f"""
You are a security assistant. Analyze the following code and explain any security vulnerabilities in clear, simple language.
If no vulnerabilities are present, say so clearly.

Code:
{code}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

def main():
    print("Paste your code (end with an empty line):")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    code = "\n".join(lines)
    result = analyze_code(code)
    print("\nAnalysis:\n")
    print(result)

if __name__ == "__main__":
    main()
