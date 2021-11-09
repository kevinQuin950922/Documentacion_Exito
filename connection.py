from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from dotenv import load_dotenv
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import markdown
import requests
import base64
import os
import json
import pathlib
import sys
sys.path.append ('/home/john-mejia/Documentos/proyecto-final/documentacion_continua_actualizador/repositorios/') 
import repositorios
class ConnectionAz:
    
    def __init__(self,token,organization):
        load_dotenv()
        self.first = True
       

    def clone_or_pull_repos_for_project_id(self,project):
        path = pathlib.Path(project)
        repos = []
        for repo in path.iterdir():
            if repo.is_dir():
                repos.append(project + "/" + repo.name + "-" + repo.name)
        return self.createJsonResponse(repos,project)

    def createJsonResponse(self,repos,project):
        json_repos = {}
        for repo in repos:
            name = repo.split("-")
            json_repo = self.conditionData(name[0])
            json_repos[name[1]] = json_repo
        return json_repos

    def conditionData(self,target_dir):
        
        f = open(f"{target_dir}/readme.html", "r")
        html = f.read()
        soup = BeautifulSoup(html)
        
        # kill all script and style elements
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        # get text
        text = soup.get_text()
        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        contenido = '{"dir_md":"' + target_dir + '/readme.html",'
        estado = False
        for i,line in enumerate(text.splitlines()):
            if i + 1 == len(text.splitlines()):
                if estado and ":" in line:
                    value = line.split(":")
                    if "," in value[1]:
                        items = ""
                        for i,item in enumerate(value[1].split(",")):
                            if i + 1 == len(value[1].split(",")):
                                items += '"' + item + '"'
                            else:
                                items += '"' + item + '",'
                        contenido += '"' + value[0].replace(" ", "") + '":['  + items + ']' + ""
                    elif len(value) > 2:
                        urlDatos = ""
                        for i,item in enumerate(value):
                            if i!=0:
                                urlDatos += urlDatos + item
                        contenido += '"' + value[0].replace(" ", "") + '":"'  + urlDatos.replace(" ","") + '"'
                    else:    
                        contenido += '"' + value[0].replace(" ", "") + '":"'  + value[1] + '"' + ","
                if line == "NOMBRE DE LA INTEGRACIÓN O DEL API":
                    estado=True
                elif line == "Tabla de contenido":
                    estado=False
            else:
                if estado and ":" in line:
                    value = line.split(":")
                    if "," in value[1]:
                        items = ""
                        for i,item in enumerate(value[1].split(",")):
                            if i + 1 == len(value[1].split(",")):
                                items += '"' + item + '"'
                            else:
                                items += '"' + item + '",'
                        contenido += '"' + value[0].replace(" ", "") + '":['  + items + ']' + ","
                    elif len(value) > 2:
                        urlDatos = value[1] + ":" + value[2]
                        contenido += '"' + value[0].replace(" ", "") + '":"'  + urlDatos.replace(" ","") + '"'
                    else:    
                        contenido += '"' + value[0].replace(" ", "") + '":"'  + value[1] + '"' + ","
                if line == "NOMBRE DE LA INTEGRACIÓN O DEL API":
                    estado=True
                elif line == "Tabla de contenido":
                    estado=False
        contenido += "}"
        estado=False
        json_final = json.loads(contenido)
        return json_final

    # # Get the first page of projects
    def startConnect(self):
        dir = "data/repositorios/"
        repositories = pathlib.Path(dir)
        repository = []
        for fichero in repositories.iterdir():
            if fichero.is_dir():
                repository.append(dir + fichero.name + "-" + fichero.name)
        project_info = {}
        for repo in repository:
            divCadena = repo.split("-")
            json_project = self.clone_or_pull_repos_for_project_id(divCadena[0])
            project_info[divCadena[1]] = json_project
        return project_info

