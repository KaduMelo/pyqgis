treeView = iface.layerTreeView()
node = treeView.currentNode()
if node.nodeType() == QgsLayerTreeNode.NodeGroup:
    total = len(node.children())
    print("Total: {} de nodes".format(total))


