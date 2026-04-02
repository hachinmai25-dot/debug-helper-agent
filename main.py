import anthropic

# Load agent files
soul = open("SOUL.md").read()
rules = open("RULES.md").read()
skill = open("skills/debug/SKILL.md").read()

system_prompt = f"{soul}\n\n{rules}\n\n{skill}"

client = anthropic.Anthropic()

print("🐛 Debug Helper Agent")
print("Paste your error below (type 'exit' to quit)")
print("-" * 40)

while True:
    error = input("\nYour error: ")
    if error.lower() == "exit":
        break

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=system_prompt,
        messages=[{"role": "user", "content": error}]
    )

    print("\n" + response.content[0].text)
