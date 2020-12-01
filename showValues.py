@qgsfunction(args='auto', group='Custom')
def showValues(feature, parent):
    names = feature.fields().names()
    values = '\n'.join([ "{} : {}".format(n, feature[n]) for n in names ])
    return "# MPF #\n{}".format(values)