/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var WIDTH = 100;
  var HEIGHT = 50;
  var HALF_WIDTH = WIDTH / 2;
  var HALF_HEIGHT = HEIGHT / 2;
  var IDENTIFYING_OFFSET_X = 8;
  var IDENTIFYING_OFFSET_Y = 5;

  erd.Relationship = function(details) {
    erd.Selectable.call(this);
    erd.AttributeOwner.call(this);
    this.details = {
      name: 'Relationship',
      isIdentifying: false,
      x: 0,
      y: 0,
      slots: [{
        slotIndex: 0,
        minimum: '',
        maximum: '',
        participation: erd.ParticipationType.unspecified,
        cardinality: erd.CardinalityType.unspecified,
        role: '',
        entityId: 0
      },{
        slotIndex: 1,
        minimum: '',
        maximum: '',
        participation: erd.ParticipationType.unspecified,
        cardinality: erd.CardinalityType.unspecified,
        role: '',
        entityId: 0
      }]
    };

    _.assign(this.details, details);

    this.centerAnchor = new erd.Anchor(this, 0, 0);
    this.outerAnchors = [
      new erd.RelationshipAnchor(this, -HALF_WIDTH, 0, 'left'),
      new erd.RelationshipAnchor(this, 0, -HALF_HEIGHT, 'top'),
      new erd.RelationshipAnchor(this, HALF_WIDTH, 0, 'right'),
      new erd.RelationshipAnchor(this, 0, HALF_HEIGHT, 'bottom')
    ];
  };

  _.assign(erd.Relationship.prototype, erd.Selectable.prototype);
  _.assign(erd.Relationship.prototype, erd.AttributeOwner.prototype);

  erd.Relationship.prototype.getType = function() {
    return 'Relationship';
  };

  erd.Relationship.prototype.getCenterPoint = function() {
    return {
      x: this.details.x,
      y: this.details.y
    };
  };

  erd.Relationship.prototype.getOppositeAnchor = function(anchor) {
    switch (anchor.side) {
      case 'left':
        return this.outerAnchors[2];
      case 'top':
        return this.outerAnchors[3];
      case 'right':
        return this.outerAnchors[0];
      case 'bottom':
        return this.outerAnchors[1];
    }
  };

  erd.Relationship.prototype.hitTest = function(x, y) {
    return (this.details.x - HALF_WIDTH < x &&
            this.details.y - HALF_HEIGHT < y &&
            this.details.x + HALF_WIDTH > x &&
            this.details.y + HALF_HEIGHT > y);
  };

  erd.Relationship.prototype.containedBy = function(rect) {
    return erd.utils.rectContainsPoint(rect, this.details.x, this.details.y);
  };

  erd.Relationship.prototype.move = function(dx, dy) {
    if (!this.moved) {
      this.moved = true;
      this.details.x += dx;
      this.details.y += dy;
      this.moveChildAttributes(dx, dy);
      this.updateConnectors();
    }
  };

  erd.Relationship.prototype.drawAsConnectTarget = function(context,strokeStyle) {
    this.draw(context);
    context.save();
    context.beginPath();
    context.translate(this.details.x, this.details.y);
    context.strokeStyle = strokeStyle;
    context.lineWidth = erd.settings.connectStrokeWidth * 2;
    context.moveTo(0, -HALF_HEIGHT);
    context.lineTo(HALF_WIDTH, 0);
    context.lineTo(0, HALF_HEIGHT);
    context.lineTo(-HALF_WIDTH, 0);
    context.closePath();
    context.stroke();
    context.restore();
  };

  erd.Relationship.prototype.draw = function(context) {
    context.save();
    context.translate(this.details.x + 0.5, this.details.y + 0.5);
    context.lineWidth = erd.settings.strokeWidth;
    context.strokeStyle = erd.settings.stroke;
    if (this.getIsSelected()) {
      context.fillStyle = erd.settings.selectedShapeFill;
    } else {
      context.fillStyle = erd.settings.shapeFill;
    }
    context.beginPath();
    context.moveTo(0, -HALF_HEIGHT);
    context.lineTo(HALF_WIDTH, 0);
    context.lineTo(0, HALF_HEIGHT);
    context.lineTo(-HALF_WIDTH, 0);
    context.closePath();
    context.fill();
    context.stroke();

    if (this.details.isIdentifying) {
      context.beginPath();
      context.moveTo(0, -HALF_HEIGHT + IDENTIFYING_OFFSET_Y);
      context.lineTo(HALF_WIDTH - IDENTIFYING_OFFSET_X, 0);
      context.lineTo(0, HALF_HEIGHT - IDENTIFYING_OFFSET_Y);
      context.lineTo(-HALF_WIDTH + IDENTIFYING_OFFSET_X, 0);
      context.closePath();
      context.stroke();
    }

    var text = this.details.name;
    if (erd.debug.enable) {
      text += ' ' + this.details.id;
    }

    erd.utils.wrapText(context, this.details.name, {
      textAlign: 'center',
      textBaseline: 'middle',
      maxWidth: WIDTH
    });

    context.restore();
  };

  erd.Relationship.prototype.updateConnectors = function() {
    for (var i = 0; i < this.outerAnchors.length; ++i) {
      var anchor = this.outerAnchors[i];
      anchor.updateAllConnectors();
    }
  };

  erd.Relationship.prototype.getSlot = function(slot) {
    if (typeof slot === 'number' && slot >= 0 && slot < this.details.slots.length) {
      return this.details.slots[slot];
    }
    return null;
  };

  erd.Relationship.prototype.getAvailableSlot = function() {
    for (var i = 0; i < this.details.slots.length; ++i) {
      if (this.details.slots[i].entityId === 0) {
        return this.details.slots[i];
      }
    }
    return null;
  };

  erd.Relationship.prototype.getSlotConnector = function(slot) {
    var entityId = this.details.slots[slot].entityId;
    for (var i = 0; i < this.outerAnchors.length; ++i) {
      var anchor = this.outerAnchors[i];
      for (var j = 0; j < anchor.connectors.length; ++j) {
        if (anchor.connectors[j].entity.details.id === entityId && anchor.connectors[j].details.slotIndex === slot) {
          return anchor.connectors[j];
        }
      }
    }
    return null;
  };

  erd.Relationship.prototype.removeFromStage = function(stage) {
    this.centerAnchor.removeAllConnectorsFromStage(stage);
    for (var i= 0; i < this.outerAnchors.length; ++i) {
      this.outerAnchors[i].removeAllConnectorsFromStage(stage);
    }
    stage.removeItem(this);
  };

  erd.Relationship.prototype.relatedEntityCount = function() {
    var count = 0;
    for (var i = 0; i < this.details.slots.length; ++i) {
      if (this.details.slots[i].entityId !== 0) {
        count += 1;
      }
    }
    return count;
  };

  erd.Relationship.prototype.getBounds = function(forMouseMove) {
    var bounds = {
      left: this.details.x - HALF_WIDTH,
      top: this.details.y - HALF_HEIGHT,
      right: this.details.x + HALF_WIDTH + 1,
      bottom: this.details.y + HALF_HEIGHT + 1
    };
    if (forMouseMove) {
      var other = this.getChildAttributeBounds();
      bounds = erd.utils.combineBounds(bounds, other);
    }
    return bounds;
  };

})();
