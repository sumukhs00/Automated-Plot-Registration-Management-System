/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var WIDTH = 100;
  var HEIGHT = 50;
  var HALF_WIDTH = WIDTH / 2;
  var HALF_HEIGHT = HEIGHT / 2;
  var WEAK_OFFSET = 5;
  var ANCHOR_WIDTH = 20;

  erd.EntityType = {
    Regular: 'regular',
    Weak: 'weak',
    Associative: 'associative'
  };

  erd.Entity = function(details) {
    erd.Selectable.call(this);
    erd.AttributeOwner.call(this);
    this.details = {
      name: 'Entity',
      type: erd.EntityType.Regular,
      x: 0,
      y: 0
    };
    _.assign(this.details, details);
    this.moved = false;
    this.centerAnchor = new erd.Anchor(this, 0, 0);
    this.entityAnchors = [
      new erd.EntityAnchor(this, -50 - ANCHOR_WIDTH, 0.5, 'left'),
      new erd.EntityAnchor(this, -50.5 + ANCHOR_WIDTH, -25 - ANCHOR_WIDTH, 'top'),
      new erd.EntityAnchor(this, 0.5, -25 - ANCHOR_WIDTH, 'top'),
      new erd.EntityAnchor(this, 50.5 - ANCHOR_WIDTH, -25 - ANCHOR_WIDTH, 'top'),
      new erd.EntityAnchor(this, 50 + ANCHOR_WIDTH, 0.5, 'right'),
      new erd.EntityAnchor(this, 50.5 - ANCHOR_WIDTH, 25 + ANCHOR_WIDTH, 'bottom'),
      new erd.EntityAnchor(this, 0.5, 25 + ANCHOR_WIDTH, 'bottom'),
      new erd.EntityAnchor(this, -50.5 + ANCHOR_WIDTH, 25 + ANCHOR_WIDTH, 'bottom')
    ];
  };

  _.assign(erd.Entity.prototype, erd.Selectable.prototype);
  _.assign(erd.Entity.prototype, erd.AttributeOwner.prototype);

  erd.Entity.prototype.getType = function() {
    return 'Entity';
  };

  erd.Entity.prototype.getCenterPoint = function() {
    return {
      x: this.details.x,
      y: this.details.y
    };
  };

  erd.Entity.prototype.hitTest = function(x, y) {
    return (this.details.x - HALF_WIDTH < x &&
            this.details.y - HALF_HEIGHT < y &&
            this.details.x + HALF_WIDTH > x &&
            this.details.y + HALF_HEIGHT > y);
  };

  erd.Entity.prototype.containedBy = function(rect) {
    return erd.utils.rectContainsPoint(rect, this.details.x, this.details.y);
  };

  erd.Entity.prototype.move = function(dx, dy) {
    if (!this.moved) {
      this.moved = true;
      this.details.x += dx;
      this.details.y += dy;
      this.moveChildAttributes(dx, dy);
      this.updateConnectors();
    }
  };

  erd.Entity.prototype.drawAsConnectTarget = function(context, strokeStyle) {
    this.draw(context);
    context.save();
    context.beginPath();
    context.translate(this.details.x, this.details.y);
    context.rect(-HALF_WIDTH, -HALF_HEIGHT, WIDTH, HEIGHT);
    context.strokeStyle = strokeStyle;
    context.lineWidth = erd.settings.connectStrokeWidth * 2;
    context.stroke();
    context.restore();
  };

  erd.Entity.prototype.draw = function(context) {
    context.save();
    context.translate(this.details.x + 0.5, this.details.y + 0.5);

    context.beginPath();

    if (this.getIsSelected()) {
      context.fillStyle = erd.settings.selectedShapeFill;
    } else {
      context.fillStyle = erd.settings.shapeFill;
    }

    context.rect(-HALF_WIDTH, -HALF_HEIGHT, WIDTH, HEIGHT);
    context.lineWidth = erd.settings.strokeWidth;
    context.strokeStyle = erd.settings.stroke;
    context.fill();
    context.stroke();
    context.closePath();

    if (this.details.type === erd.EntityType.Weak) {
      context.beginPath();
      context.rect(-HALF_WIDTH + WEAK_OFFSET, -HALF_HEIGHT + WEAK_OFFSET,
        WIDTH - WEAK_OFFSET * 2, HEIGHT - WEAK_OFFSET * 2);
      context.stroke();
    } else if (this.details.type === erd.EntityType.Associative) {
      context.beginPath();
      context.moveTo(0, -HALF_HEIGHT);
      context.lineTo(HALF_WIDTH, 0);
      context.lineTo(0, HALF_HEIGHT);
      context.lineTo(-HALF_WIDTH, 0);
      context.closePath();
      context.stroke();
    }

    var text = this.details.name;
    if (erd.debug.enable) {
      text = text + ' ' + this.details.id;
    }
    erd.utils.wrapText(context, text, {
      textAlign: 'center',
      textBaseline: 'middle',
      maxWidth: WIDTH
    });

    context.restore();

    for (var i = 0; i < this.entityAnchors.length; ++i) {
      this.entityAnchors[i].draw(context);
    }
  };

  erd.Entity.prototype.updateConnectors = function() {
    for (var i = 0; i < this.entityAnchors.length; ++i) {
      var anchor = this.entityAnchors[i];
      anchor.updateAllConnectors();
    }
  };

  erd.Entity.prototype.removeFromStage = function(stage) {
    this.centerAnchor.removeAllConnectorsFromStage(stage);
    for (var i= 0; i < this.entityAnchors.length; ++i) {
      this.entityAnchors[i].removeAllConnectorsFromStage(stage);
    }
    stage.removeItem(this);
  };

  erd.Entity.prototype.getBounds = function(forMouseMove) {
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
