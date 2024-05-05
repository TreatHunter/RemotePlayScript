#! /usr/bin/python3

"""
https://github.com/TreatHunter
This is web ui for remote play script. Its purpose is to control old pc as tvstation to be controlled over ssh
v1.0.0

MIT License

Copyright (c) 2024 TreatHunter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Annotated
from fastapi import FastAPI, Form, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
import subprocess

app = FastAPI(title="api")


@app.post("/api/")
async def home(url: Annotated[str, Form()], regime: Annotated[str, Form()]):
    print(url)
    print(regime)
    subprocess.call(["python3", "prp.py", regime, url])
    return RedirectResponse("/", status_code=status.HTTP_303_SEE_OTHER)


app.mount("/", StaticFiles(directory="static", html=True), name="static")
