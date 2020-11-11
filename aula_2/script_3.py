from os import path

diretorio = "path_to_livepyqgis"

# criando caminho ao geopackage
full_path = path.join(diretorio, 'dados/base_dados.gpkg')

# testando se ele existe
if path.isfile(full_path):
    arquivo = QgsVectorLayer( full_path, "test", "ogr")
    # Conectando ao gpkg com dataProvider()
    subLayers = arquivo.dataProvider().subLayers()
    for subLayer in subLayers:
        #print( subLayer )
        nome = subLayer.split( "!!::!!" )[1]
        print( "Nome da layer =", nome )
        uri = f"{full_path}|layername={nome}" # Se o python for 3.6
        # Cria Camada
        sub_vlayer = QgsVectorLayer( uri, nome, 'ogr' )
        # quantas feicoes
        print( "Total de feições =", sub_vlayer.featureCount())
        # Quantidade de Campos
        qtd_campos = len(sub_vlayer.fields())
        print("Quantidade de campos =", qtd_campos)
        # qual geometria
        print( "Geometria =", QgsWkbTypes.displayString(sub_vlayer.wkbType()))
        # consulta crs
        print( "SRC =", sub_vlayer.crs().authid(), "\n\n")
else:
    print( "Geopackage não existe\n\n" )
