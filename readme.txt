# Document Summarization AI App

Welcome to the Document Summarization AI App! This application allows users to upload a document through a web interface, which is then processed by a FastAPI API. The API reads the content of the file and utilizes a state-of-the-art text summarization model to generate concise summaries. The resulting summary is then displayed on the site, providing users with a quick and efficient way to extract key information from large documents.

## Features

- **User-Friendly Interface**: A simple and intuitive web interface that allows users to upload documents easily.

- **FastAPI Backend**: Powered by FastAPI, a modern, fast (high-performance), web framework for building APIs with Python 3.7+.

- **Text Summarization Model**: Utilizes a text summarization model from the Hugging Face Transformers library to generate meaningful summaries.

## How to Use

1. **Upload a Document**: Visit the home page and use the provided file input to upload a document (supported formats include .txt, .doc, .docx, and .pdf).

2. **Summarize**: Click the "Summarize" button to send the document to the FastAPI API.

3. **View Summary**: The app processes the document using the text summarization model and displays the generated summary on the site.

## Requirements

- Python 3.7+
- FastAPI
- Hugging Face Transformers

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/document-summarization-app.git
