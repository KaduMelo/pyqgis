from os import path, sep
from qgis.core import ( QgsVectorLayer, QgsApplication, QgsWkbTypes)

# configura caminho ao recursos QGIS
QgsApplication.setPrefixPath('/home/kylefelipe/miniconda3/envs/qgis_34', True)

# Cria referencia a aplicação QGIS
# Segundo argumento desabilita Interface grafica.
qgs = QgsApplication([], False)

# Inicializando e carregando os recursos
qgs.initQgis()

diretorio = "/home/kylefelipe/geocast_repo/livepyqgis/"

# criando caminho ao geopackage
full_path = path.join(diretorio, 'dados/base_dados.gpkg')

# Montando metadados do arquivo
metadado = f"""{'-'*15}METADADOS{'-'*15}"""
metadado += f"""\n\nArquivo: {full_path.split(sep)[-1]}"""
metadado += f"""\n\nConteúdo:"""

# testando se ele existe
if path.isfile(full_path):
    arquivo = QgsVectorLayer( full_path, "test", "ogr")
    # Conectando ao gpkg com dataProvider()
    subLayers = arquivo.dataProvider().subLayers()
    for subLayer in subLayers:
        # print( subLayer )
        nome = subLayer.split( "!!::!!" )[1]
        print( "Nome da layer =", nome )
        uri = "%s|layername=%s" % ( full_path , nome ) # Se o python for 3.6 + pode-se usar f"{full_path}|layername={nome}"
        # Cria Camada
        sub_vlayer = QgsVectorLayer( uri, nome, 'ogr' )
        # quantas feicoes
        print( "Total de feições =", sub_vlayer.featureCount())
        
        # Quantidade de Campos
        qtd_campos = len(sub_vlayer.fields())
        print("Quantidade de campos =", qtd_campos)
        
        # qual geometria
        geometria = QgsWkbTypes.displayString(sub_vlayer.wkbType())
        print( "Geometria =", geometria)
        
        # como pegar geometria
        print( sub_vlayer.wkbType())
        # consulta crs
        print( "SRC =", sub_vlayer.crs().authid(), "\n\n")
        
        # Montando Metadado
        metadado += f"""\n\nCamada = {nome}"""
        metadado += f"""\nTotal de feições = {sub_vlayer.featureCount()}"""
        metadado += f"""\nQuantidade de campos = {qtd_campos}"""
        metadado += f"""\nGeometria = {geometria}"""
        metadado += f"""\nSRC = {sub_vlayer.crs().authid()}"""
else:
    print( "nao deu" )

sPath = full_path.split(sep)
path_Metadados = path.join(diretorio, 'dados', sPath[-1].split('.')[0]+"_metadados.txt")

with open(path_Metadados, 'w') as meta:
    meta.write(metadado)
    print("Metadado gerado com sucesso.")

# fecha recursos
qgs.exitQgis()
