from typing import ValuesView
import unittest
import json
from unittest import mock
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
    if not(os.path.exists('./repositorioPrueba/prueba/prueba')):
        os.makedirs('./repositorioPrueba/prueba/prueba')
    f = open(f"./repositorioPrueba/prueba/prueba/readme.md", "w")
    f.write('**NOMBRE DE LA INTEGRACIÓN O DEL API**\n')
    f.write('**Área:** Soluciones de Clientes\n')
    f.write('**Analista Ágil:** Juan Guillermo Montoya\n')
    f.write('**Dominio:** Clientes\n')
    f.write('**Proyecto:** Móvil Éxito\n')
    f.write('**Palabras Clave:** redención, PCO, acumulación\n')
    f.write('**Infraestructura de despliegue:** AKS,OKS, GCP, ODI, OSB\n')
    f.write('**Sistemas Origen:** Clifre, Teradata, Sinco \n')
    f.write('**Sistemas Destino:** Clifre, Teradata, Sinco, Kafka\n')
    f.write('**Tipo desarrollo:** Api, Worker, Batch, Modelo, Portal Web, Móvil ** main-pipeline.yml\n')
    f.write('**Versión Lenguaje:** NetCore, Java, Angular, Python, R\n')
    f.write('**URL Consumo Api:** https://wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html\n')
    f.close()

def delete_repo():
    os.remove('./repositorioPrueba/prueba/prueba/readme.html')
    os.remove('./repositorioPrueba/prueba/prueba/readme.md')
    os.rmdir('./repositorioPrueba/prueba/prueba/')
    os.rmdir('./repositorioPrueba/prueba/')
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
        self.assertTrue(os.path.exists("data/repositorios/prueba"))
        os.rmdir('data/repositorios/prueba')

    
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


    # Mock conditionData
    @mock.patch.object(ConnectionAz,'__init__',return_value=None)
    @mock.patch('os.system',return_value=None)
    def test_condition_data(self,mock_conectionaz,mock_system1):
        create_repo()
        data=json.loads('{"value": [{"author": {"date": "2021-11-09T21:41:52Z"}}]}')
        target_dir='./repositorioPrueba/prueba/prueba'
        connection_az=ConnectionAz(None,None)
        connection_az.first=True
        connection_az.personal_access_token="test"
        result=connection_az.conditionData(data,target_dir,None,None,None)
        expected=json.loads('{"dir_md": "./repositorioPrueba/prueba/prueba/readme.html", "Área": " Soluciones de Clientes", "AnalistaÁgil": " Juan Guillermo Montoya", "Dominio": " Clientes", "Proyecto": " Móvil Éxito", "PalabrasClave": [" redención", " PCO", " acumulación"], "Infraestructuradedespliegue": [" AKS", "OKS", " GCP", " ODI", " OSB"], "SistemasOrigen": [" Clifre", " Teradata", " Sinco"], "SistemasDestino": [" Clifre", " Teradata", " Sinco", " Kafka"], "Tipodesarrollo": [" Api", " Worker", " Batch", " Modelo", " Portal Web", " Móvil"], "VersiónLenguaje": [" NetCore", " Java", " Angular", " Python", " R"], "URLConsumoApi": "**https**https//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html"}')
        self.assertAlmostEqual(result,expected)
        self.assertTrue(os.path.exists('./repositorioPrueba/prueba/prueba/readme.html'))
        delete_repo()
