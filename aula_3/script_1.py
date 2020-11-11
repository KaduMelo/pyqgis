# Pontos
vp = QgsVectorLayer("Point?crs=epsg:31983", "temporary_points", "memory")
QgsProject.instance().addMapLayer(vp)
dpPonto = vp.dataProvider()

# Criando 

ponto1 = QgsPoint(10, 10)
ponto2 = QgsPoint(10, 11)
ponto3 = QgsPoint(11, 11)
ponto4 = QgsPoint(11, 10)

# Criando uma feição para receber uma geometria
feicaoPonto = QgsFeature()

# Adicionando a geometria a feição
feicaoPonto.setGeometry(ponto4)

# Adicionando a feição à camada
dpPonto.addFeature(feicaoPonto)

# Atualizando a extensão da camada.
vp.updateExtents()

# Atualizando o canvas
iface.mapCanvas().setExtent(vp.extent().buffered(0.5))
iface.mapCanvas().refresh()

# Adicionando vários pontos através de uma lista
#lista de pontos
pontos = [ponto1, ponto2, ponto3, ponto4]

for i in pontos:
    feicaoPontos.setGeometry(i)
    dpPonto.addFeature(feicaoPontos)

vp.updateExtents()

iface.mapCanvas().setExtent(vp.extent().buffered(0.1))
iface.mapCanvas().refresh()

for i in pontos[1:]:
    print(f"Distancia entre o ponto 1 e o ponto{pontos.index(i) + 1} é de {pontos[0].distance(i)}")

# Linha

vl = QgsVectorLayer("Linestring?crs=epsg:31983", "temporary_line", "memory")
QgsProject.instance().addMapLayer(vl)
dpLinha = vl.dataProvider()

# Criando uma feição para receber uma geometria
feicaoLinha = QgsFeature()
# Criando a GEOMETRIA
geometria = QgsLineString(pontos)
# Atribuindo a GEOMETRIA a FEIÇÃO
feicaoLinha.setGeometry(geometria)
# Adicionando a FEIÇÃO à camada
dpLinha.addFeature(feicaoLinha)
vl.updateExtents()
iface.mapCanvas().setExtent(vl.extent().buffered(0.5))
iface.mapCanvas().refresh()

# Poligono
vp = QgsVectorLayer("Polygon?crs=epsg:31983", "temporary_polygon", "memory")
QgsProject.instance().addMapLayer(vp)
dpPoligono = vp.dataProvider()

ponto1 = QgsPointXY(10, 10)
ponto2 = QgsPointXY(10, 11)
ponto3 = QgsPointXY(11, 11)
ponto4 = QgsPointXY(11, 10)
#lista de pontos
pontosXY = [ponto1, ponto2, ponto3, ponto4]

# Criando uma feição para receber uma geometria
feicaoPoligono = QgsFeature()

geometria = QgsGeometry.fromPolygonXY([pontosXY])
feicaoPoligono.setGeometry(geometria)
dpPoligono.addFeature(feicaoPoligono)
vp.updateExtents()
iface.mapCanvas().setExtent(vp.extent().buffered(0.5))
iface.mapCanvas().refresh()
