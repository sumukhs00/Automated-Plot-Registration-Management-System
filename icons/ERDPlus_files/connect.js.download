/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.ConnectMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
    this.startShape = null;
    this.endShape = null;
    this.trackingPoint = null;
  };

  _.assign(erd.ConnectMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.ConnectMouseHandler.prototype.onMouseMove = function(evt, x, y) {
    if (this.startShape !== null) {
      var shape = this.stage.hitTest(x, y);
      if (shape !== null && shape.details.id !== this.startShape.details.id) {
        this.endShape = shape;
        this.trackingPoint = null;
      } else {
        this.endShape = null;
        this.trackingPoint = {
          x: x,
          y: y
        };
      }
      this.stage.draw();
    }
  };

  erd.ConnectMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var shape = this.stage.hitTest(x, y);
    if (shape !== null) {
      this.startShape = shape;
      this.stage.draw();
    }
  };

  erd.ConnectMouseHandler.prototype.onMouseUp = function(evt, x, y) {
    this.connect();
    this.startShape = null;
    this.endShape = null;
    this.trackingPoint = null;
    this.stage.draw();
    this.stage.invokeConnectModeEndCallback();
  };

  erd.ConnectMouseHandler.prototype.drawSpecial = function(context) {
    if (this.startShape !== null && (this.trackingPoint !== null || this.endShape !== null)) {
      var pt1 = this.startShape.getCenterPoint();
      var pt2 = this.trackingPoint;
      if (this.endShape !== null) {
        pt2 = this.endShape.getCenterPoint();
      }

      var color = erd.settings.connectMissStroke;
      if (this.canConnect()) {
        color = erd.settings.connectHitStroke;
      }

      context.save();
      context.strokeStyle = color;
      context.lineWidth = erd.settings.connectStrokeWidth;
      context.beginPath();
      context.moveTo(pt1.x, pt1.y);
      context.lineTo(pt2.x, pt2.y);
      context.stroke();
      context.restore();

      this.startShape.drawAsConnectTarget(context, color);
      if (this.endShape !== null) {
        this.endShape.drawAsConnectTarget(context, color);
      }
    }
  };

  erd.ConnectMouseHandler.prototype.canConnect = function() {
    if (this.startShape !== null && this.endShape !== null) {

      var startType = this.startShape.getType();
      var endType = this.endShape.getType();
      if (!this.limitSingleConnector(startType, endType)) {
        return false;
      }

      if (this.startShape.getType() === 'Relationship' && this.endShape.getType() === 'Relationship') {
        return false;
      }

      if (this.startShape.getType() === 'Relationship' && this.endShape.getType() === 'Entity' && this.startShape.relatedEntityCount() === 2) {
        return false;
      }

      if (this.endShape.getType() === 'Relationship' && this.startShape.getType() === 'Entity' && this.endShape.relatedEntityCount() === 2) {
        return false;
      }

      if (this.startShape.getType() === 'Attribute' && this.endShape.getType() === 'Attribute') {
        if (this.startShape.details.isComposite === false && this.endShape.details.isComposite === false) {
          return false;
        }
      }

      if (this.startShape.getType() === 'Table' && this.endShape.getType() === 'Table') {
        return this.startShape.hasPk() || this.endShape.hasPk();
      }

      if (this.startShape.getType() === 'Dimension' && (this.endShape.getType() === 'Fact' || this.endShape.getType() === 'Dimension')) {
        return this.startShape.hasPk();
      }

      if (this.startShape.getType() === 'Fact') {
        return false;
      }

      return true;

    } else {
      return false;
    }
  };

  // Limit only one connector for certain pairs
  erd.ConnectMouseHandler.prototype.limitSingleConnector = function(startType, endType) {
    var pairs = [
      ['Attribute', 'Attribute'],
      ['Attribute', 'Entity'],
      ['Attribute', 'Relationship']
    ];
    for (var i = 0; i < pairs.length; ++i) {
      if (pairs[i][0] === startType && pairs[i][1] === endType ||
          pairs[i][1] === startType && pairs[i][0] === endType) {
        var id1 = this.startShape.details.id;
        var id2 = this.endShape.details.id;
        var connector = this.stage.findConnectorByIds(id1, id2);
        if (connector !== null) {
          return false;
        }
      }
    }
    return true;
  };

  erd.ConnectMouseHandler.prototype.connect = function() {
    if (this.canConnect()) {
      this.stage.undoManager.startAction();
      if (this.startShape.getType() === 'Entity' && this.endShape.getType() === 'Entity') {
        // Create a new relationship
        var entity1 = this.startShape;
        var entity2 = this.endShape;
        var pt = {
          x: Math.round((entity1.details.x + entity2.details.x) / 2),
          y: Math.round((entity1.details.y + entity2.details.y) / 2)
        };
        var relationship = this.stage.factory.relationship(pt);
        this.stage.addItem(relationship);
        this.stage.connect.items(entity1, relationship);
        this.stage.connect.items(entity2, relationship);
        this.stage.clearSelection();
        relationship.setIsSelected(true);
        this.stage.invokeActiveItemChangedCallback(relationship);
      } else {
        this.stage.connect.items(this.startShape, this.endShape);
      }
      this.stage.undoManager.endAction();
      this.stage.resetMouseMode();
    }
  };

})();
