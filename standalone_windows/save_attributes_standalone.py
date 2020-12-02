from os import path
from qgis.core import QgsVectorLayer, QgsApplication, QgsWkbTypes

# QgsApplication.setPrefixPath('/home/kylefelipe/miniconda3/envs/qgis_34', True)

qgis = QgsApplication([], False)

qgis.initQgis()

# Lembre-se de mudar conforme o ambiente que estiver trabalhando
diretorio = "D://Users//Dell//Downloads"
arquivoFisico = 'base_dados.gpkg'

# Caminho completo para o GPKG
full_path = path.join(diretorio, arquivoFisico)

# Acessando as camadas do GEOPACKAGE


metadado = f"""{'-'*15}METADADOS{'-'*15}"""
metadado += f"\n\nArquivo: {arquivoFisico}"
metadado += f"\n\nConteúdo:"

if path.isfile(full_path):
    arquivo = QgsVectorLayer(full_path, "test", "ogr")
    sub_layers = arquivo.dataProvider().subLayers()
    for subLayer in sub_layers:
        # Pegando o nome da camada
        nome = subLayer.split('!!::!!')[1]
        print('Nome da Camada =', nome)
        uri = f"{full_path}|layername={nome}"
        subCamada = QgsVectorLayer(uri, nome, "ogr")
        
        # Quantidade de Feições 
        qt_feicoes = subCamada.featureCount()
        print(f'Quantidade de feições: {qt_feicoes}')
        
        # Quantos campos
        qtd_campos = len(subCamada.fields()) 
        print(f"Quantidade de campos = {qtd_campos}")
        
        # Tipo de geometria
        tp_geometria = QgsWkbTypes.displayString(subCamada.wkbType())
        print(f"Geometria = {tp_geometria}")
        
        # SRC
        subSrc = subCamada.crs().authid()
        print(f"SRC = {subSrc}")
        
        metadado += f"\n\nNome Camada: {nome}"
        metadado += "\nTotal de Feições: {0}".format(qt_feicoes)
        metadado += "\nQuantidade de Campos: %d" % (qtd_campos)
        metadado += f"\nGeometria: {tp_geometria}"
        metadado += f"\nSRC: {subSrc}"
else:
    print('Seu caminho tem algo errado!!!')

nomeMetadado = arquivoFisico.split('.')[0]+"_METADADOS.txt"
caminhoMetadado = path.join(diretorio, nomeMetadado)

with open(caminhoMetadado, 'w') as meta:
    meta.write(metadado)
    print('Metadado Criado Lindamente!')

#print(caminhoMetadado)

qgis.exitQgis()
