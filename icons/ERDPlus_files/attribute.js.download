/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var WIDTH = 100;
  var HEIGHT = 50;
  var HALF_WIDTH = WIDTH / 2;
  var HALF_HEIGHT = HEIGHT / 2;

  erd.Attribute = function(details) {
    erd.Selectable.call(this);
    erd.AttributeOwner.call(this);
    this.details = {
      name: 'Attribute',
      isDerived: false,
      isMultivalued: false,
      isOptional: false,
      isComposite: false,
      isUnique: false,
      x: 0,
      y: 0
    };
    _.assign(this.details, details);
    this.centerAnchor = new erd.Anchor(this, 0, 0);
    this.owner = null;
  };

  _.assign(erd.Attribute.prototype, erd.Selectable.prototype);
  _.assign(erd.Attribute.prototype, erd.AttributeOwner.prototype);

  erd.Attribute.prototype.getType = function() {
    return 'Attribute';
  };

  erd.Attribute.prototype.isPartiallyUnique = function() {
    return (this.owner !== null && this.owner.getType() === 'Entity' && this.owner.details.type === 'weak');
  };

  erd.Attribute.prototype.getCenterPoint = function() {
    return {
      x: this.details.x,
      y: this.details.y
    };
  };

  erd.Attribute.prototype.hitTest = function(x, y) {
    var dx = x - this.details.x;
    var dy = y - this.details.y;
    return ((dx * dx) / (HALF_WIDTH * HALF_WIDTH) + (dy * dy) / (HALF_HEIGHT * HALF_HEIGHT) <= 1);
  };

  erd.Attribute.prototype.containedBy = function(rect) {
    return erd.utils.rectContainsPoint(rect, this.details.x, this.details.y);
  };

  erd.Attribute.prototype.move = function(dx, dy) {
    if (!this.moved) {
      this.moved = true;
      this.details.x += dx;
      this.details.y += dy;
      this.moveChildAttributes(dx, dy);
    }
  };

  erd.Attribute.prototype.getOwner = function() {
    return this.owner;
  };

  erd.Attribute.prototype.setOwner = function(owner) {
    this.owner = owner;
  };

  erd.Attribute.prototype.removeFromStage = function(stage) {
    this.centerAnchor.removeAllConnectorsFromStage(stage);
    if (this.owner !== null) {
      this.owner.removeAttribute(this);
    }
    stage.removeItem(this);
  };

  erd.Attribute.prototype.drawAsConnectTarget = function(context, strokeStyle) {
    this.draw(context);
    context.save();
    context.beginPath();
    context.translate(this.details.x, this.details.y);
    context.scale(1.0, 0.5);
    context.strokeStyle = strokeStyle;
    context.lineWidth = erd.settings.connectStrokeWidth * 2;
    context.arc(0, 0, HALF_WIDTH, 0, Math.PI * 2, false);
    context.stroke();
    context.restore();
  };

  erd.Attribute.prototype.draw = function(context) {

    context.save();
    context.translate(this.details.x, this.details.y);

    context.save();
    context.beginPath();
    context.scale(1.0, 0.5);

    if (this.details.isDerived) {
      context.setLineDash(erd.settings.dashArray);
    } else {
      context.setLineDash([]);
    }

    if (this.getIsSelected()) {
      context.fillStyle = erd.settings.selectedShapeFill;
    } else {
      context.fillStyle = erd.settings.shapeFill;
    }

    context.arc(0, 0, HALF_WIDTH, 0, Math.PI * 2, false);
    context.lineWidth = erd.settings.strokeWidth;
    context.strokeStyle = erd.settings.stroke;
    context.fill();
    context.stroke();

    if (this.details.isMultivalued) {
      context.beginPath();
      context.scale(1.0, 0.92);
      context.arc(0, 0, HALF_WIDTH - 3, 0, Math.PI * 2, false);
      context.stroke();
    }

    context.restore();

    var text = this.details.name;
    if (this.details.isOptional) {
      text = text + ' (O)';
    } else if (this.details.isComposite) {
      text = '( ' + text + ' )';
    }

    erd.utils.wrapText(context, text, {
      textAlign: 'center',
      textBaseline: 'middle',
      underline: this.details.isUnique,
      dottedUnderline: this.isPartiallyUnique(),
      maxWidth: WIDTH
    });

    context.restore();
  };

  erd.Attribute.prototype.getBounds = function(forMouseMove) {
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
