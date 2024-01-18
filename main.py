from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from transformers import pipeline
import re

app = FastAPI()
templates = Jinja2Templates(directory="templates")
summarizer = pipeline("summarization")

def clean_text(text):
    # Remove spaces before periods at the end of sentences
    text = re.sub(r'\s+(\.)', r'\1', text)
    # Capitalize the first letter of each sentence
    text = '. '.join(sentence.capitalize() for sentence in text.split('. '))
    return text

@app.get("/", response_class=HTMLResponse)
def index_page(request: Request, summarized_text: str = None):
    return templates.TemplateResponse("index.html", {"request": request, "summarized_text": summarized_text})

@app.post("/summarize/", response_class=HTMLResponse)
async def summarize_text_from_file(file: UploadFile = File(...), request: Request = None):
    if not file.filename.endswith(('.txt', '.doc', '.docx', '.pdf')):
        raise HTTPException(status_code=400, detail="Only text, doc, docx, and pdf files are supported.")

    contents = await file.read()

    try:
        text = contents.decode("utf-8")
        summarized_text = summarizer(text, max_length=250, min_length=100, length_penalty=2.0, num_beams=4, temperature=0.7)[0]['summary_text']
        return index_page(request, summarized_text=clean_text(summarized_text))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing the document: {str(e)}")
