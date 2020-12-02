import sys, os, pathlib

from qgis.PyQt.QtCore import QObject, pyqtSignal
from qgis.core import (
    Qgis, QgsApplication, QgsProject,
    QgsVectorLayer,
    QgsTask, QgsTaskManager
)

layer = None
def getDescriptionFilesList(sourcePath, statusBar):
    def getTotalDirs():
        total = 0
        for root, _dirs, _files in os.walk( sourcePath ):
            if os.path.split( root )[-1][0] == '.':
                continue
            total += 1
        return total
        
    filesDesc = []
    totalDirs = getTotalDirs()
    countDirs = 0
    for root, _dirs, files in os.walk( sourcePath ):
        if os.path.split( root )[-1][0] == '.':
            continue
        countDirs += 1
        msg = f"{countDirs} of {totalDirs}"
        statusBar.showMessage( msg )
        for f in files:
            if f[0] == '.':
                continue
            path_file = pathlib.Path( os.path.join( root, f ) )
            if path_file.is_symlink():
                continue
            size = path_file.stat().st_size
            item = ( f, root, os.path.splitext( f )[1][1:], size )
            filesDesc.append( item )
    return filesDesc

def getDescriptionFilesListTask(task, sourcePath, statusBar):
    def getTotalDirs():
        total = 0
        for root, _dirs, _files in os.walk( sourcePath ):
            if os.path.split( root )[-1][0] == '.':
                continue
            if task.isCanceled():
                return None
            total += 1
        return total
        
    filesDesc = []
    totalDirs = getTotalDirs()
    if totalDirs is None:
        return None
    countDirs = 0
    for root, _dirs, files in os.walk( sourcePath ):
        if os.path.split( root )[-1][0] == '.':
            continue
        if task.isCanceled():
            return None
        #if countDirs == 200:
            # 2 / 0
            #raise Exception('bad value!')
        countDirs += 1
        msg = f"{countDirs} of {totalDirs}"
        statusBar.messageChanged.emit( msg )
        for f in files:
            if f[0] == '.':
                continue
            path_file = pathlib.Path( os.path.join( root, f ) )
            if path_file.is_symlink():
                continue
            size = path_file.stat().st_size
            item = ( f, root, os.path.splitext( f )[1][1:], size )
            filesDesc.append( item )
    return filesDesc

def saveDescriptionFilesList( pathFile, filesDesc):
    with open( pathFile, mode='w') as w_file:
        line = "name,path,ext,size_bytes\n"
        w_file.write( line )
        for item in filesDesc:
            line = "{}\n".format( ','.join( [ str( v ) for v in item ] ) ) # List Comprehensions
            w_file.write( line )

    global layer

    project = QgsProject.instance()
    if not layer is None:
        project.removeMapLayers( [ layer.id() ] )

    layer = QgsVectorLayer( pathFile, 'descript_files', 'ogr' )
    project.addMapLayer( layer )

def run(iface, sourcePath, pathFile):
    statusBar = iface.mainWindow().statusBar()
    statusBar.clearMessage()
    filesDesc = getDescriptionFilesList( sourcePath, statusBar )
    saveDescriptionFilesList (pathFile, filesDesc )
    del filesDesc[:]
    msg = "Saved {}".format( pathFile )
    iface.messageBar().pushMessage( 'DescriptionFiles', msg, Qgis.Info )

def runTask(iface, sourcePath, pathFile):
    def finished(exception, result=None):
        if not exception is None:
            msg = "Exception: {}".format( exception )
            iface.messageBar().pushMessage( 'DescriptionFiles', msg, Qgis.Critical )
            return
        if result is None:
            msg = "Canceled by user"
            iface.messageBar().pushMessage( 'DescriptionFiles', msg, Qgis.Warning )
            return
        saveDescriptionFilesList ( pathFile, result )
        del result[:]
        msg = "Saved {}".format( pathFile )
        iface.messageBar().pushMessage( 'DescriptionFiles', msg, Qgis.Info )
    
    statusBar = iface.mainWindow().statusBar()
    statusBar.clearMessage()
    task = QgsTask.fromFunction(
        'DescriptionFiles',
        getDescriptionFilesListTask,
        on_finished=finished,
        sourcePath=sourcePath, statusBar=statusBar
    )
    QgsApplication.taskManager().addTask( task )


#run( iface, 'D:/Users/Dell/Downloads', 'D:/Users/Dell/Downloads/teste/desc-files.csv' )
#runTask( iface, 'D:/Users/Dell/Downloads', 'D:/Users/Dell/Downloads/teste/desc-files.csv' )
