from qgis.core import (Qgis, QgsCoordinateReferenceSystem, QgsProject)
from qgis import utils as QgsUtils

from qgis.PyQt.QtWidgets import QApplication

crs4326 = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId)
proj4Layer = "[% layer_property(@layer_id, 'crs_definition') %]"
crsLayer = QgsCoordinateReferenceSystem.fromProj4(proj4Layer)
wkt = "[% geom_to_wkt( $geometry ) %]"
geom = QgsGeometry.fromWkt(wkt)

if not crsLayer == crs4326:
    ct = QgsCoordinateTransform(crsLayer, crs4326, QgsProject.instance())
    geom.transform(ct)
    json = geom.asJson()
del geom
cb = QApplication.clipboard()
cb.setText(json)

title = "'Geojson' to Clipboard"
nameLayer = "[% @layer_name %]"
msg  = "Copied to Clipboard(CRS = 4326)"
QgsUtils.iface.messageBar().pushMessage(title, msg, Qgis.Info)