# Carregando um dado vetorial
iface.addVectorLayer("/path_to_livepyqgis/dados/bcim_2016_21_11_2018.gpkg|layername=lim_unidade_federacao_a", "Estados Brasil", "ogr")
# atribuindo a camada ativa a um objeto
uf = iface.activeLayer()
# contado as feições desse objeto
uf.featureCount()
# identificando os campos da camada
for field in uf.fields():
    print(field.name())

print(uf.fields()[0].name())

# Print dos valores de cada feição para o campo "nome"
for feature in uf.getFeatures():
    print(feature["nome"])

# abrindo tabela de atributos:
iface.showAttributeTable(uf)

# filtrando por uma string
uf.setSubsetString("nome = 'Rio de Janeiro'")
# Para dar zoom ao resultado
iface.zoomToActiveLayer()
# para desfazer o filtro
uf.setSubsetString("")

# alterando a cor
uf.renderer().symbol().setColor(QColor("black"))
# atualizando o canvas
uf.triggerRepaint()
# atualizando a simbologia na lista de camadas
iface.layerTreeView().refreshLayerSymbology(uf.id())

# Salvando o projeto
QgsProject.instance().write('/path_to_folder/livepyqgis/projetos/projeto1.qgs')

print(QgsProject.instance().fileName())
