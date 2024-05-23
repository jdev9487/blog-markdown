from flask import Flask
from flask_cors import CORS
import frontmatter as fm
import os
from dateutil.parser import parse

app = Flask(__name__)
CORS(app)

@app.get("/front-matter")
def all_metadata():
    fms = [fm.load(f'markdown/{x}').metadata | {"slug": x.replace(".md", "")} for x in os.listdir("markdown") if x.endswith(".md")]
    for matter in fms:
        matter["date"] = "{:%B %d, %Y}".format(parse(matter["date"]))
    return fms

@app.get("/front-matter/<slug>")
def metadata(slug):
    matter = fm.load(f'markdown/{slug}.md').metadata
    matter["date"] = "{:%B %d, %Y}".format(parse(matter["date"]))
    return matter

@app.get("/markdown/<slug>")
def markdown(slug):
    file = open(f'markdown/{slug}.md', 'r')
    markdown = file.read()
    file.close()
    return markdown

if __name__ == "__main__":
    app.run()