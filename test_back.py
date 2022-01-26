from typing import ValuesView
import unittest
import json
from unittest import mock
from defer import return_value
from msrest.authentication import BasicAuthentication
from azure.devops.connection import Connection
import tempfile
import os
import pathlib
from pathlib import Path
from ActualizadorAzureDevops import ConnectionAz
import time
import requests

## Creacion de repo
def create_repo():
    if not(os.path.exists('./repositorioPrueba/prueba/prueba/documentacion')):
        os.makedirs('./repositorioPrueba/prueba/prueba/documentacion')
    f = open(f"./repositorioPrueba/prueba/prueba/documentacion/readme.html", "w")
    f.write('<p><strong>NOMBRE DE LA INTEGRACIÓN O DEL API</strong></p>\n')
    f.write('<p><strong>Área:</strong> Soluciones de Clientes</p>\n')
    f.write('<p><strong>Analista Ágil:</strong> Juan Guillermo Montoya</p>\n')
    f.write('<p><strong>Dominio:</strong> Clientes</p>\n')
    f.write('<p><strong>Proyecto:</strong> Móvil Éxito</p>\n')
    f.write('<p><strong>Palabras Clave:</strong> redención, PCO, acumulación</p>\n')
    f.write('<p><strong>Infraestructura de despliegue:</strong> AKS,OKS, GCP, ODI, OSB</p>\n')
    f.write('<p><strong>Sistemas Origen:</strong> Clifre, Teradata, Sinco </p>\n')
    f.write('<p><strong>Sistemas Destino:</strong> Clifre, Teradata, Sinco, Kafka</p>\n')
    f.write('<p><strong>Tipo desarrollo:</strong> Api, Worker, Batch, Modelo, Portal Web, Móvil ** main-pipeline.yml</p>\n')
    f.write('<p><strong>Versión Lenguaje:</strong> NetCore, Java, Angular, Python, R</p>\n')
    f.write('<p><strong>URL Consumo Api:</strong> https://wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html</p>\n')
    f.write('<h4 id="tabla-de-contenido">Tabla de contenido</h4>\n')
    f.write('<ul>')
    f.write('<li><a href="#descripción-de-la-necesidad">Descripción de la necesidad</a></li>\n')
    f.write('<li><a href="#diagrama-de-la-necesidad">Diagrama de la necesidad</a></li>\n')
    f.write('<li><a href="#clasificacion-de-las-interfaces">Clasificacion de las Interfaces</a></li>\n')
    f.write('<li><a href="#atributos-de-calidad-de-la-solucion">Atributos de calidad de la solucion</a></li>\n')
    f.write('<li><a href="#diagrama-de-componentes-de-la-interfaz">Diagrama de componentes de la Interfaz</a></li>\n')
    f.write('<li><a href="#consideraciones">Consideraciones</a></li>\n')
    f.write('<li><a href="#mapeo-de-datos">Mapeo de datos</a></li>\n')
    f.write('<li><a href="#mapeo_movil_exito_bolsillo">Mapeo Movil_Exito_Bolsillo</a></li>\n')
    f.write('<li><a href="#mapeo_movil_exito_gestores">Mapeo Movil_Exito_Gestores</a></li>\n')
    f.write('<li><a href="#mapeo_movil_exito_tipoajuste">Mapeo Movil_Exito_Tipoajuste</a></li>\n')
    f.write('<li><a href="#características-técnicas-de-la-interfaz">Características técnicas de la Interfaz</a></li>\n')
    f.write('<li><a href="#manejo-de-errores">Manejo de Errores</a></li>\n')
    f.write('<li><a href="#manejo-de-reproceso">Manejo de reproceso</a></li>\n')
    f.write('<li>\n')
    f.write('<p><a href="#manual-de-despliegue">Manual de despliegue</a></p>\n')
    f.write('</li>\n')
    f.write('<li>\n')
    f.write('<p><a href="#inventario-de-artefactos">Inventario de Artefactos</a></p>\n')
    f.write('</li>\n')
    f.write('<li><a href="#topologías">Topologías</a> </li>\n')
    f.write('<li><a href="#directorios">Directorios</a></li>\n')
    f.write('<li><a href="#Operaciones-de-la-Interfaz-(Servicio)">Operaciones de la Interfaz (Servicio)</a></li>\n')
    f.write('</ul>\n')
    f.close()

def delete_repo():
    if (os.path.exists('./repositorioPrueba/prueba/prueba/documentacion/readme.html')):
        os.remove('./repositorioPrueba/prueba/prueba/documentacion/readme.html')
    if (os.path.exists('./repositorioPrueba/prueba/prueba/documentacion/readme.md')):
        os.remove('./repositorioPrueba/prueba/prueba/documentacion/readme.md')
    os.rmdir('./repositorioPrueba/prueba/prueba/documentacion')
    os.rmdir('./repositorioPrueba/prueba/prueba')
    os.rmdir('./repositorioPrueba/prueba')
    os.rmdir('./repositorioPrueba')

##  Mock Class
class mock_core_client:
    def get_projects():
        return m_get_projects

class m_get_projects:
    value=[{"test":"test"}]
    continuation_token=None

class Mock_get_repositories:
    def get_repositories(id):
        return id

class Mock_connection:
    class clients:
        def get_git_client():
            return Mock_get_repositories

class Mock_get_project:
    id="321513213151"
    name="prueba"

class Mock_request:
    class content:
        def decode(valor):
            return '{"Hola":"hola"}'

class Mock_request_condition:
    status_code = 400
    content=None





class test_actualizador_azure_devops(unittest.TestCase):

    @mock.patch.object(ConnectionAz,'__init__',return_value=None)
    @mock.patch.object(ConnectionAz,'clone_or_pull_repos_for_project_id',return_value=None)
    @mock.patch('time.sleep',return_value=None)
    @mock.patch.object(ConnectionAz,'saveJson',return_value=None)
    def test_start_connect (self,mock_connectionaz,mock_clone,mock_time,mock_savejson):
        connection_az=ConnectionAz(None,None)
        connection_az.core_client=mock_core_client
        connection_az.startConnect()
        self.assertTrue(mock_time)
        self.assertTrue(mock_savejson)
        self.assertTrue(mock_clone)


    #test clone_or_pull_repos_for_project_id
    @mock.patch.object(ConnectionAz,'__init__',return_value=None)
    @mock.patch.object(ConnectionAz,'createJsonResponse',return_value=None)
    def test_clone_or_pull_repos_for_project_id(self,mock_connectionaz,mock_create):
        connection_az=ConnectionAz(None,None)
        connection_az.connection=Mock_connection
        connection_az.personal_access_token='token'
        connection_az.clone_or_pull_repos_for_project_id(Mock_get_project)
        self.assertTrue(mock_create)
        self.assertTrue(os.path.exists("./../documentacion_continua/data/repositorios/prueba"))
        os.rmdir('./../documentacion_continua/data/repositorios/prueba')

    
    #test CreateJsonResponse
    @mock.patch.object(ConnectionAz,'__init__',return_value=None)
    @mock.patch('os.path.join',return_value='prueba')
    @mock.patch('requests.get',return_value=Mock_request)
    @mock.patch.object(ConnectionAz,'conditionData',return_value=None)
    def test_create_json_response(self,mock_connectionaz,mock_path,mock_request,mock_conditiondata):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic '+'prueba'
        }
        prueba_project=Mock_get_project
        prueba_repos=[prueba_project]
        connection_az=ConnectionAz(None,None)
        connection_az.organization_url='prueba'
        connection_az.project_info={}
        connection_az.createJsonResponse(headers,prueba_repos,prueba_project)
        self.assertTrue(os.path.exists("prueba"))
        self.assertTrue(mock_conditiondata)
        os.rmdir('prueba')
    
    #test conditionDataJson
    @mock.patch.object(ConnectionAz,'__init__',return_value=None)
    def test_conditionDataJson(self,mock_connectionaz):
        create_repo()
        connection_az=ConnectionAz(None,None)
        connection_az.contenido={}
        expected=json.loads('{"dir_md": "./prueba/documentacion/readme.html", "Área": " Soluciones de Clientes", "AnalistaÁgil": " Juan Guillermo Montoya", "Dominio": " Clientes", "Proyecto": " Móvil Éxito", "PalabrasClave": [" redención", " PCO", " acumulación"], "Infraestructuradedespliegue": [" AKS", "OKS", " GCP", " ODI", " OSB"], "SistemasOrigen": [" Clifre", " Teradata", " Sinco"], "SistemasDestino": [" Clifre", " Teradata", " Sinco", " Kafka"], "Tipodesarrollo": [" Api", " Worker", " Batch", " Modelo", " Portal Web", " Móvil ** main-pipeline.yml"], "VersiónLenguaje": [" NetCore", " Java", " Angular", " Python", " R"], "URLConsumoApi": "https://wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html"}')
        result=connection_az.conditionDataJson("./repositorioPrueba/prueba/prueba")
        self.assertAlmostEqual(result,expected)
        delete_repo()
    
    #test conditionData
    @mock.patch.object(ConnectionAz,'__init__',return_value=None)
    @mock.patch('os.system',return_value=None)
    #@mock.patch('requests.get',return_value=Mock_request_condition)
    def test_condition_data(self,mock_conectionaz,mock_system1):
        create_repo()
        data=json.loads('{"value": [{"author": {"date": "2021-11-09T21:41:52Z"}}]}')
        target_dir='./repositorioPrueba/prueba/prueba'
        url="https://dev.azure.com/grupo-exito/GCIT-Agile/_apis/git/repositories/mis-premios-cloud-function/items?path=/documentacion/&$format=zip&download=true"
        headers=json.loads('{"Accept": "application/json", "Authorization": "Basic Omc1dHE3eTRoZGI0bmM2NWFzZ2t2enF6Z3B5YzdveHB1czd3cTRtNWVrNGIycHJ0dXZ3YXE="}')
        name_project="GCIT-Agile"
        name_repo="mis-premios-cloud-function"
        connection_az=ConnectionAz(None,None)
        connection_az.first=True
        connection_az.personal_access_token="test"
        result=connection_az.conditionData(data,target_dir, url, headers, name_project, name_repo)
        expected=json.loads('{"dir_md": "./prueba/documentacion/readme.html", "Dominio": "Default", "Proyecto": "Default", "Área": "Default", "AnalistaÁgil": "Default", "PalabrasClave": "Default", "Infraestructuradedespliegue": "Default", "SistemasOrigen": "Default", "SistemasDestino": "Default", "Tipodesarrollo": "Default", "VersiónLenguaje": "Default", "URLConsumoApi": "Default"}')
        self.assertAlmostEqual(result,expected)
        self.assertTrue(os.path.exists('./repositorioPrueba/prueba/prueba/documentacion/readme.html'))
        delete_repo()
