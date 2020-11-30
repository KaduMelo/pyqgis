@qgisfunction(group='MPF 2020')
def showValues(feature, parent):
    names = feature.fields().names()
    values = '\n'.join([ "{}".fomat(n, feature[n]) for n in names ])
    return "# MPF #\n{values}"