/*jslint browser:true */
"use strict";

window.erd = window.erd || {};

(function() {
  erd.DiagramStage = function(canvasElement, options) {
    this.factory = new erd.Factory(this);
    this.connect = new erd.ConnectHelper(this);
    this.shapes = [];
    this.connectors = [];
    this.canvas = canvasElement;
    this.context = this.canvas.getContext("2d");
    this.undoManager = new erd.UndoManager(this);
    this.options = options;

    erd.debug._activeStage = this;
    this.scaleX = 1;
    this.scaleY = 1;

    attachMouseEvent(this, "mousemove", this.onMouseMove);
    attachMouseEvent(this, "mousedown", this.onMouseDown);
    attachMouseEvent(this, "mouseup", this.onMouseUp);
    this.mouseHandlers = {
      select: new erd.SelectMouseHandler(this),
      connect: new erd.ConnectMouseHandler(this),
      entity: new erd.EntityMouseHandler(this),
      attribute: new erd.AttributeMouseHandler(this),
      relationship: new erd.RelationshipMouseHandler(this),
      table: new erd.TableMouseHandler(this),
      fact: new erd.FactMouseHandler(this),
      dimension: new erd.DimensionMouseHandler(this),
      label: new erd.LabelMouseHandler(this),
      none: new erd.NoneMouseHandler(this)
    };
    this.resetMouseMode();
  };

  erd.DiagramStage.prototype.setScale = function(sx, sy) {
    this.scaleX = sx;
    this.scaleY = sy;
  };

  erd.DiagramStage.prototype.clear = function() {
    this.factory = new erd.Factory(this);
    this.shapes = [];
    this.connectors = [];
    this.undoManager.clear();
  };

  erd.DiagramStage.prototype.handleMouseDropItem = function(item) {
    this.undoManager.startAction();
    this.addItem(item);
    this.draw();
    this.undoManager.endAction();
    this.invokeActiveItemChangedCallback(item);
    this.resetMouseMode();
  };

  erd.DiagramStage.prototype.invokeActiveItemChangedCallback = function(item) {
    this.options.activeItemChangedCallback(item);
  };

  erd.DiagramStage.prototype.invokeStartMoveCallback = function() {
    this.options.startMoveCallback();
  };

  erd.DiagramStage.prototype.invokeEndMoveCallback = function() {
    this.options.endMoveCallback();
  };

  erd.DiagramStage.prototype.invokeConnectModeEndCallback = function() {
    this.options.connectModeEndCallback();
  };

  erd.DiagramStage.prototype.invokeDirtyCallback = function() {
    this.options.dirtyCallback();
  };

  erd.DiagramStage.prototype.invokeMouseModeResetCallback = function() {
    this.options.mouseModeResetCallback(this.mouseMode);
  };

  erd.DiagramStage.prototype.hitTest = function(x, y) {
    for (var i = this.shapes.length - 1; i >= 0; i--) {
      if (this.shapes[i].hitTest(x, y)) {
        return this.shapes[i];
      }
    }
    return null;
  };

  erd.DiagramStage.prototype.moveSelectedShapes = function(dx, dy) {
    for (var i = 0; i < this.shapes.length; ++i) {
      if (this.shapes[i].getIsSelected()) {
        this.shapes[i].move(dx, dy);
      }
    }
    for (var j = 0; j < this.shapes.length; ++j) {
      this.shapes[j].moved = false;
    }
  };

  erd.DiagramStage.prototype.onMouseMove = function(evt, x, y) {
    this.mouseHandlers[this.mouseMode].onMouseMove(evt, x, y);
  };

  erd.DiagramStage.prototype.onMouseDown = function(evt, x, y) {
    this.mouseHandlers[this.mouseMode].onMouseDown(evt, x, y);
    this.options.selectedCountChange();
  };

  erd.DiagramStage.prototype.onMouseUp = function(evt, x, y) {
    this.mouseHandlers[this.mouseMode].onMouseUp(evt, x, y);
    this.options.selectedCountChange();
  };

  erd.DiagramStage.prototype.draw = function() {
    var context = this.context;
    context.save();
    context.clearRect(0, 0, this.canvas.width, this.canvas.height);
    context.scale(this.scaleX, this.scaleY);

    // var bounds = this.getBounds(false);
    // context.beginPath();
    // context.moveTo(bounds.left, bounds.top);
    // context.lineTo(bounds.right, bounds.top);
    // context.lineTo(bounds.right, bounds.bottom);
    // context.lineTo(bounds.left, bounds.bottom);
    // context.lineTo(bounds.left, bounds.top);
    // context.stroke();

    for (var j = 0; j < this.connectors.length; ++j) {
      this.connectors[j].draw(context);
    }
    for (var i = 0; i < this.shapes.length; ++i) {
      this.shapes[i].draw(context);
    }
    context.restore();

    this.mouseHandlers[this.mouseMode].drawSpecial(context);
  };

  erd.DiagramStage.prototype.clearSelection = function() {
    for (var i = 0; i < this.shapes.length; i++) {
      this.shapes[i].clearSelection();
    }
  };

  erd.DiagramStage.prototype.selectedCount = function() {
    var count = 0;
    for (var i = this.shapes.length - 1; i >= 0; i--) {
      var shape = this.shapes[i];
      if (shape.getIsSelected()) {
        count += 1;
      }
    }
    return count;
  };

  erd.DiagramStage.prototype.selectByRect = function(rect) {
    for (var i = 0; i < this.shapes.length; ++i) {
      if (this.shapes[i].containedBy(rect)) {
        this.shapes[i].setIsSelected(true);
      }
    }
  };

  erd.DiagramStage.prototype.deleteSelection = function() {
    if (this.selectedCount() > 0) {
      this.undoManager.startAction();
      for (var i = this.shapes.length - 1; i >= 0; i--) {
        var shape = this.shapes[i];
        if (shape.getIsSelected()) {
          this.shapes[i].removeFromStage(this);
        }
      }
      this.undoManager.endAction();
    }
  };

  erd.DiagramStage.prototype.selectItem = function(item) {
    this.clearSelection();
    item.setIsSelected(true);
    this.invokeActiveItemChangedCallback(item);
  };

  erd.DiagramStage.prototype.addItem = function(item) {
    switch (item.getType()) {
      case "Entity":
      case "Attribute":
      case "Relationship":
      case "Table":
      case "Fact":
      case "Dimension":
      case "Label":
        this.shapes.push(item);
        break;
      case "Connector":
      case "RelationshipConnector":
      case "TableConnector":
        item.updateAnchors();
        this.connectors.push(item);
        break;
      default:
        throw "erd.DiagramStage.addItem unable to add " + item.getType();
    }
  };

  erd.DiagramStage.prototype.removeItem = function(item) {
    switch (item.getType()) {
      case "Entity":
      case "Attribute":
      case "Relationship":
      case "Table":
      case "Fact":
      case "Dimension":
      case "Label":
        this.shapes = _.reject(this.shapes, function(i) {
          return i.details.id === item.details.id;
        });
        break;
      case "Connector":
      case "RelationshipConnector":
      case "TableConnector":
        this.connectors = _.reject(this.connectors, function(c) {
          return c.details.id === item.details.id;
        });
        break;
      default:
        throw "erd.DiagramStage.removeItem unable to remove " + item.getType();
    }
  };

  erd.DiagramStage.prototype.findById = function(id) {
    if (typeof id === "string") {
      id = parseInt(id);
    }
    for (var i = 0; i < this.shapes.length; ++i) {
      if (this.shapes[i].details.id === id) {
        return this.shapes[i];
      }
    }
    for (var j = 0; j < this.connectors.length; ++j) {
      if (this.connectors[j].details.id === id) {
        return this.connectors[j];
      }
    }
    return null;
  };

  erd.DiagramStage.prototype.findConnectorByIds = function(id1, id2) {
    for (var i = 0; i < this.connectors.length; ++i) {
      var connector = this.connectors[i];
      if (
        (connector.sourceItem.details.id === id1 && connector.destinationItem.details.id === id2) ||
        (connector.sourceItem.details.id === id2 && connector.destinationItem.details.id === id1)
      ) {
        return connector;
      }
    }
    return null;
  };

  erd.DiagramStage.prototype.findByName = function(name) {
    for (var i = 0; i < this.shapes.length; ++i) {
      if (this.shapes[i].details.name === name) {
        return this.shapes[i];
      }
    }
    return null;
  };

  erd.DiagramStage.prototype.findAllByType = function(type) {
    var found = [];
    for (var i = 0; i < this.shapes.length; ++i) {
      if (this.shapes[i].getType() === type) {
        found.push(this.shapes[i]);
      }
    }
    return found;
  };

  erd.DiagramStage.prototype.resetMouseMode = function() {
    this.mouseMode = "select";
    this.invokeMouseModeResetCallback();
  };

  /*
   * Get the bounding rectangle of all shapes, or just for those shapes that will
   * be moved during a mouse drag opertion (that includes child attributes).
   */
  erd.DiagramStage.prototype.getBounds = function(forMouseMove) {
    var bounds = {
      left: Number.MAX_VALUE,
      top: Number.MAX_VALUE,
      right: Number.MIN_VALUE,
      bottom: Number.MIN_VALUE
    };
    for (var i = 0; i < this.shapes.length; ++i) {
      if (forMouseMove && this.shapes[i].getIsSelected()) {
        var other = this.shapes[i].getBounds(true);
        bounds = erd.utils.combineBounds(bounds, other);
      } else if (!forMouseMove) {
        var other = this.shapes[i].getBounds(false);
        bounds = erd.utils.combineBounds(bounds, other);
      }
    }
    return bounds;
  };

  // Add an event handler that converts the coordinates and invokes the callback.
  var attachMouseEvent = function(diagramStage, name, callback) {
    diagramStage.canvas.addEventListener(name, function(evt) {
      evt.stopImmediatePropagation();
      var rect = diagramStage.canvas.getBoundingClientRect();
      var x = evt.clientX - rect.left;
      var y = evt.clientY - rect.top;
      callback.call(diagramStage, evt, x, y);
    });
  };
})();
