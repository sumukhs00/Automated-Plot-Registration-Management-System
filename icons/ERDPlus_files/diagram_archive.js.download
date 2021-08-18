/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var VERSION = 2;

  // Version History
  //
  // 1 - Initial version of ERDPlus 2.0
  // 2 - August, 2015. Adding "references" array to foreign key base_table.

  erd.DiagramArchive = function(stage) {
    this.stage = stage;
  };

  // Storing

  erd.DiagramArchive.prototype.toJson = function() {
    var data = {
      version: VERSION,
      www: 'erdplus.com',
      shapes: [],
      connectors: [],
      width: this.stage.canvas.width,
      height: this.stage.canvas.height
    };
    this.storeShapes(data);
    this.storeConnectors(data);
    return JSON.stringify(data);
  };

  erd.DiagramArchive.prototype.storeShapes = function(data) {
    for (var i = 0; i < this.stage.shapes.length; ++i) {
      var shape = this.stage.shapes[i];
      var info = {
        type: shape.getType(),
        details: _.clone(shape.details)
      };
      data.shapes.push(info);
    }
  };

  erd.DiagramArchive.prototype.storeConnectors = function(data) {
    for (var i = 0; i < this.stage.connectors.length; ++i) {
      var connector = this.stage.connectors[i];
      var info = {
        type: connector.getType(),
        details: _.clone(connector.details),
        source: connector.sourceItem.details.id,
        destination: connector.destinationItem.details.id
      };
      data.connectors.push(info);
    }
  };

  // Loading

  erd.DiagramArchive.prototype.fromJson = function(json) {
    var data = JSON.parse(json);
    this.stage.shapes = [];
    this.stage.connectors = [];
    if (typeof data.shapes !== 'undefined') {
      this.loadShapes(data.shapes);
    }
    if (typeof data.connectors !== 'undefined') {
      this.loadConnectors(data.connectors);
    }
    for (var i = 0; i < this.stage.shapes.length; ++i) {
      this.stage.shapes[i].postLoad();
    }

    // Check version
    while (data.version < VERSION) {
      switch (data.version) {
        case 1:
          this.upgrade1to2(data);
          break;
        default:
          return data;
      }
    }
    return data;
  };

  erd.DiagramArchive.prototype.loadShapes = function(shapes) {
    for (var i = 0; i < shapes.length; ++i) {
      var shape = this.createShape(shapes[i].type, shapes[i].details);
      this.stage.addItem(shape);
    }
  };

  erd.DiagramArchive.prototype.createShape = function(type, details) {
    switch (type) {
      case 'Entity':
        return this.stage.factory.entity(details);
      case 'Attribute':
        return this.stage.factory.attribute(details);
      case 'Relationship':
        return this.stage.factory.relationship(details);
      case 'Table':
        return this.stage.factory.table(details);
      case 'Fact':
        return this.stage.factory.fact(details);
      case 'Dimension':
        return this.stage.factory.dimension(details);
      case 'Label':
        return this.stage.factory.label(details);
      default:
        throw 'erd.DiagramArchive.createShape: unable to create ' + type;
    }
  };

  erd.DiagramArchive.prototype.loadConnectors = function(connectors) {
    for (var i = 0; i < connectors.length; ++i) {
      var conn = connectors[i];
      var source = this.stage.findById(conn.source);
      var destination = this.stage.findById(conn.destination);
      this.stage.connect.items(source, destination, conn.details);
    }
  };

  erd.DiagramArchive.prototype.upgrade1to2 = function(data) {
    data.version = 2;

    // data.shapes[0].details.attributes[0]
    // Set default attribute to int
    for (var j = 0; j < data.shapes.length; ++j) {
      switch (data.shapes[j].type) {
        case 'Table':
        case 'Fact':
        case 'Dimension':
          var shapeDetails = data.shapes[j].details;
          for (var k = 0; k < shapeDetails.attributes.length; ++k) {
            shapeDetails.attributes[k].dataType = 'int';
          }
          break;
      }
    }

    // Update FK
    for (var i = 0; i < data.connectors.length; ++i) {
      if (data.connectors[i].type === 'TableConnector') {
        var conn = this.stage.findById(data.connectors[i].details.id);
        var newFk = conn.pkTable.createFk();

        var existingFk = conn.fkTable.getAttributeById(conn.details.fkAttributeId);
        existingFk.references = newFk.references;
        if (newFk.names.length > 1) {
          if (existingFk !== null) {
            existingFk.names = newFk.names;
          }
        }
      }
    }
  };

})();
