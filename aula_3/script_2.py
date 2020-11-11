# Pontos
vp = QgsVectorLayer("Point?crs=epsg:31983", "temporary_points", "memory")
QgsProject.instance().addMapLayer(vp)
dpPonto = vp.dataProvider()

campos = [QgsField('id_feature', QVariant.Int),
        QgsField('nome', QVariant.String),
        QgsField('x', QVariant.Double),
        QgsField('y', QVariant.Double)]

res = vp.dataProvider().addAttributes(campos)
vp.updateFields()

# Criando 

ponto1 = QgsPoint(10, 10)
ponto2 = QgsPoint(10, 11)
ponto3 = QgsPoint(11, 11)
ponto4 = QgsPoint(11, 10)

pontos = [ponto1, ponto2, ponto3, ponto4]


# Adicionando a geometria a feição

for i in pontos:
    # Criando uma feição para receber uma geometria
    feicaoPonto = QgsFeature(vp.fields())
    feicaoPonto.setGeometry(i)
    atributos = [pontos.index(i), f'Ponto {pontos.index(i)} ', i.x(), i.y()]
    feicaoPonto.setAttributes(atributos)
    dpPonto.addFeature(feicaoPonto)
    

# Atualizando a extensão da camada.
vp.updateExtents()

# Atualizando o canvas
iface.mapCanvas().setExtent(vp.extent().buffered(0.5))
iface.mapCanvas().refresh()
