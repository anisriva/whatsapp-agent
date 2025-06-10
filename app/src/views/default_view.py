from fastapi import Request
from app.src.config.app import get_templates

'''
$ desc   : Home View
$ route  : GET /
$ access : PUBLIC
'''
def home_view(request: Request):
    templates = get_templates()
    return templates.TemplateResponse("index.html", {"request": request})
