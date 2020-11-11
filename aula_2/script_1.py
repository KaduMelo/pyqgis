import os
from pprint import pprint
diretorio = 'path_to_livepyqgis'

# Dicionarios

aurelio = {'ArcGIS': 'Um dos mais reconhecidos e mais caros SIG do mundo', 
           'QGIS': 'Talvez o mais conhecido SIG de código aberto', 
           'GRASS GIS': 'Pouco falado, nas um dos mais poderosos que já ouvi falar'}

# Pegando o significado de QGIS
print(aurelio['QGIS'])

aurelio['GVSIG'] = 'Deve ser interessante, mas nunca usei'

# Modificando um significado de uma chave
aurelio['QGIS'] = 'É o mais falado... e com #PyQGIS, vira uma bazuca!'

# Abrindo o projeto salvo na aula anterior
QgsProject.instance().read(os.path.join(diretorio, 'projetos/projeto1.qgs'))

# acessando layer
uf = QgsProject.instance().mapLayersByName('Estados Brasil lim_unidade_federacao_a')[0]

# identificando propriedades de simbologia
uf.renderer().symbol().symbolLayer(0).properties()

pprint(uf.renderer().symbol().symbolLayer(0).properties())

# salvando esse dicionario para alterar um parametro
dic = uf.renderer().symbol().symbolLayer(0).properties()

pprint(dic)
print(dic)

# alterando parametro para transparente
dic["style"] = "no"

# fazendo update
uf.renderer().setSymbol(QgsFillSymbol.createSimple(dic))
# atualizando canvas
uf.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(uf.id())


# add raster layer
iface.addRasterLayer(os.path.join(diretorio, "dados/BR_SRTM.tif"))

# Para acessa layer por nome:
rlayer = QgsProject.instance().mapLayersByName('BR_SRTM')[0]

# quantos algoritos temos?
len(QgsApplication.processingRegistry().algorithms())

# quais sao eles?
pprint(QgsApplication.processingRegistry().algorithms()[0:10])

# usando processing
import processing

# Conhecendo mais sobre o algoritmo
processing.algorithmHelp("qgis:reprojectlayer")
# executando
projectResult = processing.run('qgis:reprojectlayer', {
'INPUT': uf, 
'TARGET_CRS': 'EPSG:102033',
'OUTPUT': "memory:ufProjected"})
projectResult['OUTPUT'] 
ufProjected = QgsProject.instance().addMapLayer( projectResult['OUTPUT'] )

# vendo CRS
ufProjected.crs().authid()

# processando e carregando

# hillshade
processing.algorithmHelp("qgis:hillshade")
output = os.path.join('/tmp/processing_hillshade.tif')
hillshade = processing.runAndLoadResults('qgis:hillshade',
    {'AZIMUTH': 300,
    'INPUT': input,
    'OUTPUT': output,
    'V_ANGLE': 40,
    'Z_FACTOR': 111120})

# slope
processing.algorithmHelp("gdal:slope")
output = os.path.join('/tmp/processing_slope.tif')
out = processing.runAndLoadResults("gdal:slope",
    { 'INPUT' : input,
    'BAND': 1,
    'SCALE': 111120,
    'AS_PERCENT': False,
    'COMPUTE_EDGES': False,
    'ZEVENBERGEN': False,
    'OUTPUT' : output
    })
