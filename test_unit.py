import unittest
import json
from unittest import mock
import main
from connection import ConnectionAz
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
    f.write('<p><strong>URL Consumo Api:</strong> https://wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html</p>')
    f.write('<h4 id="tabla-de-contenido">Tabla de contenido</h4>')
    f.write('<ul>')
    f.write(
        '<li><a href="#descripción-de-la-necesidad">Descripción de la necesidad</a></li>')
    f.write('<li><a href="#diagrama-de-la-necesidad">Diagrama de la necesidad</a></li>')
    f.write('<li><a href="#clasificacion-de-las-interfaces">Clasificacion de las Interfaces</a></li>')
    f.write('<li><a href="#atributos-de-calidad-de-la-solucion">Atributos de calidad de la solucion</a></li>')
    f.write('<li><a href="#diagrama-de-componentes-de-la-interfaz">Diagrama de componentes de la Interfaz</a></li>')
    f.write('<li><a href="#consideraciones">Consideraciones</a></li>')
    f.write('<li><a href="#mapeo-de-datos">Mapeo de datos</a></li>')
    f.write(
        '<li><a href="#mapeo_movil_exito_bolsillo">Mapeo Movil_Exito_Bolsillo</a></li>')
    f.write(
        '<li><a href="#mapeo_movil_exito_gestores">Mapeo Movil_Exito_Gestores</a></li>')
    f.write('<li><a href="#mapeo_movil_exito_tipoajuste">Mapeo Movil_Exito_Tipoajuste</a></li>')
    f.write('<li><a href="#características-técnicas-de-la-interfaz">Características técnicas de la Interfaz</a></li>')
    f.write('<li><a href="#manejo-de-errores">Manejo de Errores</a></li>')
    f.write('<li><a href="#manejo-de-reproceso">Manejo de reproceso</a></li>')
    f.write('<li>')
    f.write('<p><a href="#manual-de-despliegue">Manual de despliegue</a></p>')
    f.write('</li>')
    f.write('<li>')
    f.write('<p><a href="#inventario-de-artefactos">Inventario de Artefactos</a></p>')
    f.write('</li>')
    f.write('<li><a href="#topologías">Topologías</a> </li>')
    f.write('<li><a href="#directorios">Directorios</a></li>')
    f.write('<li><a href="#Operaciones-de-la-Interfaz-(Servicio)">Operaciones de la Interfaz (Servicio)</a></li>')
    f.write('</ul>')
    f.close()
    f = open(f"./repositorioPrueba/prueba/prueba/readme.md", "w")
    f.close()

# eliminar repositorio


def delete_repo():
    os.remove('./repositorioPrueba/prueba/prueba/readme.html')
    os.remove('./repositorioPrueba/prueba/prueba/readme.md')
    os.rmdir('./repositorioPrueba/prueba/prueba/')
    os.rmdir('./repositorioPrueba/prueba/')
    os.rmdir('./repositorioPrueba')

# Pruebas archivo connection.py


class test_connection(unittest.TestCase):
    # Prueba metodo createJson
    mock_conditionData = json.loads(
        '{"dir_md": "repositorioPrueba/prueba/prueba/readme.html", "Área": " Soluciones de Clientes", "AnalistaÁgil": " Juan Guillermo Montoya", "Dominio": " Clientes", "Proyecto": " Móvil Éxito", "PalabrasClave": [" redención", " PCO", " acumulación"], "Infraestructuradedespliegue": [" AKS", "OKS", " GCP", " ODI", " OSB"], "SistemasOrigen": [" Clifre", " Teradata", " Sinco"], "SistemasDestino": [" Clifre", " Teradata", " Sinco", " Kafka"], "Tipodesarrollo": [" Api", " Worker", " Batch", " Modelo", " Portal Web", " Móvil ** main-pipeline.yml"], "VersiónLenguaje": [" NetCore", " Java", " Angular", " Python", " R"], "URLConsumoApi": "httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html"}')

    @mock.patch.object(ConnectionAz, '__init__', return_value=None)
    @mock.patch.object(ConnectionAz, 'conditionData', return_value=mock_conditionData)
    def test_createJson(self, mock_init, mock_connection):
        except_create_json_response = json.loads(
            '{"prueba": {"dir_md": "repositorioPrueba/prueba/prueba/readme.html", "Área": " Soluciones de Clientes", "AnalistaÁgil": " Juan Guillermo Montoya", "Dominio": " Clientes", "Proyecto": " Móvil Éxito", "PalabrasClave": [" redención", " PCO", " acumulación"], "Infraestructuradedespliegue": [" AKS", "OKS", " GCP", " ODI", " OSB"], "SistemasOrigen": [" Clifre", " Teradata", " Sinco"], "SistemasDestino": [" Clifre", " Teradata", " Sinco", " Kafka"], "Tipodesarrollo": [" Api", " Worker", " Batch", " Modelo", " Portal Web", " Móvil ** main-pipeline.yml"], "VersiónLenguaje": [" NetCore", " Java", " Angular", " Python", " R"], "URLConsumoApi": "httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html"}}')
        create_repo()
        connection_az = ConnectionAz()
        respuesta_create_json_response = connection_az.createJsonResponse(
            ['repositorioPrubeba/prueba/prueba-prueba'], None)
        self.assertTrue(mock_connection)
        self.assertEqual(respuesta_create_json_response,
                         except_create_json_response)
        delete_repo()

    # #Prueba metodo clone_or_pull_repos_for_project_id
    @mock.patch.object(ConnectionAz, '__init__', return_value=None)
    @mock.patch.object(ConnectionAz, 'createJsonResponse', return_value=None)
    def test_clone_or_pull_repos_for_project_id(self, mock_init, mock_create_json_response):
        create_repo()
        conection_az = ConnectionAz()
        conection_az.clone_or_pull_repos_for_project_id(
            'repositorioPrueba/prueba')
        self.assertTrue(mock_init)
        self.assertTrue(mock_create_json_response)
        delete_repo()

    # prueba metodo conditionData
    @mock.patch.object(ConnectionAz, '__init__', return_value=None)
    def test_conditionData(self, mock_init):
        excpect_condition_data = json.loads(
            '{"dir_md":"repositorioPrueba/prueba/prueba/readme.html","Área":" Soluciones de Clientes","AnalistaÁgil":" Juan Guillermo Montoya","Dominio":" Clientes","Proyecto":" Móvil Éxito","PalabrasClave":[" redención"," PCO"," acumulación"],"Infraestructuradedespliegue":[" AKS","OKS"," GCP"," ODI"," OSB"],"SistemasOrigen":[" Clifre"," Teradata"," Sinco"],"SistemasDestino":[" Clifre"," Teradata"," Sinco"," Kafka"],"Tipodesarrollo":[" Api"," Worker"," Batch"," Modelo"," Portal Web"," Móvil ** main-pipeline.yml"],"VersiónLenguaje":[" NetCore"," Java"," Angular"," Python"," R"],"URLConsumoApi":"httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.htmlTabladecontenidoDescripcióndelanecesidadDiagramadelanecesidadClasificaciondelasInterfacesAtributosdecalidaddelasolucionDiagramadecomponentesdelaInterfazConsideracionesMapeodedatosMapeoMovil_Exito_BolsilloMapeoMovil_Exito_GestoresMapeoMovil_Exito_TipoajusteCaracterísticastécnicasdelaInterfazManejodeErroresManejodereprocesoManualdedespliegueInventariodeArtefactosTopologíasDirectoriosOperacionesdelaInterfaz(Servicio)"}')
        create_repo()
        link = 'repositorioPrueba/'
        link = link + os.listdir(link)[0] + '/'
        link = link + os.listdir(link)[0]
        connection_az = ConnectionAz()
        re_condition_data = connection_az.conditionData(link)
        self.assertEqual(re_condition_data, excpect_condition_data)
        self.assertTrue(mock_init)
        delete_repo()

    # Prueba  metodo startConnect
    mock_clone=json.loads('{"prueba": {"dir_md":"repositorioPrueba/prueba/prueba/readme.html","Área":" Soluciones de Clientes","AnalistaÁgil":" Juan Guillermo Montoya","Dominio":" Clientes","Proyecto":" Móvil Éxito","PalabrasClave":[" redención"," PCO"," acumulación"],"Infraestructuradedespliegue":[" AKS","OKS"," GCP"," ODI"," OSB"],"SistemasOrigen":[" Clifre"," Teradata"," Sinco"],"SistemasDestino":[" Clifre"," Teradata"," Sinco"," Kafka"],"Tipodesarrollo":[" Api"," Worker"," Batch"," Modelo"," Portal Web"," Móvil ** main-pipeline.yml"],"VersiónLenguaje":[" NetCore"," Java"," Angular"," Python"," R"],"URLConsumoApi":"httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.htmlTabladecontenidoDescripcióndelanecesidadDiagramadelanecesidadClasificaciondelasInterfacesAtributosdecalidaddelasolucionDiagramadecomponentesdelaInterfazConsideracionesMapeodedatosMapeoMovil_Exito_BolsilloMapeoMovil_Exito_GestoresMapeoMovil_Exito_TipoajusteCaracterísticastécnicasdelaInterfazManejodeErroresManejodereprocesoManualdedespliegueInventariodeArtefactosTopologíasDirectoriosOperacionesdelaInterfaz(Servicio)"}}')
    @mock.patch.object(ConnectionAz, '__init__', return_value=None)
    @mock.patch.object(ConnectionAz,'clone_or_pull_repos_for_project_id',return_value=mock_clone)
    @mock.patch('connection.pathlib.Path',return_value=Path('repositorioPrueba/'))
    def test_startConnect(self, mock_init,mock_path,mock_clone):
        excpect_start_connect=json.loads('{"prueba": {"prueba": {"dir_md":"repositorioPrueba/prueba/prueba/readme.html","Área":" Soluciones de Clientes","AnalistaÁgil":" Juan Guillermo Montoya","Dominio":" Clientes","Proyecto":" Móvil Éxito","PalabrasClave":[" redención"," PCO"," acumulación"],"Infraestructuradedespliegue":[" AKS","OKS"," GCP"," ODI"," OSB"],"SistemasOrigen":[" Clifre"," Teradata"," Sinco"],"SistemasDestino":[" Clifre"," Teradata"," Sinco"," Kafka"],"Tipodesarrollo":[" Api"," Worker"," Batch"," Modelo"," Portal Web"," Móvil ** main-pipeline.yml"],"VersiónLenguaje":[" NetCore"," Java"," Angular"," Python"," R"],"URLConsumoApi":"httpshttps//wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.htmlTabladecontenidoDescripcióndelanecesidadDiagramadelanecesidadClasificaciondelasInterfacesAtributosdecalidaddelasolucionDiagramadecomponentesdelaInterfazConsideracionesMapeodedatosMapeoMovil_Exito_BolsilloMapeoMovil_Exito_GestoresMapeoMovil_Exito_TipoajusteCaracterísticastécnicasdelaInterfazManejodeErroresManejodereprocesoManualdedespliegueInventariodeArtefactosTopologíasDirectoriosOperacionesdelaInterfaz(Servicio)"}}}')
        create_repo()
        connection_az = ConnectionAz()
        project = connection_az.startConnect()
        self.assertEqual(project, excpect_start_connect)
        self.assertTrue(mock_init)
        delete_repo()


#Pruebas al archivo main.py
class MockStartConnect():
    def startConnect(self):
        json_re=json.loads('{"prueba200": {"prueba200": {"dir_md": "data/repositorios/prueba200/prueba200/readme.html", "Área": " Soluciones de Clientes", "AnalistaÁgil": " Juan Guillermo Montoya", "Dominio": " Clientes", "Proyecto": " Móvil Éxito", "PalabrasClave": [" redención", " PCO", " acumulación"], "Infraestructuradedespliegue": [" AKS", "OKS", " GCP", " ODI", " OSB"], "SistemasOrigen": [" Clifre", " Teradata", " Sinco"], "SistemasDestino": [" Clifre", " Teradata", " Sinco", " Kafka"], "Tipodesarrollo": [" Api", " Worker", " Batch", " Modelo", " Portal Web", " Móvil ** main-pipeline.yml"], "VersiónLenguaje": [" NetCore", " Java", " Angular", " Python", " R"], "URLConsumoApi": "https://wolframio.grupo-exito.com/apiew/producto/v1/HLZKHMELSEVH/swagger/index.html"}}}')
        return json_re

class test_main(unittest.TestCase):
    @mock.patch('connection.ConnectionAz',return_value=MockStartConnect())
    @mock.patch('main.render_template',return_value=None)
    def test_get_project(self,mock_connection,mock_render_template):
        re_get_project=main.get_projects()
        self.assertTrue(mock_connection)
        self.assertTrue(mock_render_template)
        self.assertEqual(re_get_project,None)

    @mock.patch('main.render_template',return_value=None)
    def test_render_vue(self,mock_render_template):
        create_repo()
        re_render_vue=main.render_vue('repositorioPrueba/prueba/prueba/readme.html')
        self.assertTrue(mock_render_template)
        self.assertEqual(re_render_vue,None)
        delete_repo()

if __name__ == '__main__':
    unittest.main()
