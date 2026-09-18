# AI Chatbot

A Streamlit chatbot powered by Groq and GPT-OSS-20B.

## Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
```

Then run:

```bash
streamlit run app.py
```

## Deploy to Streamlit Community Cloud

1. Push this project to GitHub.
2. Do not upload `.env`.
3. Create a Streamlit Community Cloud app from the GitHub repository.
4. Set the main file to `app.py`.
5. Add `GROQ_API_KEY` under the app's Secrets settings.

## Security

Never commit or share your real API keys. If a key is exposed, revoke/rotate it.
