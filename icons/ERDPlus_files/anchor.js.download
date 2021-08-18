/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.Anchor = function(owner, dx, dy) {
    this.owner = owner;
    this.dx = dx;
    this.dy = dy;
    this.connectors = [];
  };

  erd.Anchor.prototype.setOffsetX = function(dx) {
    this.dx = dx;
  };

  erd.Anchor.prototype.setOffsetY = function(dy) {
    this.dy = dy;
  };

  // Returns the point of the anchor used as an endpoint for connectors.
  erd.Anchor.prototype.getPoint = function() {
    var pt = this.owner.getCenterPoint();
    return {
      x: pt.x + this.dx,
      y: pt.y + this.dy
    };
  };

  erd.Anchor.prototype.addConnector = function(connector) {
    this.connectors.push(connector);
  };

  erd.Anchor.prototype.removeConnector = function(connector) {
    this.connectors = _.reject(this.connectors, function(conn) {
      return conn.details.id === connector.details.id;
    });
  };

  erd.Anchor.prototype.firstConnector = function() {
    if (this.connectors.length > 0) {
      return this.connectors[0];
    }
    return null;
  };

  erd.Anchor.prototype.countConnectors = function() {
    return this.connectors.length;
  };

  erd.Anchor.prototype.updateAllConnectors = function() {
    for (var i = 0; i < this.connectors.length; ++i) {
      this.connectors[i].updateAnchors();
    }
  };

  erd.Anchor.prototype.removeAllConnectorsFromStage = function(stage) {
    for (var i = this.connectors.length - 1; i >= 0; --i) {
      var connector = this.connectors[i];
      connector.removeFromStage(stage);
    }
  };

})();
