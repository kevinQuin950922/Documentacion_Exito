from flask import Flask, jsonify, render_template,current_app,flash,redirect,request
from flask.signals import template_rendered
from bs4 import BeautifulSoup
import json
import os
from jinja2 import Environment, FileSystemLoader
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.sansio.request import Request
import requests
import re
import copy







template_dir = os.path.abspath("./")
app = Flask(__name__, template_folder = template_dir)
app.secret_key = 'secret-key'

@app.route("/projects/home")
def get_projects():
   try:
     with open('data/data.json') as file:
      jsonData = json.load(file)
   except FileNotFoundError:
    return render_template("template/spinner.html")

   jsonString = copy.deepcopy(jsonData)
   jsonDominio = {}
   for key in jsonData:
      # remove the project if is empty
      if jsonData[key] == {}:
         jsonString.pop(key, None)
         continue
      for key2 in jsonData[key]:
         
         # when the repo exist but there is no any file inside it
         if jsonData[key][key2] == {}:
            jsonString[key].pop(key2, None)
            continue

         if jsonData[key][key2]['Dominio'] in jsonDominio:
            jsonDominio[jsonData[key][key2]['Dominio']].append(jsonData[key][key2])
         else:
            jsonDominio[jsonData[key][key2]['Dominio']] = [jsonData[key][key2]]
   # after remove repositories with have no data now convert it to json string
   jsonString = json.dumps(jsonString)
   return render_template("template/index.html", jsonfile=jsonString, jsonDominioString = json.dumps(jsonDominio))

@app.route('/readme', defaults={'path': ''})
@app.route('/readme/<path:path>')
def render_vue(path):
   NoneType = type(None)
   with open('data/data.json') as file:
      jsonData = json.load(file)
      jsonString = json.dumps(jsonData)
      jsonDominio = {}
      for key in jsonData:
       for key2 in jsonData[key]:
         
         # avoid fail when repo is empty
         if jsonData[key][key2] == {}:
            continue

         if jsonData[key][key2]['Dominio'] in jsonDominio:
            jsonDominio[jsonData[key][key2]['Dominio']].append(jsonData[key][key2])
         else:
            jsonDominio[jsonData[key][key2]['Dominio']] = [jsonData[key][key2]]
            
   print (path + "este es el path")

   try:
    f = open(path)
    html = f.read()
   except FileNotFoundError as e:
            flash(f"Archivo readme.MD no encontrado", "Aviso!!!")
            print (e)
            return  redirect("/projects/home")

   try: 
      soup = BeautifulSoup(html)

      #### section to fix Readme.html that doesn't have the "tabla de contenido" inside <ul> tag
      tagIndexTitle = soup.find('p', text= "TABLA DE CONTENIDO")
      if tagIndexTitle:
         # find all <p> with text that start with enumeration
         tagIndexList = soup.findAll('p', text= re.compile('^[0-9]+[\.]'))

         # replace >p> with <li> and wrap into new <ul>
         ulTag = soup.new_tag("ul")
         for tag in tagIndexList:

            # to ensure that is the index list, check the <p> wrap an <a> and the href start with "#"
            existHref = tag.findChild('a', href = re.compile('^[\#]'))
            if existHref:
               tag.name = 'li'
               ulTag.append(tag)

         # auxiliar div to wrap <h3> title  and <ul>
         auxTag = soup.new_tag("div")
         newTagTitle = soup.new_tag("h3", id= "tabla-de-contenido", string= "Tabla de contenido" )
         auxTag.append(newTagTitle)
         auxTag.append(ulTag)

         # Replace axuiliar div into the current title <p>
         tagIndexTitle.replace_with(auxTag)
         auxTag.unwrap()
      ####

      soup.find('ul')['class'] = 'sidebar-links sidebar-group-items'
      for tag in soup.find_all('a'):
        tag['class'] = 'sidebar-link'
        tag['aria-current'] = 'page'
      entrada = soup.find_all('ul')
      contenido = entrada[0]
      
   except Exception as e:
      flash(f"Archivo readme.MD no compatible", "Aviso!!!")
      return  redirect("/projects/home")
      
   return render_template("template/vuepress.html", pathfile=path, contenido_sidebar=contenido)
   
@app.route("/<path:path>")
def render_file(path):
    try:
     return render_template(path)
    except FileNotFoundError:
     return render_template("template/notfound.html")

app.errorhandler(HTTPException)
def internal_error(error):
    return "error", 500
 
app.errorhandler(NotFound)
def internal_error(error):
    return "error no encontrado", 501
 
 
 
 
 
@app.before_request
def get_referer():
   with open('data/data.json') as file:
      jsonData = json.load(file)
      jsonString = json.dumps(jsonData)
      referrer = request.headers.get("Referer")

     
            
         
            
         
      
      

   conection=request.headers.get("Conection")
   print(conection)
   
   
   
   
   


if __name__ == "__main___":
   app.run()
    




    



