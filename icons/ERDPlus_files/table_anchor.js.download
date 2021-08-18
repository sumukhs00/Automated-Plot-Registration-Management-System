/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var WIDTH = 20;

  erd.TableAnchor = function(owner, dx, dy, side, attributeId) {
    erd.Anchor.call(this, owner, dx, dy);
    this.side = side;
    this.attributeId = attributeId;
  };

  _.assign(erd.TableAnchor.prototype, erd.Anchor.prototype);

  erd.TableAnchor.prototype.getPoint = function() {
    if (this.side === 'left') {
      return {
        x: this.owner.details.x + this.dx - WIDTH,
        y: this.owner.details.y + this.dy
      };
    } else {
      return {
        x: this.owner.details.x + this.dx + WIDTH,
        y: this.owner.details.y + this.dy
      };
    }
  };

  erd.TableAnchor.prototype.getAnchorWidth = function() {
    return WIDTH;
  };

  erd.TableAnchor.prototype.draw = function(context) {
    if (this.firstConnector() !== null) {
      var pt = this.getPoint();

      context.save();
      context.translate(pt.x, pt.y);
      if (this.side === 'right') {
        context.rotate(Math.PI);
      }

      context.strokeStyle = erd.settings.stroke;
      context.beginPath();
      context.moveTo(0, 0);
      context.lineTo(WIDTH, 0);
      context.stroke();

      if (this.isPkAnchor()) {
        context.beginPath();
        context.fillStyle = erd.settings.arrowFill;
        context.moveTo(WIDTH, 0);
        context.lineTo(WIDTH - 5, 0 - 5);
        context.lineTo(WIDTH - 5, 0 + 5);
        context.closePath();
        context.stroke();
        context.fill();
      }

      context.restore();
    }
  };

  erd.TableAnchor.prototype.isPkAnchor = function() {
    return this.attributeId === 0;
  };

})();
