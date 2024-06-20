# Text Summarization API

This project provides a simple API for text summarization using FastAPI and Hugging Face's Transformers library. The API takes a text input and returns a summarized version of the text.

## Features

- Summarizes input text using state-of-the-art NLP models.
- Allows customization of summary length.

## Requirements

- Python 3.7+
- FastAPI
- Transformers
- Pydantic
- Uvicorn

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/text-summarization-api.git
    cd text-summarization-api
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate    # On Windows use `env\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install fastapi transformers pydantic uvicorn
    ```

## Usage

1. **Run the API server:**
    ```bash
    uvicorn main:app --reload
    ```

2. **Access the API documentation:**
    Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation provided by Swagger UI.

## API Endpoints

### Root Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Description:** Returns a simple greeting message.

### Summarization Endpoint

- **URL:** `/meow`
- **Method:** `POST`
- **Description:** Returns the summarized text based on the input data.

#### Request Body

- `text_data` (string): The text to be summarized.
- `max_l` (integer): The maximum length of the summary.
- `min_l` (integer): The minimum length of the summary.

#### Example Request

```json
{
  "text_data": "Your long text here...",
  "max_l": 100,
  "min_l": 50
}
