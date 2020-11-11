# -*- coding=utf-8 -*-

from os import path
from qgis.PyQt import QtWidgets # Para abrir uma janela de erro para o usuario.
diretorio = "path_to_livepyqgis"

# Complementando o caminho até o arquivo
caminho = str('[%caminho%]').split(', ')
full_path = path.join(diretorio, *caminho, '[%arquivo%]')

# Verificando se o arquivo existe na pasta, antes de adicionar ao QGIS
if path.isfile(full_path):
    rasterLayer = QgsRasterLayer(full_path, '[%cena%]' )
    # Pegando o provedor de dados para configurar o simbologia, transparência, etc.
    provider = rasterLayer.dataProvider()
    if '[%composicao%]'== 'BS': # Verificando se o campo "composicao" da feição é 'BS'
        provider.setNoDataValue(1, 0) # Configurando o valor NO DATA da camada para 0
    QgsProject.instance().addMapLayer(rasterLayer)
else:
    # Caso o arquivo não exista, mostrar uma mensagem de erro.
    QtWidgets.QMessageBox.critical(None, "Erro ao adicionar raster", f"Nenhum raster para a órbita {[%path%]} ponto {[%row%]} foi encontrado.")
