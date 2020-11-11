"""
Ordenar os pontos a partir do ponto mais ao norte (y).add().add()
E remove anéis internos dos poligonos.
Esse script funciona apenas em geometrias simples.
"""

from collections import namedtuple
from operator import attrgetter

layer = QgsProject.instance().mapLayer('pol_3ef44284_3231_4314_9f8a_aa65232b4c6c')

features = layer.getFeatures()
caps = layer.dataProvider().capabilities()

def ordena_perimetro(perimetro):
    """Ordena o vetor do perimetro passado"""
    Node = namedtuple('Node', ['idx', 'x', 'y'])
    nodes = [Node(perimetro.index(i), i.x(), i.y()) for i in perimetro]
    ponto_mais_ao_norte = sorted(nodes, key=attrgetter('y'), reverse=True)[0].idx
    return [perimetro[ponto_mais_ao_norte:] + perimetro[1:ponto_mais_ao_norte]]

def ordena_poligono(geometria, limpar_aneis=False):
    """Ordena a geometria de uma determinada feição"""
    geometria = geometria.asPolygon()
    geom = ordena_perimetro(geometria[0])
    geometria_ordenada = QgsGeometry.fromPolygonXY(geom)
    if not limpar_aneis:
        if len(geometria) > 1:
            for anel in geometria[1:]:
                geometria_ordenada.addRing(anel)
    return geometria_ordenada

def limpa_anel(geometry):
    """Remove anéis internos da geometria"""
    geometry = geometry.asPolygon()
    return QgsGeometry.fromPolygonXY([geometry[0]])

layer.startEditing()
# Usando ordena_poligono
for feature in features:
   fid = feature.id()
   geom = ordena_poligono(feature.geometry())
   if caps & QgsVectorDataProvider.ChangeGeometries:
       mod = layer.dataProvider().changeGeometryValues({fid : geom})
       print(mod)
   else:
       print(f"Feição fid {fid} não pode ser modificada!")

# Usando limpa_anel
for feature in features:
    fid = feature.id()
    geom = limpa_anel(feature.geometry())
    if caps & QgsVectorDataProvider.ChangeGeometries:
        mod = layer.dataProvider().changeGeometryValues({fid : geom})
        print(mod)
    else:
        print(f"Feição fid {fid} não pode ser modificada!")
layer.commitChanges()
