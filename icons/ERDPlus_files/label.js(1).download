/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var HANDLE_OFFSET = 20;
  var MIN_WIDTH = 50;
  var MIN_HEIGHT = 50;

  erd.Label = function(details) {
    erd.Selectable.call(this);
    this.details = {
      text: 'New Label',
      x: 0, // top,left
      y: 0,
      width: 100,
      height: 50
    };
    _.assign(this.details, details);
    this.moved = false;
  };

  _.assign(erd.Label.prototype, erd.Selectable.prototype);

  erd.Label.prototype.getType = function() {
    return 'Label';
  };

  erd.Label.prototype.hitTest = function(x, y) {
    return (this.details.x < x &&
            this.details.y < y &&
            this.details.x + this.details.width > x &&
            this.details.y + this.details.height > y);
  };

  erd.Label.prototype.hitTestResize = function(x, y) {
    return (this.details.x + this.details.width - HANDLE_OFFSET < x &&
            this.details.y + this.details.height - HANDLE_OFFSET < y &&
            this.details.x + this.details.width > x &&
            this.details.y + this.details.height > y);
  };

  erd.Label.prototype.containedBy = function(rect) {
    var x = this.details.x + this.details.width / 2;
    var y = this.details.y + this.details.height / 2;
    return erd.utils.rectContainsPoint(rect, x, y);
  };

  erd.Label.prototype.move = function(dx, dy) {
    if (!this.moved) {
      this.moved = true;
      this.details.x += dx;
      this.details.y += dy;
    }
  };

  erd.Label.prototype.resizeLabel = function(dx, dy) {
    this.details.width = Math.max(this.details.width + dx, MIN_WIDTH);
    this.details.height = Math.max(this.details.height + dy, MIN_HEIGHT);
  };

  erd.Label.prototype.draw = function(context) {
    context.save();
    context.translate(this.details.x + 0.5, this.details.y + 0.5);

    context.beginPath();
    if (this.getIsSelected()) {
      context.fillStyle = erd.settings.selectedShapeFill;
    } else {
      context.fillStyle = erd.settings.shapeFill;
    }
    context.lineWidth = erd.settings.strokeWidth;
    context.strokeStyle = erd.settings.stroke;
    context.lineWidth = erd.settings.lineWidth;
    context.rect(0, 0, this.details.width, this.details.height);
    context.fill();

    if (this.getIsSelected()) {
      context.stroke();

      context.beginPath();
      var x = this.details.width; // bottom right corner
      var y = this.details.height;
      context.fillStyle = erd.settings.labelResizeShapeFill;
      context.moveTo(x - HANDLE_OFFSET, y);
      context.lineTo(x, y - HANDLE_OFFSET);
      context.lineTo(x, y);
      context.fill();
      context.stroke();
    }

    erd.utils.wrapText(context, this.details.text, {
      x: 2,
      textAlign: 'left',
      textBaseline: 'top',
      width: this.details.width - 4, // allow 2px margin both sides
      height: this.details.height
    });

    context.restore();
  };

  erd.Label.prototype.drawAsConnectTarget = function(context, strokeStyle) {
  };

  erd.Label.prototype.getBounds = function(forMouseMove) {
    var bounds = {
      left: this.details.x,
      top: this.details.y,
      right: this.details.x + this.details.width + 1,
      bottom: this.details.y + this.details.height + 1
    };
    return bounds;
  };

  erd.Label.prototype.removeFromStage = function(stage) {
    stage.removeItem(this);
  };

})();
