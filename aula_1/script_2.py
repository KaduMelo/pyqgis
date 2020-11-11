import os

from osgeo import ogr

diretorio = "path_to_livepyqgis"

# Caminho até o gpkg base_dados
base_dados = os.path.join(diretorio, "dados/base_dados.gpkg")

print( base_dados )

# Caminho até o gpkg bcim_2016_21_11_2018.gpkg
bcim = os.path.join(diretorio, "dados"
                    , "bcim_2016_21_11_2018.gpkg")

# Testando se o caminho é válido
if os.path.isfile(bcim):
    print( "Arquivo Existente!" )
else:
    print("Arquivo Inexistente!" )

# Pegando o nome da pasta de um arquivo.
caminho = os.path.dirname(bcim)

# Verificando se a camada é Válida
vector_layer = base_dados + "|layername=1104_mg_municipios_pol"

if QgsVectorLayer( vector_layer, "1104_mg_municipios_pol", "ogr" ).isValid():
    print( "Essa camada é válida!" )
else:
    print( "Deu ruim" )
    
# Adicionando Todas as camadas de um GPKG usando subLayers()

arquivo = QgsVectorLayer( bcim , "", "ogr")
if arquivo.isValid():
    print( "yes" )
else:
    print( "Nop" )
    
subLayers = arquivo.dataProvider().subLayers()

for subLayer in subLayers:
    # print( subLayer )
    nome = subLayer.split( "!!::!!" )[1]
    # print( nome )
    uri = "%s|layername=%s" % ( bcim , nome )
    # print( uri )
    # Cria Camada
    sub_vlayer = QgsVectorLayer( uri, nome, 'ogr' )
    # Adiciona a camada ao mapa
    QgsProject.instance().addMapLayer( sub_vlayer )

# Adicionando todas as camadas usando o OSGEO

# Conectando ao gpkg

con = ogr.Open( base_dados )

for camada in con:
    uri = "%s|layername=%s" % ( base_dados , camada.GetName() )
    camadaVetorial = QgsVectorLayer( uri, camada.GetName(), 'ogr' ) 
    QgsProject.instance().addMapLayer( camadaVetorial )

# Atribuir a um objeto uma camada pelo nome
vlayer = QgsProject.instance().mapLayersByName('grade_landsat_mg')[0]
# Dando zoom na camada
iface.mapCanvas().setExtent( vlayer.extent() )
iface.mapCanvas().refresh()
