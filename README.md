# 🐛 Debug Helper Agent

A calm, developer-friendly AI debugging assistant that explains
not just the fix — but WHY the error happened and how to
prevent it next time.

---

## 🎯 What it does

- Identifies the type of error
- Explains why it happened
- Gives you the fix
- Tells you how to prevent it next time

---

## 🚀 Demo

![Debug Helper Demo](demo.png)

---

## 🛠️ Tech Stack

- Model: LLaMA 3.3 70B (via Groq)
- Runtime: Python
- Agent Structure: SOUL.md + RULES.md + SKILL.md

---

## ⚙️ Setup

### 1. Clone the repository
\```bash
git clone https://github.com/hachinmai25_dot/debug-helper-agent.git
cd debug-helper-agent
\```

### 2. Install dependencies
\```bash
pip install groq python-dotenv
\```

### 3. Get your free Groq API key
```
1. Go to console.groq.com
2. Sign up for free
3. Click API Keys → Create API Key
4. Copy the key
```

### 4. Create your .env file
\```bash
echo "GROQ_API_KEY=gsk_your-key-here" > .env
\```

### 5. Run the agent
\```bash
python main.py
\```

---

## 📁 Project Structure

\```
debug-helper-agent/
├── agent.yaml        # Agent manifest
├── SOUL.md           # Agent personality
├── RULES.md          # Agent rules
├── main.py           # Run the agent
├── .env              # Your API key (never share!)
├── skills/
│   └── debug/
│       └── SKILL.md  # Debug skill
└── tools/
    └── error-analyzer.yaml
\```

---

## 💡 Example

\```
You: TypeError: cannot read properties of undefined (reading 'map')

🤖 Debug Helper:
1. IDENTIFY — This is a TypeError in JavaScript
2. EXPLAIN — You are trying to call .map() on a value that is undefined
3. FIX — Check if the array exists before calling .map()
4. PREVENT — Always initialize arrays with a default empty value []
\```

---

## 🏆 Built for Hackathon

Built with ❤️ using Groq's free API + LLaMA 3.3 70B model

---

## ⚠️ Important

- Never share your `.env` file
- Never push your API key to GitHub
- `.env` is protected by `.gitignore`
