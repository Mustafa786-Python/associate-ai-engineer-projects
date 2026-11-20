# Associate AI Engineer: Project Log

> Code I wrote while working through the **DataCamp Associate AI Engineer** course.
> One rule for this repo: **if it is here, I built it.**

I learn by building. Watching a lesson tells me a concept exists. Writing the code, breaking it, and fixing it tells me I understand it. This repo is where that second part lives.

Each project here comes from a module of the course. I take the idea, build it myself, and push it with notes on what worked and what broke.

---

## What this repo is

- A record of my hands-on work with LLMs, APIs, and prompt engineering.
- Projects I built on my own, not copied course exercises.
- A log of my progress. Early projects are simple. Later ones get harder.

## What this repo is not

- Not a copy of DataCamp's lessons or solutions. Their content belongs to them.
- Not production software. These are learning projects.

---

## What's inside

| # | Project | What it does | Concepts practiced | Status |
|---|---------|--------------|--------------------|--------|
| 03 | [TODO: Paris travel guide chatbot, if you add it](./03-paris-guide-chatbot) | A chatbot that answers Paris tourist questions as a virtual guide | System, user, and assistant roles; temperature; token limits | [TODO] |

> Edit this table to match the folders you actually have. Delete any row for a project that is not in the repo.

---

## Skills I'm practicing

Keep only the lines that match projects in this repo.

- **OpenAI API:** sending requests, reading responses, managing a conversation with `system`, `user`, and `assistant` roles.
- **Model settings:** controlling randomness with `temperature` and answer length with the token limit.
- **Prompt engineering:** zero-shot, one-shot, and few-shot prompts; chain-of-thought prompts; multi-step prompting.
- **Python for AI work:** clean scripts, environment variables for keys, and readable project structure.

---

## Project structure

```
associate-ai-engineer-projects/
├── README.md
├── .gitignore
├── requirements.txt
├── 01-project-name/
│   ├── main.py
│   └── README.md
├── 02-project-name/
│   ├── main.py
│   └── README.md
└── ...
```

Every project folder has its own short README that explains what the project does and how to run it.

---

## Run a project

**Requirements:** Python 3.10 or newer and an OpenAI API key. The OpenAI API needs a paid balance.

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install the packages
pip install -r requirements.txt
```

**Add your API key.** Create a `.env` file in the project folder:

```
OPENAI_API_KEY=your_key_here
```

Then run a project:

```bash
python3 01-project-name/main.py
```

> **Never commit your key.** `.env` is listed in `.gitignore`. If a key ever reaches GitHub, delete it in the OpenAI dashboard and create a new one.

---

## Lessons so far

Short, honest notes. Add your own as you build.

- [TODO: something that broke and how you fixed it]
- [TODO: a prompt that did not work, and what you changed]
- [TODO: one thing you would do differently next time]

---

## Roadmap

- [ ] [TODO: next module or project]
- [ ] Add a short demo to each project
- [ ] Add tests where they make sense

---

## Credits

Built while following the DataCamp Associate AI Engineer course. The ideas come from the course. The code in this repo is my own.

## License

MIT. See the [LICENSE](./LICENSE) file.

---

*Last updated: [TODO: date]*