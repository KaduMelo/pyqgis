# criando um arquivo simples
# A camada terá o mesmo nome do arquivo

camada = iface.activeLayer()
caminho_arquivo = 'Caminho para a pasta'

opcoes = QgsVectorFileWriter.SaveVectorOptions() # Instancia da Sub Classe

opcoes.layerName = "nome_da_camada"
opcoes.actionOnExistingFile = QgsVectorFileWriter.ActionOnExistingFile.CreateOrOverwriteLayer

_writer = QgsVectorFileWriter.writeAsVectorFormat(camada, # Obrigatório
                                                caminho_arquivo, # Obrigatório
                                                opcoes
                                                )
if _writer[0] == QgsVectorFileWriter.NoError:
    print(_writer)
    print("Arquivo Salvo com sucesso!")
else:
    print(_writer)
