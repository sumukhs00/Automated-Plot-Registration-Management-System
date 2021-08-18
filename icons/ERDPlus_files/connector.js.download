/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.Connector = function(sourceItem, destinationItem, details) {
    this.sourceItem = sourceItem;
    this.destinationItem = destinationItem;
    this.sourceAnchor = null;
    this.destinationAnchor = null;
    this.details = {};
    _.assign(this.details, details);
  };

  erd.Connector.prototype.draw = function(context) {
    if (this.sourceAnchor !== null && this.destinationAnchor !== null) {
      var pt1 = this.sourceAnchor.getPoint();
      var pt2 = this.destinationAnchor.getPoint();
      context.beginPath();
      context.moveTo(pt1.x, pt1.y);
      context.lineTo(pt2.x, pt2.y);
      context.stroke();

      if (erd.debug.enable) {
        erd.utils.fillText(context, this.details.id, {
          x: (pt1.x + pt2.x) / 2,
          y: (pt1.y + pt2.y) / 2
        });
      }
    }
  };

  erd.Connector.prototype.getType = function() {
    return 'Connector';
  };

  erd.Connector.prototype.updateAnchors = function() {
    if (this.sourceAnchor === null || this.destinationAnchor === null) {
      this.sourceAnchor = this.sourceItem.centerAnchor;
      this.sourceAnchor.addConnector(this);
      this.destinationAnchor = this.destinationItem.centerAnchor;
      this.destinationAnchor.addConnector(this);
    }
  };

  erd.Connector.prototype.removeFromStage = function(stage) {
    if (this.sourceAnchor !== null) {
      this.sourceAnchor.removeConnector(this);
      this.sourceAnchor = null;
      this.sourceItem = null;
    }
    if (this.destinationAnchor !== null) {
      this.destinationAnchor.removeConnector(this);
      this.destinationAnchor = null;
      this.destinationItem = null;
    }
    stage.removeItem(this);
  };

})();
