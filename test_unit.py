import unittest
from json import load
from unittest import mock

from flask import flash
from flask.app import Flask
import main
import tempfile
import os
import pathlib
from pathlib import Path

# carpeta temporal con repositorios


def create_repo():
    if not(os.path.exists('./repositorioPrueba/prueba/prueba')):
        os.makedirs('./repositorioPrueba/prueba/prueba')
    f = open(f"./repositorioPrueba/prueba/prueba/readme.html", "w")
    f.write('<p><strong>NOMBRE DE LA INTEGRACIÓN O DEL API</strong></p>\n')
    f.write('<p><strong>Área:</strong> Soluciones de Clientes</p>\n')
    f.write('<p><strong>Analista Ágil:</strong> Juan Guillermo Montoya</p>\n')
    f.write('<p><strong>Dominio:</strong> Clientes</p>\n')
    f.write('<p><strong>Proyecto:</strong> Móvil Éxito</p>\n')
    f.write('<p><strong>Palabras Clave:</strong> redención, PCO, acumulación</p>\n')
    f.write(
        '<p><strong>Infraestructura de despliegue:</strong> AKS,OKS, GCP, ODI, OSB</p>\n')
    f.write('<p><strong>Sistemas Origen:</strong> Clifre, Teradata, Sinco </p>\n')
    f.write('<p><strong>Sistemas Destino:</strong> Clifre, Teradata, Sinco, Kafka</p>\n')
    f.write('<p><strong>Tipo desarrollo:</strong> Api, Worker, Batch, Modelo, Portal Web, Móvil ** main-pipeline.yml</p>\n')
    f.write(
        '<p><strong>Versión Lenguaje:</strong> NetCore, Java, Angular, Python, R</p>\n')
    f.write('<p><strong>URL Consumo Api:</strong> https://wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html</p>\n')
    f.write('<h4 id="tabla-de-contenido">Tabla de contenido</h4>\n')
    f.write('<ul>')
    f.write(
        '<li><a href="#descripción-de-la-necesidad">Descripción de la necesidad</a></li>\n')
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
    f = open(f"./repositorioPrueba/prueba/prueba/readme.md", "w")
    f.close()

def create_json():
    if not(os.path.exists('./prueba_data/prueba')):
        os.makedirs('./prueba_data/prueba')
    f = open(f"./prueba_data/prueba/data.json", "w")
    f.write('{\n')
    f.write('"prueba400": {\n')
    f.write('    "prueba400": {\n')
    f.write('        "dir_md": "repositorioPrueba/prueba/prueba/readme.html",\n')
    f.write('        "\u00c1rea": "Area prueba",\n')
    f.write('        "Analista\u00c1gil": "Analista prueba",\n')
    f.write('        "Dominio": "Dominio prueba",\n')
    f.write('        "Proyecto": "proyecto prueba",\n')
    f.write('        "PalabrasClave": "Palabras prueba",\n')
    f.write('        "Infraestructuradedespliegue": "Infraestructura prueba",\n')
    f.write('        "SistemasOrigen": "Sistema origen prueba",\n')
    f.write('        "SistemasDestino": "Sistema destino prueba",\n')
    f.write('        "Tipodesarrollo": "Desarrollo de  prueba",\n')
    f.write('        "Versi\u00f3nLenguaje": "Lenguaje de  prueba",\n')
    f.write('        "URLConsumoApi": "Url de prueba"\n')
    f.write('    }\n')
    f.write('}\n')
    f.write('}\n')
    f.close()

# eliminar repositorio
def delete_repo():
    os.remove('./repositorioPrueba/prueba/prueba/readme.html')
    os.remove('./repositorioPrueba/prueba/prueba/readme.md')
    os.rmdir('./repositorioPrueba/prueba/prueba/')
    os.rmdir('./repositorioPrueba/prueba/')
    os.rmdir('./repositorioPrueba')

def delete_json():
    os.remove('./prueba_data/prueba/data.json')
    os.rmdir('./prueba_data/prueba/')
    os.rmdir('./prueba_data')

# Pruebas archivo connection.py
# class test_connection(unittest.TestCase):
#     # Prueba metodo createJson
#     mock_conditionData = json.loads(
#         '{"dir_md": "repositorioPrueba/prueba/prueba/readme.html", "Área": " Soluciones de Clientes", "AnalistaÁgil": " Juan Guillermo Montoya", "Dominio": " Clientes", "Proyecto": " Móvil Éxito", "PalabrasClave": [" redención", " PCO", " acumulación"], "Infraestructuradedespliegue": [" AKS", "OKS", " GCP", " ODI", " OSB"], "SistemasOrigen": [" Clifre", " Teradata", " Sinco"], "SistemasDestino": [" Clifre", " Teradata", " Sinco", " Kafka"], "Tipodesarrollo": [" Api", " Worker", " Batch", " Modelo", " Portal Web", " Móvil ** main-pipeline.yml"], "VersiónLenguaje": [" NetCore", " Java", " Angular", " Python", " R"], "URLConsumoApi": "httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html"}')

#     @mock.patch.object(ConnectionAz, '__init__', return_value=None)
#     @mock.patch.object(ConnectionAz, 'conditionData', return_value=mock_conditionData)
#     def test_createJson(self, mock_init, mock_connection):
#         except_create_json_response = json.loads(
#             '{"prueba": {"dir_md": "repositorioPrueba/prueba/prueba/readme.html", "Área": " Soluciones de Clientes", "AnalistaÁgil": " Juan Guillermo Montoya", "Dominio": " Clientes", "Proyecto": " Móvil Éxito", "PalabrasClave": [" redención", " PCO", " acumulación"], "Infraestructuradedespliegue": [" AKS", "OKS", " GCP", " ODI", " OSB"], "SistemasOrigen": [" Clifre", " Teradata", " Sinco"], "SistemasDestino": [" Clifre", " Teradata", " Sinco", " Kafka"], "Tipodesarrollo": [" Api", " Worker", " Batch", " Modelo", " Portal Web", " Móvil ** main-pipeline.yml"], "VersiónLenguaje": [" NetCore", " Java", " Angular", " Python", " R"], "URLConsumoApi": "httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html"}}')
#         create_repo()
#         connection_az = ConnectionAz()
#         respuesta_create_json_response = connection_az.createJsonResponse(
#             ['repositorioPrubeba/prueba/prueba-prueba'], None)
#         self.assertTrue(mock_connection)
#         self.assertEqual(respuesta_create_json_response,
#                          except_create_json_response)
#         delete_repo()

#     # #Prueba metodo clone_or_pull_repos_for_project_id
#     @mock.patch.object(ConnectionAz, '__init__', return_value=None)
#     @mock.patch.object(ConnectionAz, 'createJsonResponse', return_value=None)
#     def test_clone_or_pull_repos_for_project_id(self, mock_init, mock_create_json_response):
#         create_repo()
#         conection_az = ConnectionAz()
#         conection_az.clone_or_pull_repos_for_project_id(
#             'repositorioPrueba/prueba')
#         self.assertTrue(mock_init)
#         self.assertTrue(mock_create_json_response)
#         delete_repo()

#     # prueba metodo conditionData
#     @mock.patch.object(ConnectionAz, '__init__', return_value=None)
#     def test_conditionData(self, mock_init):
#         excpect_condition_data = json.loads(
#             '{"dir_md":"repositorioPrueba/prueba/prueba/readme.html","Área":" Soluciones de Clientes","AnalistaÁgil":" Juan Guillermo Montoya","Dominio":" Clientes","Proyecto":" Móvil Éxito","PalabrasClave":[" redención"," PCO"," acumulación"],"Infraestructuradedespliegue":[" AKS","OKS"," GCP"," ODI"," OSB"],"SistemasOrigen":[" Clifre"," Teradata"," Sinco"],"SistemasDestino":[" Clifre"," Teradata"," Sinco"," Kafka"],"Tipodesarrollo":[" Api"," Worker"," Batch"," Modelo"," Portal Web"," Móvil ** main-pipeline.yml"],"VersiónLenguaje":[" NetCore"," Java"," Angular"," Python"," R"],"URLConsumoApi":"httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.htmlTabladecontenidoDescripcióndelanecesidadDiagramadelanecesidadClasificaciondelasInterfacesAtributosdecalidaddelasolucionDiagramadecomponentesdelaInterfazConsideracionesMapeodedatosMapeoMovil_Exito_BolsilloMapeoMovil_Exito_GestoresMapeoMovil_Exito_TipoajusteCaracterísticastécnicasdelaInterfazManejodeErroresManejodereprocesoManualdedespliegueInventariodeArtefactosTopologíasDirectoriosOperacionesdelaInterfaz(Servicio)"}')
#         create_repo()
#         link = 'repositorioPrueba/'
#         link = link + os.listdir(link)[0] + '/'
#         link = link + os.listdir(link)[0]
#         connection_az = ConnectionAz()
#         re_condition_data = connection_az.conditionData(link)
#         self.assertEqual(re_condition_data, excpect_condition_data)
#         self.assertTrue(mock_init)
#         delete_repo()

#     # Prueba  metodo startConnect
#     mock_clone=json.loads('{"prueba": {"dir_md":"repositorioPrueba/prueba/prueba/readme.html","Área":" Soluciones de Clientes","AnalistaÁgil":" Juan Guillermo Montoya","Dominio":" Clientes","Proyecto":" Móvil Éxito","PalabrasClave":[" redención"," PCO"," acumulación"],"Infraestructuradedespliegue":[" AKS","OKS"," GCP"," ODI"," OSB"],"SistemasOrigen":[" Clifre"," Teradata"," Sinco"],"SistemasDestino":[" Clifre"," Teradata"," Sinco"," Kafka"],"Tipodesarrollo":[" Api"," Worker"," Batch"," Modelo"," Portal Web"," Móvil ** main-pipeline.yml"],"VersiónLenguaje":[" NetCore"," Java"," Angular"," Python"," R"],"URLConsumoApi":"httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.htmlTabladecontenidoDescripcióndelanecesidadDiagramadelanecesidadClasificaciondelasInterfacesAtributosdecalidaddelasolucionDiagramadecomponentesdelaInterfazConsideracionesMapeodedatosMapeoMovil_Exito_BolsilloMapeoMovil_Exito_GestoresMapeoMovil_Exito_TipoajusteCaracterísticastécnicasdelaInterfazManejodeErroresManejodereprocesoManualdedespliegueInventariodeArtefactosTopologíasDirectoriosOperacionesdelaInterfaz(Servicio)"}}')
#     @mock.patch.object(ConnectionAz, '__init__', return_value=None)
#     @mock.patch.object(ConnectionAz,'clone_or_pull_repos_for_project_id',return_value=mock_clone)
#     @mock.patch('connection.pathlib.Path',return_value=Path('repositorioPrueba/'))
#     def test_startConnect(self, mock_init,mock_path,mock_clone):
#         excpect_start_connect=json.loads('{"prueba": {"prueba": {"dir_md":"repositorioPrueba/prueba/prueba/readme.html","Área":" Soluciones de Clientes","AnalistaÁgil":" Juan Guillermo Montoya","Dominio":" Clientes","Proyecto":" Móvil Éxito","PalabrasClave":[" redención"," PCO"," acumulación"],"Infraestructuradedespliegue":[" AKS","OKS"," GCP"," ODI"," OSB"],"SistemasOrigen":[" Clifre"," Teradata"," Sinco"],"SistemasDestino":[" Clifre"," Teradata"," Sinco"," Kafka"],"Tipodesarrollo":[" Api"," Worker"," Batch"," Modelo"," Portal Web"," Móvil ** main-pipeline.yml"],"VersiónLenguaje":[" NetCore"," Java"," Angular"," Python"," R"],"URLConsumoApi":"httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.htmlTabladecontenidoDescripcióndelanecesidadDiagramadelanecesidadClasificaciondelasInterfacesAtributosdecalidaddelasolucionDiagramadecomponentesdelaInterfazConsideracionesMapeodedatosMapeoMovil_Exito_BolsilloMapeoMovil_Exito_GestoresMapeoMovil_Exito_TipoajusteCaracterísticastécnicasdelaInterfazManejodeErroresManejodereprocesoManualdedespliegueInventariodeArtefactosTopologíasDirectoriosOperacionesdelaInterfaz(Servicio)"}}}')
#         create_repo()
#         connection_az = ConnectionAz()
#         project = connection_az.startConnect()
#         self.assertEqual(project, excpect_start_connect)
#         self.assertTrue(mock_init)
#         delete_repo()


#Pruebas al archivo main.py      

class test_main(unittest.TestCase):
    @mock.patch('main.open', mock.mock_open())
    @mock.patch('main.render_template',return_value=None)
    def test_get_project(self,mock_render_template):
        create_json()
        with mock.patch('main.json.load',return_value=load(open('prueba_data/prueba/data.json'))) as mock_json:
            re_get_project=main.get_projects()
            self.assertTrue(mock_render_template)
            self.assertTrue(mock_json)
            self.assertEqual(re_get_project,None)
            delete_json()


    @mock.patch('flask.flash',return_value=None)
    @mock.patch('main.render_template',return_value=None)
    def test_render_vue(self,mock_render_template,mock_flash):
        create_repo()
        create_json()
        with mock.patch('main.json.load',return_value=load(open('prueba_data/prueba/data.json'))) as mock_json:
            re_render_vue=main.render_vue('./repositorioPrueba/prueba/prueba/readme.html')
            self.assertTrue(mock_render_template)
            self.assertEqual(re_render_vue,None)
            delete_repo()
            delete_json()

if __name__ == '__main__':
    unittest.main()
