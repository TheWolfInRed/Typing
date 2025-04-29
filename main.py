from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>Simple Typing App</title>
        </head>
        <body>
            <h1>Type something:</h1>
            <textarea rows="10" cols="50"></textarea>
        </body>
    </html>
    """
    return html_content
