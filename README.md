# Associate AI Engineer: Notes and Projects

This repository holds my notes and projects from the DataCamp Associate AI Engineer course.
The notes are in my own words. The projects are code I built.

> If it is here, I wrote it: my own notes and my own code.

I use this repo to keep the work I do while learning and building with AI. It includes
course-related notes I wrote and projects I built along the way.

---

## What this repo is

- Notes and projects made along with the DataCamp Associate AI Engineer course.
- Notes I wrote in my own words.
- Code projects I built.
- A record of the topics and tools I have worked through.

## What this repo is not

- Not a copy of DataCamp's lessons or solutions. Their content belongs to them.
- Not a collection of production software.

---

## What's inside

### Notes

| Topic | What it covers | Link |
|-------|----------------|------|
| Working on Hugging Face | Local text generation with a Transformers pipeline and GPT-2 | [local_inference.py](./Notes/Working_on_Hugging_Face/local_inference.py) |
| Working on Hugging Face | A provider-based chat completion example using the Hugging Face Inference client | [inferecne_provider.py](./Notes/Working_on_Hugging_Face/inferecne_provider.py) |

### Projects

| # | Project | What it does | Concepts practiced | Status |
|---|---------|--------------|--------------------|--------|
| 01 | [Planning a Trip to Paris with the OpenAI API](./Projects/Project_%20Planning%20a%20Trip%20to%20Paris%20with%20the%20OpenAI%20API) | A notebook that uses OpenAI to answer predefined questions about Paris landmarks and travel | Chat conversations, system prompts, OpenAI chat completions, temperature, token limits | Built |

---

## Skills I'm practicing

- **OpenAI chat completions:** sending conversation messages and reading model responses.
- **Prompting:** setting the Paris guide's role, response limits, and answer style with a system prompt.
- **Model settings:** using `temperature=0.0` and `max_tokens=100`.
- **Python for AI work:** using notebooks, environment variables, and API clients.
- **Hugging Face:** running local text generation and calling a provider through the Inference client.

---

## Project structure

```
associate-ai-engineer-projects/
├── README.md
├── Notes/
│   └── Working_on_Hugging_Face/
│       ├── local_inference.py
│       └── inferecne_provider.py
└── Projects/
    └── Project_ Planning a Trip to Paris with the OpenAI API/
        ├── notebook.ipynb
        └── images/
            ├── connect-integ.png
            ├── eiffel-tower.png
            ├── env-var-details.png
            ├── openai-add-payment-method.png
            ├── openai-create-account.jpeg
            └── openai-new-secret-key.png
```

---

## Run a project

**Requirements:** Jupyter and the Python packages used by the project.
The Paris notebook uses the OpenAI API.

```bash
# 1. Clone the repo
git clone https://github.com/Mustafa786-Python/associate-ai-engineer-projects.git
cd associate-ai-engineer-projects

# 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install the notebook and OpenAI packages
pip install jupyter openai
```

**Add your API key.** Set `OPENAI_API_KEY` in the environment or create a `.env` file
in the project folder:

```
OPENAI_API_KEY=your_key_here
```

Open the Paris notebook:

```bash
jupyter notebook "Projects/Project_ Planning a Trip to Paris with the OpenAI API/notebook.ipynb"
```

The provider inference note uses the Hugging Face endpoint through Together rather
than OpenAI. It reads `HF_TOKEN` from the environment.

> **Never commit your key.** If a key reaches GitHub, delete it and create a new one.

---

## Lessons so far

- A Paris travel conversation can keep system, user, and assistant messages in one ordered list.
- Setting `temperature=0.0` and a `max_tokens` limit keeps the Paris answers more focused.
- Local Hugging Face generation can use a Transformers pipeline.
- A Hugging Face provider example can point Inference calls to Together and the DeepSeek-V3 model.

---

## Roadmap

No future projects or milestones are documented in the repo yet.

---

## Credits

Built while following the DataCamp Associate AI Engineer course. The ideas come from
the course. The notes are in my own words, and the code in this repo is my own.

---

*Last updated: 2026-11-21*
