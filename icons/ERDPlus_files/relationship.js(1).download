/*jslint browser:true */
'use strict';

window.erd = window.erd || {};

(function() {

  erd.RelationshipMouseHandler = function(stage) {
    erd.BaseMouseHandler.call(this, stage);
  };

  _.assign(erd.RelationshipMouseHandler.prototype, erd.BaseMouseHandler.prototype);

  erd.RelationshipMouseHandler.prototype.onMouseDown = function(evt, x, y) {
    var relationship = this.stage.factory.relationship({
      x: x,
      y: y
    });
    this.stage.handleMouseDropItem(relationship);
  };

})();
