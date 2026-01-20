import re
import os

import yaml

from datetime import datetime
from markdown import markdown

from jinja2 import Environment, FileSystemLoader

# ------------------------------------------------------------------------------
# Environment
# ------------------------------------------------------------------------------

CONTENT_DIR         = os.environ.get('CONTENT_DIR', 'content')
TEMPLATE_DIR        = os.environ.get('TEMPLATE_DIR', 'template')
PUBLIC_DIR          = os.environ.get('PUBLIC_DIR', 'public')
STATIC_DIR          = os.environ.get('STATIC_DIR', 'static')
BASE_TEMPLATE       = os.environ.get('BASE_TEMPLATE', 'base.html')
CONFIG_FILE         = os.environ.get('CONFIG_FILE', 'config.yaml')

# ------------------------------------------------------------------------------
# Utils
# ------------------------------------------------------------------------------

def fread(path):
    with open(path, "r") as f: return f.read()

def fwrite(path, data):
    with open(path, "w") as f: return f.write(data)

# ------------------------------------------------------------------------------
# Builder
# ------------------------------------------------------------------------------

def build_pages():

    pages = []

    def __parse(path):
        content = fread(path)
        pattern = re.compile(r'^---\s*(.*?)\s*---', re.DOTALL)
        match = pattern.search(content)
        if match:
            fm_content = match.group(1)
            fm_dict = yaml.safe_load(fm_content)
            fm_dict.setdefault("template", BASE_TEMPLATE)
            fm_dict.setdefault("last_update", datetime.fromtimestamp(
                os.path.getmtime(path)).strftime('%Y-%m-%d %H:%M'))
            fm_dict["content"] = content[match.end():] 
            fm_dict["url"] = os.path.normpath(
                os.path.relpath(path.replace(".md", ".html"), CONTENT_DIR))
            return fm_dict
        else:
            return {}
                
    def __build(pages):

        for root,_,files in os.walk(CONTENT_DIR):
            for filename in files:
                filepath = os.path.join(root, filename)
                pages.append(__parse(filepath))

        for page in pages:
            t = __env__.get_template(page.get("template", BASE_TEMPLATE))
            html = t.render(site=__site__, pages=pages, page=page)
            path = os.path.join(PUBLIC_DIR, page.get("url", "index.html"))
            if not os.path.exists(os.path.dirname(path)):
                os.makedirs(os.path.dirname(path))
            fwrite(path, html)

    __build(pages)


def build_index_of():

    def __index_of(dirpath, output_file='index.html'):
    
        items = [ f for f in os.listdir(dirpath) if f != "index.html" ]
        html = f"""
        <!DOCTYPE html>
        <html lang="en"><head>
        <meta http-equiv="content-type" content="text/html; charset=UTF-8">
        <meta charset="utf-8">
        <title>Directory listing for {dirpath}</title>
        </head>
        <body>
        <h1>Directory listing for {dirpath}</h1>
        <hr><ul>
        <li><a href="../">../</a></li>
        """
        for item in items: 
            href = os.path.join("/", dirpath, item)
            html += f'<li><a href="{href}">{item}</a></li>\n'
        html += "</ul>\n<hr>\n</body></html>"
        fwrite(output_file, html)

    for root, dirs, files in os.walk(STATIC_DIR):
        path = os.path.join(root, 'index.html')
        __index_of(root, path)

# ------------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------------

def main():

    global __site__
    global __env__

    __site__ = yaml.safe_load(fread(CONFIG_FILE))
    __env__  = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

    def __markdown(data, extensions=['attr_list', 'fenced_code']):
        return markdown(data, extensions=extensions)
    def __now(fmt = "%Y-%m-%d %H:%M"):
        return datetime.now().strftime(fmt)
        
    __env__.filters["markdown"] = __markdown 
    __env__.globals["now"] = __now 

    build_pages()
    build_index_of()

if __name__ == "__main__":

    main()

