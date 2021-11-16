from flask import Flask, jsonify, render_template,current_app
from flask.signals import template_rendered
from bs4 import BeautifulSoup
import json
import os
from jinja2 import Environment, FileSystemLoader


template_dir = os.path.abspath("./")
app = Flask(__name__, template_folder = template_dir)

@app.route("/projects/home")
def get_projects():
   with open('data.json') as file:
      jsonData = json.load(file)
   jsonString = json.dumps(jsonData)
   jsonDominio = {}
   for key in jsonData:
      for key2 in jsonData[key]:
         if jsonData[key][key2]['Dominio'] in jsonDominio:
            jsonDominio[jsonData[key][key2]['Dominio']].append(jsonData[key][key2])
         else:
            jsonDominio[jsonData[key][key2]['Dominio']] = [jsonData[key][key2]]
   return render_template("template/index.html", jsonfile=jsonString, jsonDominioString = json.dumps(jsonDominio))

@app.route('/readme', defaults={'path': ''})
@app.route('/readme/<path:path>')
def render_vue(path):
   f = open(path)
   html = f.read()
   soup = BeautifulSoup(html)
   soup.find('ul')['class'] = 'sidebar-links sidebar-group-items'
   for tag in soup.find_all('a'):
      tag['class'] = 'sidebar-link'
      tag['aria-current'] = 'page'
   entrada = soup.find_all('ul')
   contenido = entrada[0]
   return render_template("template/vuepress.html", pathfile=path, contenido_sidebar=contenido)

@app.route("/<path:path>")
def render_file(path):
   return render_template(path)

if __name__ == "__main___":
    app.run()
