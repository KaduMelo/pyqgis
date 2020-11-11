from os import path
from qgis.PyQt import QtWidgets

# definindo path para dir live pyqgis
diretorio = '/media/felipe/DATA/Repos/livepyqgis'

full_path = path.join(diretorio, "dados/imagem_satelite/LS8/PARNASO/L8_20180901_cortado.tif")

if path.isfile(full_path):
    rasterLayer = QgsRasterLayer(full_path, "PARNASO")
    provider = rasterLayer.dataProvider()
    QgsProject.instance().addMapLayer(rasterLayer)
else:
    QtWidgets.QMessageBox.critical(None, "Erro ao adicionar Raster", "Confirme se o path está correto")

# identificando características do raster
rasterLayer.rasterType()
rasterLayer.bandCount()
# características de visualizacao
rasterLayer.renderer().usesBands()
rasterLayer.renderer().type()

# identificar metodos da clase QgsRasterLayer
dir(rasterLayer)

# alterando configuraçãod e contraste
rasterLayer.setDefaultContrastEnhancement()
rasterLayer.setContrastEnhancement(0)
rasterLayer.setContrastEnhancement(1)
rasterLayer.setContrastEnhancement(2)
# outra opcao
rasterLayer.setContrastEnhancement(
    QgsContrastEnhancement.StretchAndClipToMinimumMaximum)
# mais uma :)
rasterLayer.setContrastEnhancement(
    QgsContrastEnhancement.
        contrastEnhancementAlgorithmFromString('StretchToMinimumMaximium'))

# alterando a composicao de visualização da camada
rasterLayer.renderer().setRedBand(4)
rasterLayer.renderer().setGreenBand(1)
rasterLayer.renderer().usesBands()
# atualizando canvas
rasterLayer.triggerRepaint()
rasterLayer.setDefaultContrastEnhancement()

# calculando NDVI
import processing

processing.runAndLoadResults('gdal:rastercalculator',
                             {
                                 'INPUT_A': rasterLayer,
                                 'BAND_A': 4,
                                 'INPUT_B': rasterLayer,
                                 'BAND_B': 1,
                                 'FORMULA': '(A-B)/(A+B)',
                                 'OUTPUT': path.join(diretorio, "NDVI.tif"),
                                 'RTYPE': 5})

NDVI = QgsProject.instance().mapLayersByName('Calculated')[0]

NDVI.renderer().type()

providerNDVI = NDVI.dataProvider()
# calculando estatistica do raster
min = providerNDVI.bandStatistics(1).minimumValue
max = providerNDVI.bandStatistics(1).maximumValue
mean = providerNDVI.bandStatistics(1).mean

# criando rampa de cores na unha!
fcn = QgsColorRampShader()
fcn.setColorRampType(QgsColorRampShader.Interpolated)
fcn.colorRampTypeAsQString()
fcn.classificationMode()

lst = [
    QgsColorRampShader.ColorRampItem(min, QColor(255, 0, 0), '-1'),
    QgsColorRampShader.ColorRampItem(mean, QColor(255, 255, 192), '0'),
    QgsColorRampShader.ColorRampItem(max, QColor(0, 150, 0), '1')]
fcn.setColorRampItemList(lst)
shader = QgsRasterShader()
shader.setRasterShaderFunction(fcn)
renderer = QgsSingleBandPseudoColorRenderer(NDVI.dataProvider(), 1, shader)
NDVI.setRenderer(renderer)
NDVI.triggerRepaint()

# Gerando histograma

hist = QgsRasterHistogramWidget(rasterLayer)
hist.show()
hist.computeHistogram(True)
hist.refreshHistogram()
hist.histoSaveAsImage(path.join(diretorio, "HistogramaRGB.png"))
hist.destroy()

# histograma NDVI

hist = QgsRasterHistogramWidget(NDVI)
hist.show()
hist.computeHistogram(True)
hist.refreshHistogram()
hist.histoSaveAsImage(path.join(diretorio, "HistogramaNDVI.png"))
hist.destroy()
