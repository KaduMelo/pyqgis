import os

diretorio = "path_to_livepyqgis"

raster = os.path.join( diretorio, "dados" , "BR_SRTM.tif" )
rlayer = QgsRasterLayer( raster , "BR_SRTM" )

# Usando o addMapLayer()
QgsProject.instance().addMapLayer( rlayer )

# Usando iface
iface.addRasterLayer( raster , "BR_SRTM_2" )

# Adicionando camadas sem exibição habilitada
QgisProject.instance().addMapLayers( rlayer, False )

# Para removermos uma camada, usando Python, o método `removeMapLayer()`:
QgsProject.instance().addMapLayer( rlayer.id() )

# Buscando dados do raster

# Pegar resolução do raster
rLayer.width() , rLayer.height()

# Extensão do raster
rLayer.extent()
rLayer.extent().toString()

# Tipo do raster 0 = GrayOrUndefined (single band), 1 = Palette (single band), 2 = Multiband
rLayer.rasterType()

# Contando as bandas do raster
rLayer.bandCount()
