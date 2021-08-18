/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  var WIDTH = 20;

  erd.EntityAnchor = function(owner, dx, dy, side) {
    erd.Anchor.call(this, owner, dx, dy);
    this.side = side;
  };

  _.assign(erd.EntityAnchor.prototype, erd.Anchor.prototype);

  erd.EntityAnchor.prototype.draw = function(context) {
    if (this.firstConnector() !== null) {
      context.save();

      var pt = this.getPoint();
      context.translate(pt.x, pt.y);
      context.fillStyle = erd.settings.shapeFill;
      context.strokeStyle = erd.settings.stroke;
      context.save();

      switch (this.side) {
        // when 'top' No rotation for top side
        case 'right':
          context.rotate(Math.PI / 2);
          break;
        case 'bottom':
          context.rotate(Math.PI);
          break;
        case 'left':
          context.rotate(Math.PI / -2);
          break;
      }


      context.beginPath();
      context.moveTo(0, 0);
      context.lineTo(0, WIDTH);
      context.stroke();

      // This entity anchor renders the details from the opposite slot.
      // This correctly follows Chen notation even though it seems wrong.
      var slotDetails = this.firstConnector().getOppositeRelationshipSlot();
      if (slotDetails !== null) {
        this.drawCardinality(context, slotDetails.cardinality);
        this.drawParticipation(context, slotDetails.participation);
        context.restore();
        this.drawExactConstraints(context, slotDetails.minimum, slotDetails.maximum);
        context.restore();
        this.drawRole(context, slotDetails.role);
      } else {
        context.restore();
        context.restore();
      }
    }
  };

  erd.EntityAnchor.prototype.drawExactConstraints = function(context, min, max) {
    if (min.length > 0 || max.length > 0) {
      if (min.length === 0) {
        min = '1';
      }
      if (max.length === 0) {
        max = 'M';
      }
      var text = '(' + min + ',' + max + ')';
      switch (this.side) {
        case 'top':
        case 'bottom':
          erd.utils.fillText(context, text, {
            x: -WIDTH / 2,
            textAlign: 'right'
          });
          break;
        case 'right':
          erd.utils.fillText(context, text, {
            y: WIDTH / 2,
            textAlign: 'left'
          });
          break;
        case 'left':
          erd.utils.fillText(context, text, {
            y: -WIDTH / 2,
            textAlign: 'right'
          });
          break;
      }
    }
  };

  erd.EntityAnchor.prototype.drawRole = function(context, role) {
    if (typeof role === 'string') {
      context.save();
      var pt1 = this.getPoint();
      var pt2 = this.firstConnector().destinationAnchor.getPoint();
      var x = (pt1.x + pt2.x) / 2;
      var y = (pt1.y + pt2.y) / 2;
      context.translate(x, y);
      erd.utils.fillText(context, role, {
        textAlign: 'center'
      });
      context.restore();
    }
  };

  erd.EntityAnchor.prototype.drawParticipation = function(context, participation) {
    if (participation === erd.ParticipationType.mandatory) {
      context.beginPath();
      context.moveTo(-8, WIDTH / 2 - 2.5);
      context.lineTo(8, WIDTH / 2 - 2.5);
      context.stroke();
    } else if (participation === erd.ParticipationType.optional) {
      context.beginPath();
      context.scale(1, 0.4);
      context.arc(0, 15, 8, 0, 2 * Math.PI, false);
      context.fill();
      context.stroke();
    }
  };

  erd.EntityAnchor.prototype.drawCardinality = function(context, cardinality) {
    if (cardinality === erd.CardinalityType.many) {
      context.moveTo(0, WIDTH - 9);
      context.lineTo(-9, WIDTH);
      context.moveTo(0, WIDTH - 9);
      context.lineTo(9, WIDTH);
      context.stroke();
    } else if (cardinality === erd.CardinalityType.one) {
      context.beginPath();
      context.moveTo(-8, WIDTH / 2 + 4.5);
      context.lineTo(8, WIDTH / 2 + 4.5);
      context.stroke();
    }
  };

})();
