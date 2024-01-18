from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from transformers import pipeline

app = FastAPI()

summarizer = pipeline("summarization")

@app.get("/")
def read_root():
    return """
    <html>
        <head>
            <title>Document Summarizer</title>
        </head>
        <body>
            <h1>Document Summarizer</h1>
            <form action="/summarize/" method="post" enctype="multipart/form-data">
                <label for="file">Upload a document:</label>
                <input type="file" name="file" accept=".txt, .doc, .docx, .pdf" required>
                <button type="submit">Summarize</button>
            </form>
        </body>
    </html>
    """

@app.post("/summarize/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(('.txt', '.doc', '.docx', '.pdf')):
        raise HTTPException(status_code=400, detail="Only text, doc, docx, and pdf files are supported.")

    contents = await file.read()

    try:
        text = contents.decode("utf-8")
        summarized_text = summarizer(text, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, temperature=0.7)[0]['summary_text']
        return {"original_text": text, "summarized_text": summarized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing the document: {str(e)}")


