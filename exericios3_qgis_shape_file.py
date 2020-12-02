iface.addVectorLayer("D://Users//Dell//Downloads//br_municipios_20200807//BR_Municipios_2019.shp", "Municipios do Brasil", "ogr")

municipios = iface.activeLayer()

# Exercício 1
def imprimir_municipios_mg(municipios):
    municipios.setSubsetString("SIGLA_UF = 'MG'")
    print(municipios.featureCount())

imprimir_municipios_mg(municipios)

# Exercício 2
def imprimir_maior_municipio(municipios):
    municipios.setSubsetString("")
    area_territorial = 0
    nome_maior_municipio = ""
    for feature in municipios.getFeatures():
        if feature["AREA_KM2"] >= area_territorial:
            area_territorial = feature["AREA_KM2"]
            nome_maior_municipio = feature["NM_MUN"] + "/" + feature["SIGLA_UF"]
    
    print(nome_maior_municipio, area_territorial)

imprimir_maior_municipio(municipios)

idx = municipios.fields().indexFromName('AREA_KM2')
expression = 'AREA_KM2 = '+ str(municipios.maximumValue(idx))
request = QgsFeatureRequest().setFilterExpression(expression)
for f in municipios.getFeatures(request):
   print ('O maior município é {}, do estado {}, sua extensão é {}'.format(f['NM_MUN'], f['SIGLA_UF'], f['AREA_KM2']))
    
# Exercício 3
def imprimir_estado_mais_municipios(municipios):
    dicionario_estados = {}
    for feature in municipios.getFeatures():
        if feature["SIGLA_UF"] in dicionario_estados:
            dicionario_estados[feature["SIGLA_UF"]] += 1
        else:
            dicionario_estados[feature["SIGLA_UF"]] = 1
            
    print(dicionario_estados)
    
    quantidade_municipios = 0
    nome_estado_com_mais_municipios = ''
    for estado, count in dicionario_estados.items():
        if count >= quantidade_municipios:
            quantidade_municipios = count
            nome_estado_com_mais_municipios = estado + ": " + str(quantidade_municipios)
    
    print(nome_estado_com_mais_municipios)

imprimir_estado_mais_municipios(municipios)

    
